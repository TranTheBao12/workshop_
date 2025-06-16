---
title : "Kiểm tra chức năng tải ảnh"
date : "2025-05-28"
weight : 1
chapter : false
pre : " <b> 4.1 </b> "
---

### Bước 1: Tải ảnh lên

Để xác nhận rằng chức năng tải ảnh hoạt động đúng, thực hiện theo các bước sau:

---

#### Các bước thực hiện:

1. **Chạy ứng dụng:**
   - Khởi chạy server backend hoặc ứng dụng frontend có xử lý chức năng tải ảnh.

2. **Tải ảnh thử nghiệm:**
   - Sử dụng giao diện web để tải một ảnh thử.
   - Ví dụ: ảnh có chứa văn bản tiếng Việt để kiểm tra khả năng xử lý ngôn ngữ.

3. **Kiểm tra S3 Bucket:**
   - Mở giao diện AWS S3 Console.
   - Truy cập vào bucket của bạn.
   - Kiểm tra ảnh có xuất hiện trong thư mục `uploads/`.

---

#### Yêu cầu chụp ảnh minh họa:


![Ảnh chụp giao diệnAWS S3 Console hiển thị ảnh đã được tải lên trong thư mục `uploads/`](/images/2.prerequisite/anh11.png)

---

{{% notice tip %}}
Đảm bảo rằng ứng dụng của bạn có quyền tải ảnh lên S3. Nếu xảy ra lỗi, hãy kiểm tra lại IAM Role và bucket policy.
{{% /notice %}}
