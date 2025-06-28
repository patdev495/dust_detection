
# from pBaseParams import BaseParams
from sparams import BaseParams
from enum import Enum


APP_NAME = "Dust_Checking" 


class ProcessType(Enum):
    CAMERA = "camera"
    VIDEO = "video"
    IMAGE = "image"

class System_Config_Params(BaseParams):
    def __init__(self,app_name,module_name):
        super().__init__(app_name, module_name)
        self.log_dir = 'logs'
        self.debug = False
        self.process_type = ProcessType.CAMERA.value
        self.is_auto_process = True
        self.config_file_path = f"{APP_NAME}.yaml"
        
        self.normal_status_label_style = "border: 1px solid #ccc; border-radius: 3px;  "
        self.normal_status_label_text = "STATUS:..."
        self.ok_status_label_style = "border: 1px solid #ccc; border-radius: 3px; background-color: green;  color:white"
        self.ok_status_label_text = "OK"
        self.ng_status_label_style = "border: 1px solid #ccc; border-radius: 3px; background-color: red; font-weight: bold;color:white"
        self.ng_status_label_text = "NG"
        self.time_to_focus_mac_input = 500
        self.show_image_focus_score = True
        self.skip_frames_show_focus = 8
        self.create_or_load_yaml()
        
class Camera_Config_Params(BaseParams):
    def __init__(self,app_name,module_name):
        super().__init__(app_name, module_name)
        self.camera_source = 0
        self.camera_resolution = [2160,3840]
        self.enable_mjpg_format = False
        
        self.is_need_resize_frame = True
        self.resize_resolution = [1620,2880]
        self.auto_exposure = 0.25 #=.75
        self.prop_exposure = -5
        self.sensor_size = [6.4 , 4.8]

        self.is_need_rotate_camera = False
        self.rotate_angle = 180

        self.manual_setting = True
        self.brightness = 65
        self.contrast = 45
        self.saturation = 60
        self.sharpness = 65
        self.cap_type_dshow = False
        # self.auto_focus = 0
        self.zoom_in_factor = 1.05
        self.create_or_load_yaml()
        
class Product_Config_Params(BaseParams):
    def __init__(self,app_name,module_name):
        super().__init__(app_name, module_name)
        self.debug = False
        self.mac_min_len = 16
        self.mac_start_with = "PT5"
        self.tray_min_len = 16

        self.sum_ok_products = 0
        self.sum_ng_products = 0
        self.create_or_load_yaml()        
        
class Detect_LCD_Params(BaseParams):
    def __init__(self,app_name,module_name):
        super().__init__(app_name, module_name)
        
        # tham so cho adaptive threshold cv2.adaptiveThreshold()
        self.C = 2
        self.block_size = 11

        self.kernel_blur_size = [5,5]
        
        # tham so noi cac vung t
        self.kernel_size = 7
        self.expand_crop_bot = 0
        self.expand_crop_left = 0
        self.expand_crop_right = 0
        self.expand_crop_top = 3
        
        
        self.min_LCD_area_ratio = 0.4
        self.max_LCD_area_ratio = 0.8
        self.max_LCD_w_h_ratio = 0.9

        self.is_need_check_stable_frames = True
        self.is_need_scan_sn_first = True

        self.motion_score_threshold = 3
        self.required_stable_frames = 3
        self.resize_shape_caculate_stablity = [80,60]

        
        self.create_or_load_yaml()
        
class  Abnormal_Train_Params(BaseParams):
    def __init__(self,app_name,module_name):
        super().__init__(app_name, module_name)     
        self.abnormal_dir = r'D:\Tu\Old\AI\data\Data_check_bui\DATA_19.05\Train\FAI_crop\NG'
        self.accelerator = 'gpu'
        self.dataset_name = 'check_bui'
        self.image_size = 512
        self.model_type = 'Padim'
        self.normal_dir = r'D:\Tu\Old\AI\data\Data_check_bui\DATA_19.05\Train\FAI_crop\OK'
        self.normal_split_ratio = 0.1
        self.post_processing_image_sensitivity = 1
        self.post_processing_pixel_sensitivity = 1
        self.test_split_ratio = 0.1
        self.train_batch_size = 2
        self.create_or_load_yaml()
        
