import sys
import os
import platform
import subprocess
import cv2
import numpy as np
from PySide6.QtWidgets import QFileDialog
from src.global_params import detect_lcd_params

#function to get exactly path of assets file in dev environment and exe environment
def get_resource_path(relative_path):
    """Lấy đường dẫn đúng cho file resource"""
    try:
        # PyInstaller tạo temp folder và lưu path trong _MEIPASS
        base_path = sys._MEIPASS # type: ignore
    except Exception:
        # Khi chạy script thông thường
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.call(["open", path])
    else:  # Linux
        subprocess.call(["xdg-open", path])

def open_image():
    # Mở hộp thoại chọn file ảnh
    file_path, _ = QFileDialog.getOpenFileName(None, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
    return file_path


#function to check motion of wipe operation
def quick_stability_check(current_frame, 
                          prev_frame_storage={}, 
                          threshold=detect_lcd_params.motion_score_threshold, 
                          required_stable_frames=detect_lcd_params.required_stable_frames, 
                          resize_shape=detect_lcd_params.resize_shape_caculate_stablity):
        """
        Hàm đơn giản nhất thay thế get_brightness_score
        Sử dụng dictionary để lưu frame trước (tránh global variable)
        
        Usage:
            should_process, score = quick_stability_check(frame)
            if should_process:
                # Xử lý ảnh bản mạch
                process_pcb_image(frame)
        """
        if current_frame is None:
            return False, 0.0
            
        # Resize nhỏ để nhanh
        small = cv2.resize(current_frame, resize_shape)
        gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        
        # Lấy frame trước từ storage
        if 'prev' not in prev_frame_storage:
            prev_frame_storage['prev'] = gray.copy()
            prev_frame_storage['stable_count'] = 0
            return False, 0.0
        
        # So sánh
        diff = cv2.absdiff(gray, prev_frame_storage['prev'])
        motion_score = np.mean(diff)
        
        # Cập nhật
        prev_frame_storage['prev'] = gray.copy()
        
        # Đếm frame ổn định
        if motion_score < threshold:  # Threshold thấp = nhạy cảm hơn
            prev_frame_storage['stable_count'] += 1
        else:
            prev_frame_storage['stable_count'] = 0
            
        # Cần ít nhất 3 frame ổn định
        should_process = prev_frame_storage['stable_count'] >= required_stable_frames
        
        return should_process, round(motion_score, 2)

def calculate_focus_score(image):
    """
    Tính độ nét (focus score) của một ảnh bằng phương pháp Laplacian variance.

    Tham số:
        image (np.ndarray): Ảnh đầu vào, có thể là ảnh màu hoặc ảnh xám.

    Trả về:
        float: Giá trị phương sai của Laplacian (độ nét). Càng cao → ảnh càng nét.
    """
    if image is None or not isinstance(image, np.ndarray):
        raise ValueError("Ảnh đầu vào không hợp lệ.")

    # Chuyển sang ảnh xám nếu ảnh đầu vào là ảnh màu
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    # Tính đạo hàm bậc hai (Laplacian)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    variance = laplacian.var()

    return variance

def draw_focus_score(frame,focus_score):
    focus_score = calculate_focus_score(frame)

    text = f"Focus Score: {int(focus_score)}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2
    color = (0, 255, 0)  # Màu xanh lá

    # Tính kích thước của text để căn giữa
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)
    frame_height, frame_width = frame.shape[:2]

    # Tọa độ để vẽ text ở giữa dưới
    x = (frame_width - text_width) // 2
    y = frame_height - 10  # 10 px cách mép dưới

    # Vẽ nền mờ mờ cho text để dễ nhìn
    cv2.rectangle(frame, (x - 10, y - text_height - 10), (x + text_width + 10, y + 10), (0, 0, 0), -1)

    # Vẽ text
    cv2.putText(frame, text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)

    return frame