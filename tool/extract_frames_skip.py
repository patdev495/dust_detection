import cv2
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.abnormal_processing import Image_Processing

def extract_frames(video_path, output_dir, skip_frame=22, prefix=""):
    """
    Trích xuất frame từ video và lưu vào thư mục output_dir.

    Args:
        video_path (str): Đường dẫn video.
        output_dir (str): Thư mục để lưu frame.
        skip_frame (int): Số frame bỏ qua.
        prefix (str): Tiền tố để phân biệt frame từ các video khác nhau.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    frame_idx = 0
    saved_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % (skip_frame + 1) == 0:
            filename = f"{prefix}_frame_{saved_idx:05d}.jpg"
            filepath = os.path.join(output_dir, filename)
            cv2.imwrite(filepath, frame)
            saved_idx += 1

        frame_idx += 1

    cap.release()
    print(f"✅ Đã trích xuất {saved_idx} frame từ {os.path.basename(video_path)}")

def process_videos_in_directory(input_dir, output_dir, skip_frame=30, video_extensions=None):
    """
    Duyệt các video trong thư mục input_dir và trích xuất frame vào output_dir.

    Args:
        input_dir (str): Thư mục chứa video.
        output_dir (str): Thư mục chứa frame đầu ra.
        skip_frame (int): Số frame bỏ qua.
        video_extensions (list): Các đuôi video hợp lệ (mặc định hỗ trợ mp4, avi, mov, mkv).
    """
    if video_extensions is None:
        video_extensions = ['.mp4', '.avi', '.mov', '.mkv']

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        name, ext = os.path.splitext(filename)
        if os.path.isfile(filepath) and ext.lower() in video_extensions:
            print(f"▶️ Đang xử lý video: {filename}")
            prefix = name.replace(" ", "_")  # tránh lỗi tên file
            extract_frames(filepath, output_dir, skip_frame, prefix=prefix)

    print("🎉 Hoàn tất xử lý toàn bộ video.") 
 
def crop_images_in_directory(input_dir, output_dir, processing_fn, image_extensions=None):
    """
    Áp dụng một hàm xử lý lên tất cả ảnh trong thư mục và lưu kết quả.

    Args:
        input_dir (str): Thư mục chứa ảnh gốc.
        output_dir (str): Thư mục lưu ảnh sau xử lý.
        processing_fn (function): Hàm xử lý ảnh, nhận vào ảnh cv2 và trả về ảnh cv2.
        image_extensions (list): Danh sách đuôi file ảnh hợp lệ.
    """
    if image_extensions is None:
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        name, ext = os.path.splitext(filename)
        if os.path.isfile(filepath) and ext.lower() in image_extensions:
            img = cv2.imread(filepath)
            if img is None:
                print(f"⚠️ Không đọc được ảnh: {filename}")
                continue

            processed_img = processing_fn(img)['croped_image']
            if processed_img is not None:     
                output_path = os.path.join(output_dir, filename)
                cv2.imwrite(output_path, processed_img)
                print(f"✅ Đã xử lý: {filename}")

    print("🎉 Hoàn tất xử lý tất cả ảnh.") 
 
    
if __name__ == '__main__':
    # process_videos_in_directory(r"D:\Tu\Old\AI\data\Data_check_bui\DATA_19.05\Videos\OK_Videos_Removed_Dust",r"D:\Tu\Old\AI\data\Data_check_bui\DATA_19.05\Frame_30.05\OK")
    image_process = Image_Processing()
    processing_fn = image_process.detect_lcd
    crop_images_in_directory(r"D:\Tu\Old\AI\data\Data_check_bui\DATA_19.05\Frame_30.05\OK",r"D:\Tu\Old\AI\data\Data_check_bui\DATA_19.05\Train\MY_Crop_30.05\OK",processing_fn)
    
    