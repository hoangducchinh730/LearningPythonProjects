# ⏰ ClockApp — Mini đồng hồ học lập trình Python

Đây là ứng dụng đồng hồ mini được viết bằng Python — mô phỏng chức năng như ứng dụng "Clock" trong laptop hoặc điện thoại. Mục tiêu chính là giúp người học hiểu cách **xử lý thời gian**, **tạo GUI**, và **tổ chức mã nguồn chuyên nghiệp**.

## 🌟 Tính năng

- ⏱️ **Stopwatch**: bấm giờ, hiển thị giờ/phút/giây với nút Start/Pause/Reset.
- ⏰ **Timer**: hẹn giờ đếm ngược và cảnh báo khi hết thời gian.
- 🌍 **World Clock**: hiển thị giờ tại nhiều quốc gia dựa trên múi giờ thực tế.
- 🧩 Cấu trúc mã chia theo `logic/`, `gui/` và `assets/` để dễ mở rộng.

## 📚 Bạn sẽ học được

- Sử dụng thư viện `datetime`, `time`, `pytz` để xử lý thời gian chuyên sâu.
- Tạo giao diện bằng `tkinter` hoặc `customtkinter`.
- Tổ chức project chuyên nghiệp: chia folder, viết module riêng.
- Tích hợp âm thanh, icon, và cấu hình `.gitignore`, `README`, `requirements.txt`.
- Đẩy code lên GitHub đúng chuẩn cộng đồng lập trình.

## 🏗️ Đang phát triển...

Dự kiến sẽ bổ sung:
- 🔔 Chức năng báo thức hằng ngày
- 📅 Trình nhắc sự kiện cá nhân
- 📈 Lịch sử bấm giờ, lưu thời gian vào file
- ⏳ Đồng hồ analog tự vẽ bằng `Canvas`

## 📦 Cài đặt (tùy chọn)

```bash
pip install pytz customtkinter playsound
