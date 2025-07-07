import numpy as np
from src.global_params import detect_lcd_params,abnormal_inference_params
import cv2

class ImageProcessor:
    def __init__(self) -> None:
        pass
    def adaptive_image_to_binary(self, img : np.ndarray | None) -> np.ndarray | None:
        """
        Converts a BGR image to a binary image using adaptive thresholding.
            This method first converts the input image to grayscale, applies Gaussian blur to reduce noise,
            and then performs adaptive thresholding to produce a binary image. The parameters for blurring
            and thresholding are taken from the `detect_lcd_params` configuration.
            Args:
                img (np.ndarray): Input image in BGR format.
            Returns:
                np.ndarray: Binary image resulting from adaptive thresholding.
        """   
        if img is None:
            return None
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
    
    def border_gaps_binary_image(self, binary_img : np.ndarray | None) -> np.ndarray | None:
        """
        Repairs border gaps in a binary image by performing morphological closing.
        This method inverts the input binary image, applies morphological closing to connect
        broken borders (gaps) using a rectangular kernel, and then inverts the image back to
        its original polarity. The result is a binary image with repaired border gaps.
        Args:
            binary_img (np.ndarray | None): Input binary image. Should be a single-channel
                image where foreground and background are represented by 0 and 255 values.
                If None, the function returns None.
        Returns:
            np.ndarray | None: The binary image with repaired border gaps, or None if the
                input is None.
        """
        
        # 1. Đảo ảnh: vùng đen thành trắng, vùng trắng thành đen
        if binary_img is None:
            return None
        inverted = cv2.bitwise_not(binary_img)

        # 2. Morph closing để nối vùng trắng (tức là nối lại viền đen trong ảnh gốc)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (detect_lcd_params.kernel_size, detect_lcd_params.kernel_size))
        closed = cv2.morphologyEx(inverted, cv2.MORPH_CLOSE, kernel)

        # 3. Đảo lại ảnh: vùng trắng thành đen, vùng đen thành trắng
        repaired = cv2.bitwise_not(closed)
        
        return repaired
    
    def normalize_rgb_heatmap_by_sum(self, heatmap_rgb:np.ndarray) -> np.ndarray:
        """
        Normalizes an RGB heatmap by summing the values across the color channels for each pixel,
        scaling the result to the range [0, 1], and shifting the minimum value to zero.
        The normalization process is as follows:
            1. Converts the input array to float32 to prevent overflow.
            2. Sums the RGB values at each pixel location.
            3. Divides the sum by the maximum possible sum (255 * 3) to scale to [0, 1].
            4. Shifts the minimum value to zero by subtracting the minimum.
            5. Clips the result to ensure all values are within [0, 1].
        Args:
            heatmap_rgb (np.ndarray): Input RGB heatmap array of shape (H, W, 3) with dtype uint8 or similar.
        Returns:
            np.ndarray: Normalized 2D array of shape (H, W) with values in the range [0, 1].
        """
        
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
    
    def normalize_heatmap_to_binary(self, heat_map:np.ndarray) -> np.ndarray:
        """
        Converts a heatmap to a binary map based on a threshold.
        This method creates a binary map from the input heatmap, where all values greater than or equal to
        `abnormal_inference_params.heat_map_NG_thresh_hold` are set to 255 (indicating abnormal regions),
        and all other values are set to 0.
        Args:
            heat_map (np.ndarray): The input heatmap as a NumPy array.
        Returns:
            np.ndarray: A binary map of the same shape as `heat_map`, with values 0 or 255.
        """
        
        binary_map = np.zeros_like(heat_map, dtype=np.uint8)
        binary_map[heat_map >= abnormal_inference_params.heat_map_NG_thresh_hold] = 255
        return binary_map
    
    def get_top_left_point_box(self, box : np.ndarray):
        """
        Finds and returns the top-left point of a bounding box.
        Given a 2D array representing the coordinates of the corners of a box,
        this function identifies the point with the smallest sum of x and y coordinates,
        which corresponds to the top-left corner.
        Args:
            box (np.ndarray): A (4, 2) array of box corner coordinates.
        Returns:
            tuple: The (x, y) coordinates of the top-left point as integers.
        """
        
        box = np.array(box, dtype="float32")

        # Tính tổng x + y => top-left sẽ có tổng nhỏ nhất
        s = box.sum(axis=1)
        top_left = box[np.argmin(s)]

        return tuple(map(int, top_left))