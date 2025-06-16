---
title : "Xử lý và xem kết quả"
date : "2025-05-28"
weight : 2
chapter : false
pre : " <b> 4.2 </b> "
---

### Bước 2: Xử lý và xem kết quả

Sau khi tải ảnh lên thành công, bạn sẽ tiến hành xử lý ảnh để tạo video và kiểm tra kết quả.

---

#### Các bước thực hiện:

1. **Kiểm tra giao diện "EditTextList":**
   - Giao diện này hiển thị kết quả OCR từ ảnh đã tải.
   - Ngoài văn bản gốc, giao diện cũng hiển thị phần văn bản đã được dịch sang tiếng Việt hoặc ngôn ngữ khác.

2. **Tạo video từ văn bản:**
   - Nhấn nút **"Create Video"**.
   - Hệ thống sẽ xử lý và lưu video đầu ra vào thư mục `outputs/` trong S3 bucket.

3. **Xem video:**
   - Truy cập giao diện **"Result"** để xem video được tạo ra từ ảnh gốc.

---



---

{{% notice tip %}}
Nếu không thấy video trong giao diện "Result", hãy kiểm tra lại log hệ thống hoặc trạng thái xử lý. Video được lưu tại `S3 > outputs/` nếu thành công.
{{% /notice %}}
