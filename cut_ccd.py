from src.modules.AnomalyDetection import AnomalyDetection
import cv2
import os
if __name__ == "__main__":
    detect = AnomalyDetection()

    # --- Thư mục nguồn và đích ---
    source_dir = r"D:\Tu\Old\AI\data\Data_check_bui\DATA_19.05\Frame_20.06\NG"     # Thư mục chứa ảnh gốc
    output_dir = r"D:\Tu\Old\AI\data\Data_check_bui\DATA_19.05\Train\My_crop_20.06\NG"    # Thư mục lưu ảnh sau xử lý

    # Tạo thư mục đích nếu chưa có
    os.makedirs(output_dir, exist_ok=True)

    # --- Duyệt qua tất cả file trong thư mục nguồn ---
    for filename in os.listdir(source_dir):
        input_path = os.path.join(source_dir, filename)

        # Kiểm tra có phải ảnh hợp lệ không
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff')):
            continue

        # Đọc ảnh
        image = cv2.imread(input_path)
        if image is None:
            print(f"Lỗi đọc ảnh: {input_path}")
            continue

        # Xử lý ảnh
        processed_image = detect.detect_ccd(image)
        if processed_image is not None:
            cropped = processed_image['cropped_image']

        # Ghi ảnh kết quả vào thư mục đích, giữ tên gốc
        output_path = os.path.join(output_dir, filename)
        if cropped is not None:
            cv2.imwrite(output_path, cropped)

    print("✅ Xử lý xong tất cả ảnh.")