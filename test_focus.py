import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOCUS, float(200))
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
# Yêu cầu độ phân giải 4K (tuỳ camera có hỗ trợ hay không)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
print("===== Thông tin camera =====")
print(f"Độ phân giải: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)} x {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
print(f"FPS: {cap.get(cv2.CAP_PROP_FPS)}")
print(f"Brightness: {cap.get(cv2.CAP_PROP_BRIGHTNESS)}")
print(f"Contrast: {cap.get(cv2.CAP_PROP_CONTRAST)}")
print(f"Saturation: {cap.get(cv2.CAP_PROP_SATURATION)}")
print(f"Hue: {cap.get(cv2.CAP_PROP_HUE)}")
print(f"Gain: {cap.get(cv2.CAP_PROP_GAIN)}")
print(f"Exposure: {cap.get(cv2.CAP_PROP_EXPOSURE)}")
print(f"AutoFocus: {cap.get(cv2.CAP_PROP_AUTOFOCUS)}")
print(f"Focus: {cap.get(cv2.CAP_PROP_FOCUS)}")
print("Set to:", 100, "=> Actual:", cap.get(cv2.CAP_PROP_FOCUS))

fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
codec = "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)])
print("Current codec:", codec)
cap.release()





# # Tắt autofocus nếu có thể
# cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

# best_score = -1
# best_focus = -1

# def calculate_focus_score(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     return cv2.Laplacian(gray, cv2.CV_64F).var()

# # Thử quét nhiều mức focus
# for focus in range(0, 256, 5):
#     cap.set(cv2.CAP_PROP_FOCUS, float(focus))
#     time.sleep(0.2)  # đợi camera ổn định

#     ret, frame = cap.read()
#     if not ret:
#         continue

#     score = calculate_focus_score(frame)
#     print(f"Focus: {focus}, Score: {score:.2f}")

#     # Hiển thị khung hình và điểm nét
#     cv2.putText(frame, f"Focus: {focus} Score: {score:.2f}", (10, 30),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     cv2.imshow("Adjusting Focus", frame)

#     key = cv2.waitKey(1)
#     if key == 27:  # nhấn ESC để thoát sớm
#         break

#     if score > best_score:
#         best_score = score
#         best_focus = focus

# # Thiết lập lại tiêu cự tốt nhất
# print(f"Best focus: {best_focus} with score: {best_score:.2f}")
# cap.set(cv2.CAP_PROP_FOCUS, float(best_focus))

# # Hiển thị khung hình cuối với tiêu cự tối ưu
# ret, final_frame = cap.read()
# cv2.putText(final_frame, f"Best Focus: {best_focus}", (10, 30),
#             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
# cv2.imshow("Best Focus", final_frame)
# cv2.waitKey(0)

# # Giải phóng tài nguyên
# cap.release()
# cv2.destroyAllWindows()
