---
title : "Thêm vie.traineddata vào tessdata"
date : "2025-05-28"
weight : 3
chapter : false
pre : " <b> 2.1.3 </b> "
---

#### Thêm `vie.traineddata` vào Thư mục `tessdata`

Trong bước này, chúng ta sẽ tải xuống và thêm tệp dữ liệu tiếng Việt `vie.traineddata` vào thư mục `tessdata` trong dự án của bạn. Điều này là bắt buộc nếu bạn dự định sử dụng Tesseract OCR để nhận dạng văn bản tiếng Việt.

---

### 1. Tải xuống `vie.traineddata`

Truy cập kho lưu trữ GitHub chính thức của dữ liệu ngôn ngữ Tesseract OCR:

- [https://github.com/tesseract-ocr/tessdata](https://github.com/tesseract-ocr/tessdata)

Xác định vị trí tệp `vie.traineddata` và nhấp vào **Tải xuống**.

Ngoài ra, hãy sử dụng liên kết trực tiếp này để tải xuống:
[Tải xuống vie.traineddata](https://github.com/tesseract-ocr/tessdata/raw/main/vie.traineddata)

---

### 2. Tạo thư mục `tessdata` trong dự án của bạn

1. Trong Visual Studio, nhấp chuột phải vào thư mục gốc của dự án.
2. Chọn **Thêm → Thư mục mới** và đặt tên là `tessdata`.
3. Nhấp chuột phải vào `tessdata` → **Thêm → Mục hiện có**.
4. Chọn tệp `vie.traineddata` đã tải xuống và nhấp vào **Thêm**.

> 📌 Đảm bảo thuộc tính `Sao chép vào thư mục đầu ra` của `vie.traineddata` được đặt thành **Sao chép nếu mới hơn** hoặc **Luôn sao chép**.

---

### 3. Xác minh cấu trúc thư mục

Thư mục dự án của bạn bây giờ sẽ trông như sau:
![AWS Explorer](/images/2.prerequisite/anh5.png)