class Abnormal_Inference_Params(BaseParams):
    def __init__(self,app_name,module_name):
        super().__init__(app_name, module_name)
        self.model_path = r"models\openvino_512_20.05_My_Crop\model.xml"
        self.inference_type = 'Openvino' 
        self.heat_map_NG_thresh_hold = 0.14
        self.heat_map_display_alpha = 0.5
        self.max_ratio_w_h_cnt = 3
        self.brightness_threshold_caculate_dust_size = 0.9
        self.ng_color = [0,0,255]
        self.ok_color = [0,255,0]
        self.dust_color = [255,0,0]
        self.frame_count_threashold_ok = 6
        self.is_need_show_abnormal_score = True

        self.src_video = r"D:\Tu\Old\AI\data\Data_check_bui\DATA_16.01\OK\1 hat bui to.mp4"
        self.create_or_load_yaml()
   
class Request_SFC_Params(BaseParams):
    def __init__(self,app_name,module_name):
        super().__init__(app_name, module_name)
        # self.Ready_to_run = False # Nếu bắt buộc phải config thì đặt cái này = False, khi nào user chỉnh sang True thì mới cho chạy
        # self.end_point = "http://10.72.76.65:8088/api/smo/HandleData" #http://127.0.0.1:8000
        self.instruction = ['http://10.72.76.65:8088/api/smo/HandleData','http://127.0.0.1:8000/api/echo']
        self.end_point = "http://10.72.76.65:8088/api/smo/HandleData"
        self.method = "POST"
        self.headers = {"Content-Type": "application/json"}
        self.LINE_NAME = "B084FSF"
        self.GROUP_NAME = "VI"
        self.SP = "811,811"
        self.SN = "PT53SH0452060KV6"
        self.TRAY = "YO250414AA22LA09"
        self.EMP = "CYCLOPS01"
        self.PASSED = 1
        
        self.sfc_response_key1 = "Data"
        self.sfc_response_key2 = "RES"
        self.sfc_response_key3 = "COMMAND1"
        self.Data_send_to_SFC = {
            "LINE_NAME":"B084FSF",
            "GROUP_NAME":"VI",
            "SP":"811,811",
            "DATA":""
        }
        # self.is_need_scan_sn_first = True
        self.scan_sn_first_message = "Please scan SN"
        self.SFC_Response_status = "OK"
        
        self.notify_text_valid_sn = "SN - OK"
        self.notify_text_valid_tray = "TRAY - OK"

        self.notify_text_invalid_sn = "SN - Failed"
        self.notify_text_passed_product = "SFC - PASS"
        self.notify_text_still_dusty = "Dusting"
        self.notify_text_sfc_failed_request = "SFC - Fail"
        
        self.font_scale_log_image = 1.0
        self.color_text_log_image = [0, 0, 200]
        self.thickness_text_log_image = 2
        self.default_dir_log_image = './saved_images'
        self.default_dir_log_sn_pass = r"logs\pass_sn"
            
        self.create_or_load_yaml()   
    
detect_lcd_params = Detect_LCD_Params(app_name=APP_NAME,module_name='Detect_LCD')
abnormal_train_params = Abnormal_Train_Params(app_name=APP_NAME,module_name='Abnormal_Train')
abnormal_inference_params = Abnormal_Inference_Params(app_name=APP_NAME,module_name='Abnormal_Inference')
camera_config_params = Camera_Config_Params(app_name=APP_NAME,module_name='Camera_Config')
system_config_params = System_Config_Params(app_name=APP_NAME,module_name='System_Config')
product_config_params = Product_Config_Params(APP_NAME,'Product_Config')
sfc_request_params = Request_SFC_Params(APP_NAME,'SFC_Config')

def save_all_config():
    detect_lcd_params.save_to_config_file()
    abnormal_train_params.save_to_config_file()
    abnormal_inference_params.save_to_config_file()
    camera_config_params.save_to_config_file()
    system_config_params.save_to_config_file()
    product_config_params.save_to_config_file()
    sfc_request_params.save_to_config_file()

