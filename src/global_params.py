
# from pBaseParams import BaseParams
from sparams import BaseParams
from enum import Enum
from typing import Union,Literal

APP_NAME = "Dust_Checking" 

class ProcessType(Enum):
    CAMERA = "camera"
    VIDEO = "video"
    IMAGE = "image"

class System_Config_Params(BaseParams):
    def __init__(self,app_name,module_name):
        super().__init__(app_name, module_name)
        self.log_dir : str = 'logs'
        self.debug : bool = False
        self.process_type = ProcessType.CAMERA.value
        self.is_auto_process : bool = True
        self.config_file_path : str = f"{APP_NAME}.yaml"
        
        self.normal_status_label_style : str = "border: 1px solid #ccc; border-radius: 3px;  "
        self.normal_status_label_text : str = "STATUS:..."
        self.ok_status_label_style : str = "border: 1px solid #ccc; border-radius: 3px; background-color: green;  color:white"
        self.ok_status_label_text : str = "OK"
        self.ng_status_label_style : str = "border: 1px solid #ccc; border-radius: 3px; background-color: red; font-weight: bold;color:white"
        self.ng_status_label_text : str = "NG"
        self.time_to_focus_mac_input : int = 500
        self.show_image_focus_score : bool = True
        self.skip_frames_show_focus : int = 8
        self.create_or_load_yaml()
        
class Camera_Config_Params(BaseParams):
    def __init__(self,app_name : str,module_name : str):
        super().__init__(app_name, module_name)
        self.instructions = [
            'camera reoslution: [1080,1920] - fullHD or [2160,3840] - 4k',
            'auto_exposure: 0.25 - manual or 0.75 - auto',
            'prop_exposure: the closer the value is to 0, the brighter it is',
            "cap_type_dshow: true - live camera or false - video test ",
            "zoom_in_factor: zoom ratio"
        ]
        self.camera_source : Union[str,int]  = 0
        self.camera_resolution : Union[list[int],tuple[int,int]] = [1080,1920]
        self.enable_mjpg_format : bool = False
        
        self.is_need_resize_frame : bool = False
        self.resize_resolution : Union[list[int],tuple[int,int]] = [1620,2880]
        self.auto_exposure : float = 0.25 #=.75
        self.prop_exposure : int = -5
        self.sensor_size : Union[list[float],tuple[float,float]]  = [6.4 , 4.8]

        self.is_need_rotate_camera : bool = False
        self.rotate_angle : float = 180

        self.manual_setting : bool = True
        self.brightness : int = 65
        self.contrast : int = 60
        self.saturation : int = 40
        self.sharpness : int = 90
        self.gain : int = 0
        self.cap_type_dshow : bool = True
        # self.auto_focus = 0
        self.zoom_in_factor : float = 1.05
        self.create_or_load_yaml()
        
class Product_Config_Params(BaseParams):
    def __init__(self,app_name,module_name):
        super().__init__(app_name, module_name)
        self.debug : bool = False
        self.mac_min_len : int = 16
        self.mac_start_with : str = "PT5"
        self.tray_min_len : int = 16

        self.sum_ok_products : int = 0
        self.sum_ng_products : int = 0
        self.create_or_load_yaml()        
        
class Detect_LCD_Params(BaseParams):
    def __init__(self,app_name,module_name):
        super().__init__(app_name, module_name)
        
        # tham so cho adaptive threshold cv2.adaptiveThreshold()
        self.C : int = 2
        self.block_size : int = 11 #là số lẻ

        self.kernel_blur_size : list[int] = [5,5]
        
        # tham so noi cac vung t
        self.kernel_size : int = 7
        self.expand_crop_bot : int = 0
        self.expand_crop_left : int = 0
        self.expand_crop_right : int = 0
        self.expand_crop_top : int = 3
        
        
        self.min_LCD_area_ratio : float = 0.35
        self.max_LCD_area_ratio : float = 0.85
        self.max_LCD_w_h_ratio : float = 0.9

        self.is_need_check_stable_frames : bool = True
        self.is_need_scan_sn_first : bool = True

        self.motion_score_threshold : int = 3
        self.required_stable_frames = 4
        self.resize_shape_caculate_stablity : list[int] = [80,60]

        
        self.create_or_load_yaml()
        
