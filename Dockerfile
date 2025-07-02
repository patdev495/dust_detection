# Chọn đúng phiên bản Python bạn đang dùng (3.12.8)
FROM python:3.12.8-slim

# Tạo thư mục làm việc trong container
WORKDIR /app

# Copy requirements trước để tận dụng cache nếu không đổi
COPY app.py .
COPY requirements.txt .
COPY src/ src/

# Cài các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt
# Lệnh mặc định khi chạy container
CMD ["python", "app.py"]