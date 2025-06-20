import time
import cv2
import numpy as np
from anomalib.data import Folder
from anomalib.deploy import OpenVINOInferencer
from anomalib.engine import Engine
from anomalib.models import EfficientAd, Padim, Patchcore
from anomalib.post_processing import PostProcessor
from anomalib.pre_processing import PreProcessor
from anomalib.utils.visualization import ImageResult
from torchvision.transforms.v2 import Compose, Resize
from src.modules.utils import get_resource_path,quick_stability_check
from src.global_params import detect_lcd_params,abnormal_inference_params,abnormal_train_params,system_config_params,camera_config_params
import logging
import datetime

logger = logging.getLogger('app')

class AnomalyDetection:
    def __init__(self):
        self.is_detected_CCD = False
        self.is_abnormal = True
        self.result_color = (0,0,255)
        if abnormal_inference_params.inference_type.upper() == 'OPENVINO':
            self.inferencer = OpenVINOInferencer(get_resource_path(abnormal_inference_params.model_path))

        self.pixel_width = camera_config_params.sensor_size[0] /  3840 * 1000
        self.pixel_height = camera_config_params.sensor_size[1] /  2160 * 1000
    def adaptive_image_to_binary(self,img):
        """using adaptive threshold for image have lighting condition are not uniform"""
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Làm mờ để giảm nhiễu (rất quan trọng trước adaptive)
        blurred_image = cv2.GaussianBlur(gray_image, tuple(detect_lcd_params.kernel_blur_size), 0)

        binary_image = cv2.adaptiveThreshold(
            blurred_image,
            maxValue=255,
            adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,  # hoặc ADAPTIVE_THRESH_MEAN_C,ADAPTIVE_THRESH_GAUSSIAN_C  
            thresholdType=cv2.THRESH_BINARY,
            blockSize=detect_lcd_params.block_size,   # Kích thước vùng xung quanh (nên là số lẻ)
            C=detect_lcd_params.C    # Giá trị trừ sau khi tính trung bình, giúp cân chỉnh độ nhạy
        )

        return binary_image

    def border_gaps_binary_image(self, binary_img):
        # 1. Đảo ảnh: vùng đen thành trắng, vùng trắng thành đen
        inverted = cv2.bitwise_not(binary_img)

        # 2. Morph closing để nối vùng trắng (tức là nối lại viền đen trong ảnh gốc)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (detect_lcd_params.kernel_size, detect_lcd_params.kernel_size))
        closed = cv2.morphologyEx(inverted, cv2.MORPH_CLOSE, kernel)

        # 3. Đảo lại ảnh: vùng trắng thành đen, vùng đen thành trắng
        repaired = cv2.bitwise_not(closed)
        
        return repaired
    
    def get_top_left_point_box(self,box):
        """
        get top left coordinates of the box to perform the translation .
        """
        box = np.array(box, dtype="float32")

        # Tính tổng x + y => top-left sẽ có tổng nhỏ nhất
        s = box.sum(axis=1)
        top_left = box[np.argmin(s)]

        return tuple(map(int, top_left))
    #nếu detect ra thì self.is_detected_LCD = True
    def detect_ccd(self, img):
        self.is_detected_CCD = False
        if isinstance(img, str):
            img = cv2.imread(img)
        if img is None:
            logger.warning("Cannot detect LCD: Image is None or not loaded properly.")
            return None
        
        original_img = img.copy()
        #preprocessing
        binary_image = self.adaptive_image_to_binary(img)
        binary_image = self.border_gaps_binary_image(binary_image)
        
        #get area of interest
        h_image, w_image = img.shape[:2]
        center = (w_image // 2, h_image // 2)
        total_area = w_image * h_image
        
        # load area thresholds
        min_valid_area = total_area * detect_lcd_params.min_LCD_area_ratio
        max_valid_area = total_area * detect_lcd_params.max_LCD_area_ratio

        # find contours
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return None
        
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        best_contour = None
        smallest_area = float('inf')

        for contour in contours:
            (cx, cy), (cw, ch), angle = cv2.minAreaRect(contour)
            if max(cw,ch) >= detect_lcd_params.max_LCD_w_h_ratio * w_image or min(cw,ch) >= detect_lcd_params.max_LCD_w_h_ratio * h_image:
                continue  # Loại bỏ contour quá lớn so với ảnh
            area = cv2.contourArea(contour)
            
            # Early termination if area too small
            if area < min_valid_area:
                break
            if area > max_valid_area:
                continue
            
            if area < smallest_area:
                smallest_area = area
                best_contour = contour

        if best_contour is None:
            logger.debug("No valid contour found within area thresholds.")
            return None
        
        rect = cv2.minAreaRect(best_contour)
        (cx, cy), (cw, ch), angle = rect

        if cw < ch:
            angle -= 90
        
        # Get box coordinates
        box = np.int32(cv2.boxPoints(rect))

        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_image = cv2.warpAffine(
            img, rotation_matrix, (w_image, h_image),
            flags=cv2.INTER_CUBIC, 
            borderMode=cv2.BORDER_REPLICATE
        )

        rotated_box = cv2.transform(np.array([box]), rotation_matrix)[0]
        min_x = max(0, int(np.min(rotated_box[:, 0])))
        max_x = min(w_image, int(np.max(rotated_box[:, 0])))
        min_y = max(0, int(np.min(rotated_box[:, 1])) - detect_lcd_params.expand_crop_top)
        max_y = min(h_image, int(np.max(rotated_box[:, 1])) + detect_lcd_params.expand_crop_bot)
        # min_y = max(0, int(np.min(rotated_box[:, 1])))
        # max_y = min(h_image, int(np.max(rotated_box[:, 1])))
        

        top_left_point = self.get_top_left_point_box(rotated_box)

        cropped_image = rotated_image[min_y:max_y, min_x:max_x]
        
        self.is_detected_LCD = True
        return {
            "original_image": original_img,
            "binary_image": binary_image,
            "rotated_image": rotated_image,
            "cropped_image": cropped_image,
            "ccd_box_original": box,
            "top_left_point": top_left_point,
            "ccd_box_rotated": rotated_box,
            'rotate_angle': angle,
            'center': center,
        }

    def test_detect_ccd(self,video_source):
        cap = cv2.VideoCapture(video_source)
        if not cap.isOpened():
            logger.debug("Cannot open video source.")
            exit(1)
        while True:
            ret, frame = cap.read()
            if not ret:
                logger.info("End of video stream.")
                break
            
            result = self.detect_ccd(frame)
            if result is not None:
                original_image = result["original_image"]
                binary_image = result["binary_image"]
                rotated_image = result["rotated_image"]
                cropped_image = result["cropped_image"]
                ccd_box_original = result["ccd_box_original"]
                ccd_box_rotated = result["ccd_box_rotated"]

                # Draw the CCD box on the rotated image
                cv2.polylines(original_image, [ccd_box_original.astype(np.int32)], isClosed=True, color=(0, 255, 0), thickness=2)
                cv2.imshow("CCD Box on Rotated Image", original_image)
            else:
                cv2.imshow("CCD Box on Rotated Image", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    ##
    ##
    ## check anomaly detection
    def train(self):
        params = abnormal_train_params
        datamodule = Folder(
            name=params.dataset_name,
            # root=r"F:\AI\Vision\check_bui\Dust_Checking\Dust_Checking\train",
            normal_dir = params.normal_dir,
            abnormal_dir = params.abnormal_dir,
            # normal_test_dir=r"F:\AI\Vision\check_bui\Dust_Checking\Dust_Checking\test\good",
            train_batch_size = params.train_batch_size,
            # num_workers = 8,
            normal_split_ratio = params.normal_split_ratio,
            test_split_ratio = params.test_split_ratio,
        )
        datamodule.setup()

        transform = Compose([
            Resize(size=(params.image_size, params.image_size))]) 
        
        pre_processor = PreProcessor(transform=transform)
        
        post_processor = PostProcessor(
            image_sensitivity=params.post_processing_image_sensitivity,
            pixel_sensitivity=params.post_processing_pixel_sensitivity)
        
        if params.model_type.upper() == 'PADIM':
            self.model = Padim(
            pre_processor=pre_processor,
            post_processor=post_processor
            # backbone="resnet18",  # Feature extraction backbone
            # layers=["layer1", "layer2", "layer3"],
            # Layers to extract features from
            # pre_trained=True,  # Use pretrained weights
            # n_features=100,  # Number of features to retain
            
            )
        elif params.model_type.upper() == 'EfficientAd'.upper():
            self.model = EfficientAd(
            pre_processor=pre_processor,
            post_processor=post_processor,
            imagenet_dir="./datasets/imagenette",
            # model_size="s",
            )
        elif params.model_type.upper() == 'Patchcore'.upper():
            self.model = Patchcore(
            pre_processor=pre_processor,
            post_processor=post_processor,
            backbone="wide_resnet50_2",
            layers=["layer2", "layer3"],
            coreset_sampling_ratio=0.1
            )
        
        engine = Engine(accelerator=params.accelerator,default_root_dir='train_results')
        engine.train(datamodule=datamodule, model=self.model)

    def inference(self,image):
        if isinstance(image, str):
            image = cv2.imread(image)
        if image is None:
            logger.error("Cannot perform predict abnomal: Image is None or not loaded properly.")
            return None
        else:
            predictions = self.inferencer.predict(image)
            predictions = ImageResult.from_dataset_item(predictions.items[0])
            anomaly_score = predictions.pred_score
            heat_map = predictions.heat_map
            
            return {
                'original_image':image,
                'anormaly_score':anomaly_score,
                'heat_map':heat_map,
            }

    def normalize_rgb_heatmap_sum(self, heatmap_rgb):
        # Chuyển sang float để tránh tràn số khi cộng
        heatmap_rgb = heatmap_rgb.astype(np.float32)
        
        # Cộng tổng 3 kênh màu tại mỗi pixel
        summed = heatmap_rgb.sum(axis=2)  # shape (H, W)
        
        # Chia cho max tổng có thể có = 255 * 3 để chuẩn hóa về [0,1]
        normalized = summed / (255.0 * 3)
        
        # Trừ đi giá trị nhỏ nhất để "shift" về 0
        min_val = normalized.min()
        normalized_shifted = normalized - min_val
        
        # Nếu min_val == max_val thì kết quả toàn 0, tránh giá trị âm
        normalized_shifted = np.clip(normalized_shifted, 0, 1)
        
        return normalized_shifted  

    def normalize_heatmap_to_binary(self, heat_map):
        
        binary_map = np.zeros_like(heat_map, dtype=np.uint8)
        binary_map[heat_map >= abnormal_inference_params.heat_map_NG_thresh_hold] = 255
        return binary_map

    def dust_detect_on_image(self, image):
        self.is_abnormal = True
        if isinstance(image, str):
            image = cv2.imread(image)
        if image is None:
            logger.error("Cannot perform detect dust: Image is None or not loaded properly.")
            return None
        
        # initialize images to return
        image_with_dust = image.copy()
        image_with_heatmap = image.copy()

        # 1. Detect LCD
        detect_lcd_result = self.detect_ccd(image)
        if detect_lcd_result is None:
            logger.info("No valid LCD detected in the image.")
            return None

        cropped_image = detect_lcd_result['cropped_image']
        rotate_angle = detect_lcd_result['rotate_angle']
        top_left_point = detect_lcd_result['top_left_point'] #top left point in original image
        center = detect_lcd_result['center']
        original_box = detect_lcd_result['ccd_box_original']
            
        if cropped_image is not None:
            height, width = cropped_image.shape[:2]  
            abnormal_result = self.inference(cropped_image)
            if abnormal_result is not None:
                h_image, w_image = image.shape[:2]
                center = (w_image // 2, h_image // 2)
                M_back = cv2.getRotationMatrix2D(center, -rotate_angle, 1.0)
                
                # Resize heatmap về kích thước của cropped image
                original_heat_map = cv2.resize(abnormal_result['heat_map'], (int(width), int(height)))

                # Tạo ảnh trống cùng size ảnh gốc
                blank_heatmap = np.zeros_like(image)

# Dán heatmap vào vị trí top_left_point với kiểm tra bounds
                x0, y0 = top_left_point
                heat_h, heat_w = original_heat_map.shape[:2]

                # Tính toán vùng giao nhau (intersection)
                # Vùng đích trong ảnh gốc
                dst_x0 = max(0, x0)
                dst_y0 = max(0, y0)
                dst_x1 = min(x0 + heat_w, w_image)
                dst_y1 = min(y0 + heat_h, h_image)

                # Vùng nguồn trong heatmap
                src_x0 = max(0, -x0)
                src_y0 = max(0, -y0)
                src_x1 = src_x0 + (dst_x1 - dst_x0)
                src_y1 = src_y0 + (dst_y1 - dst_y0)

                # Kiểm tra vùng hợp lệ
                if dst_y1 > dst_y0 and dst_x1 > dst_x0 and src_y1 > src_y0 and src_x1 > src_x0:
                    # Đảm bảo không vượt quá bounds của heatmap
                    src_y1 = min(src_y1, heat_h)
                    src_x1 = min(src_x1, heat_w)
                    
                    # Crop heatmap
                    heat_crop = original_heat_map[src_y0:src_y1, src_x0:src_x1]
                    
                    # Tính lại vùng đích cho khớp
                    actual_h, actual_w = heat_crop.shape[:2]
                    dst_y1 = dst_y0 + actual_h
                    dst_x1 = dst_x0 + actual_w
                    
                    # Đảm bảo không vượt quá bounds của ảnh đích
                    if dst_y1 <= h_image and dst_x1 <= w_image:
                        blank_heatmap[dst_y0:dst_y1, dst_x0:dst_x1] = heat_crop
                    else:
                        logger.warning(f"Destination bounds exceed image: dst_end=({dst_y1},{dst_x1}), image_size=({h_image},{w_image})")
                else:
                    logger.warning(f"Invalid bounds: dst({dst_y0}:{dst_y1}, {dst_x0}:{dst_x1}), src({src_y0}:{src_y1}, {src_x0}:{src_x1})")

                # Xoay toàn bộ heatmap quanh tâm ảnh gốc
                rotated_heatmap_full = cv2.warpAffine(blank_heatmap, M_back, (w_image, h_image))

                # Ghép heatmap xoay vào ảnh gốc
                
                image_with_heatmap = cv2.addWeighted(image_with_heatmap, 
                                                     1.0, 
                                                     rotated_heatmap_full, 
                                                     abnormal_inference_params.heat_map_display_alpha, 
                                                     0)


                # 2. Dilation heatmap để tìm vùng
                normalize_rgb_sum = self.normalize_rgb_heatmap_sum(original_heat_map)
                max_value_abnormal = np.max(normalize_rgb_sum)  
                logger.debug(f"Max value in heatmap: {max_value_abnormal}")
                binary_heatmap = self.normalize_heatmap_to_binary(normalize_rgb_sum)

                kernel = np.ones((15, 15), dtype=np.uint8)
                dilated_heatmap = cv2.dilate(binary_heatmap, kernel, iterations=1)

                # 3. Tìm contours trên ảnh đã xử lý
                contours, _ = cv2.findContours(dilated_heatmap, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                if len(contours) == 0:
                    self.result_color = tuple(abnormal_inference_params.ok_color)
                    self.is_abnormal = False
                    # image_with_dust = cv2.polylines(image_with_dust, [original_box], True, self.result_color, 2, cv2.LINE_AA)
                else:
                    self.result_color = tuple(abnormal_inference_params.ng_color)
                    self.is_abnormal = False
                    rotated_contours = []
                    contour_global = None
                    # Vẽ contours lên ảnh gốc
                    x,y,w,h = None, None, None, None
                    count = 0
                    for contour in contours:
                        x, y, w, h = cv2.boundingRect(contour)
                        if max(w, h) >= abnormal_inference_params.max_ratio_w_h_cnt * min(w, h):
                            continue
                        count += 1
                        self.is_abnormal = True
                        # Tạo mask để đo số điểm bất thường
                        mask = np.zeros(original_heat_map.shape[:2], dtype=np.uint8)
                        cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED) # type: ignore
                        heatmap_values = normalize_rgb_sum[mask == 255]
                        if heatmap_values.size == 0:
                            continue
                        max_val = np.max(heatmap_values)
                        logger.debug(f"Max abnormal score: {max_val}")
                        threshold = abnormal_inference_params.brightness_threshold_caculate_dust_size * max_val
                        abnormal_pixel_count = np.sum(heatmap_values >= threshold)

                       
                        area_dust = self.pixel_width * self.pixel_height * abnormal_pixel_count

                        # Tính tâm contour để hiển thị số điểm

                        contour_global = contour + np.array([[[top_left_point[0], top_left_point[1]]]])
                        # 2. Chuyển contour sang float để nhân affine
                        contour_global = contour_global.astype(np.float32)
                        # 3. Áp dụng ma trận xoay affine
                        contour_rotated = cv2.transform(contour_global, M_back)
                        # 4. Chuyển lại về int nếu muốn vẽ
                        contour_rotated = contour_rotated.astype(np.int32)
                        rotated_contours.append(contour_rotated)

                        M = cv2.moments(contour_rotated)
                        if M["m00"] != 0:
                            cx_text = int(M["m10"] / M["m00"]) + 7
                            cy_text = int(M["m01"] / M["m00"])
                            position_rotated = (int(cx_text), int(cy_text))
                        else:
                            position_rotated = (int(contour_rotated[0][0][0]), int(contour_rotated[0][0][1]))
                    # Vẽ contours đã xoay lên ảnh gốc
                        cv2.putText(
                            image_with_dust,
                            f"{int(area_dust)} um",
                            position_rotated,
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            abnormal_inference_params.dust_color,
                            1,
                            lineType=cv2.LINE_AA
                        )
                        
                        if abnormal_inference_params.is_need_show_abnormal_score:
                            cv2.putText(
                                image_with_dust,
                                str(f'{max_val:.3}'),
                                (position_rotated[0]-100, position_rotated[1]),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.5,
                                abnormal_inference_params.dust_color,
                                1,
                                lineType=cv2.LINE_AA
                            )


                    image_with_dust = cv2.drawContours(image_with_dust, rotated_contours, -1, abnormal_inference_params.dust_color, 2, cv2.LINE_AA)
                
        return image_with_heatmap,image_with_dust,self.is_abnormal,original_box

if __name__ == "__main__":
    # Example usage
    detector = AnomalyDetection()
    video_source = camera_config_params.camera_source if camera_config_params.camera_source else 0
    # detector.test_dust_detect_on_image(video_source)

            




            