class  Abnormal_Train_Params(BaseParams):
    def __init__(self,app_name : str ,module_name : str):
        super().__init__(app_name, module_name)     
        self.abnormal_dir = r'D:\Tu\Old\AI\data\Data_check_bui\DATA_19.05\Train\FAI_crop\NG'
        self.accelerator : Literal['gpu','cpu']  = 'gpu'
        self.dataset_name : str = 'check_bui'
        self.image_size : int = 512
        self.model_type : str = 'Padim'
        self.normal_dir : str = r'D:\Tu\Old\AI\data\Data_check_bui\DATA_19.05\Train\FAI_crop\OK'
        self.normal_split_ratio : float = 0.1
        self.post_processing_image_sensitivity : float = 1
        self.post_processing_pixel_sensitivity : float = 1
        self.test_split_ratio : float = 0.1
        self.train_batch_size : int = 2
        self.create_or_load_yaml()
        
class Abnormal_Inference_Params(BaseParams):
    def __init__(self,app_name : str ,module_name : str):
        super().__init__(app_name, module_name)
        self.model_path : str = r"models\openvino_512_20.05_My_Crop\model.xml"
        self.inference_type : str = 'Openvino' 
        self.heat_map_NG_thresh_hold : float = 0.14 # < 1
        self.heat_map_display_alpha : float = 0.7 # < 1
        self.max_ratio_w_h_cnt : float = 3
        self.brightness_threshold_caculate_dust_size : float = 0.9 # < 1
        self.ng_color : list[int] = [0,0,255]
        self.ok_color : list[int] = [0,255,0]
        self.dust_color : list[int] = [255,0,0]
        self.frame_count_threashold_ok : int = 8
        self.is_need_show_abnormal_score : bool = True

        self.src_video : int | str = r"D:\Tu\Old\AI\data\Data_check_bui\DATA_16.01\OK\1 hat bui to.mp4"
        self.create_or_load_yaml()
   
class Request_SFC_Params(BaseParams):
    def __init__(self,app_name : str,module_name : str):
        super().__init__(app_name, module_name)
        # self.Ready_to_run = False # Nếu bắt buộc phải config thì đặt cái này = False, khi nào user chỉnh sang True thì mới cho chạy
        # self.end_point = "http://10.72.76.65:8088/api/smo/HandleData" #http://127.0.0.1:8000
        self.instruction : list[str] = ['http://10.72.76.65:8088/api/smo/HandleData','http://127.0.0.1:8000/api/echo']
        self.end_point : str = "http://10.72.76.65:8088/api/smo/HandleData"
        self.method : Literal['POST',"GET","PUT"] = "POST"
        self.headers : dict = {"Content-Type": "application/json"}
        self.LINE_NAME : str = "B084FSF"
        self.GROUP_NAME : str = "VI"
        self.SP : str = "811,811"
        self.SN : str = "PT53SH0452060KV6"
        self.TRAY : str = "YO250414AA22LA09"
        self.EMP : str = "CYCLOPS01"
        self.PASSED : Literal[0,1] = 1
        
        self.sfc_response_key1 : str = "Data"
        self.sfc_response_key2 : str = "RES"
        self.sfc_response_key3 : str = "COMMAND1"
        self.Data_send_to_SFC : dict = {
            "LINE_NAME":"B084FSF",
            "GROUP_NAME":"VI",
            "SP":"811,811",
            "DATA":""
        }
        # self.is_need_scan_sn_first = True
        self.scan_sn_first_message : str = "Please scan SN"
        self.SFC_Response_status : str = "OK"
        
        self.notify_text_valid_sn : str = "SN - OK"
        self.notify_text_valid_tray : str = "TRAY - OK"

        self.notify_text_invalid_sn : str = "SN - Failed"
        self.notify_text_passed_product : str = "SFC - PASS"
        self.notify_text_still_dusty : str = "Dusting"
        self.notify_text_sfc_failed_request : str = "SFC - Fail"
        
        self.font_scale_log_image : float = 1.0
        self.color_text_log_image : list[int] = [0, 0, 200]
        self.thickness_text_log_image : int = 2
        self.default_dir_log_image : str = './saved_images'
        self.default_dir_log_sn_pass : str = r"logs\pass_sn"
            
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

