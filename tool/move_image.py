import os
import shutil

# di chuyen tat ca anh trong thw muc con cua mot thu muc sang mot thu muc khac
# Đường dẫn thư mục cha chứa các thư mục con
thu_muc_cha = r"D:\Tu\Old\AI\data\Data_check_bui\DATA_05.05\Crop_LCD\Crop_LCD_09.05\skip120\NG"
# Đường dẫn thư mục đích để gom tất cả ảnh
thu_muc_dich = r"D:\Tu\Old\AI\data\Data_check_bui\DATA_05.05\Train\Train_09.05\NG"

# Các phần mở rộng tệp được xem là ảnh
dinh_dang_anh = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp'}

# Tạo thư mục đích nếu chưa tồn tại
os.makedirs(thu_muc_dich, exist_ok=True)

# Duyệt qua toàn bộ cây thư mục con
for root, dirs, files in os.walk(thu_muc_cha):
    for file in files:
        # Kiểm tra định dạng ảnh
        if os.path.splitext(file)[1].lower() in dinh_dang_anh:
            duong_dan_anh = os.path.join(root, file)
            ten_anh = os.path.basename(file)
            # Đảm bảo không ghi đè nếu có trùng tên
            ten_anh_moi = ten_anh
            count = 1
            while os.path.exists(os.path.join(thu_muc_dich, ten_anh_moi)):
                ten_anh_moi = f"{os.path.splitext(ten_anh)[0]}_{count}{os.path.splitext(ten_anh)[1]}"
                count += 1

            shutil.copy2(duong_dan_anh, os.path.join(thu_muc_dich, ten_anh_moi))

print("Đã sao chép xong tất cả ảnh.")
