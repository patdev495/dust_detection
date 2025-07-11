from PySide6.QtWidgets import QApplication
from controllers.main_window_controller_test import MainWindowController
# from src.modules.AnomalyDetection import AnomalyDetection
# from src.global_params import system_config_params,camera_config_params
# import logging


if __name__ == '__main__':
    
    # detector = AnomalyDetection()
    # video_source = camera_config_params.camera_source if camera_config_params.camera_source else 0
    # detector.test_detect_ccd(video_source)
    # detector.test_dust_detect_on_image(video_source)
    
    app = QApplication([])
    window = MainWindowController()
    window.show()
    app.exec()
    
    # abnomal_processing = Abnormal_Processing()
    # abnomal_processing.train()


    


    