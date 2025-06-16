---
title: "Tạo Key Pair"
date: "2025-05-28"
weight: 3
chapter: false
pre: " <b> 5.1.3 </b> "
---

### 5.1.3. Tạo Key Pair

Key pair là cần thiết để bạn có thể kết nối SSH (hoặc RDP cho Windows) vào các instance EC2 trong môi trường Elastic Beanstalk của mình, phục vụ cho việc kiểm tra hoặc gỡ lỗi.

#### Các bước:

1.  **Đăng nhập vào AWS Management Console** và điều hướng đến dịch vụ **EC2 (Elastic Compute Cloud)**.
2.  Trong thanh điều hướng bên trái, dưới mục **Network & Security**, chọn **Key Pairs**.
![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh14.png)
3.  Nhấp vào nút **Create key pair**.
![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh15.png)
4.  Đặt tên cho Key pair (ví dụ: `ImageToVideoWeb-KeyPair`).
5.  Chọn **Key pair type** là **RSA** và **Private key format** là **.pem** (cho Linux SSH client) hoặc **.ppk** (nếu bạn dùng PuTTY trên Windows). Đối với môi trường Windows, .pem cũng hoạt động với các công cụ SSH tích hợp hoặc bạn có thể chuyển đổi sang .ppk sau này. Hãy chọn **.pem** để phổ biến.
6.  Nhấp **Create key pair**. Tệp khóa riêng tư (**.pem** hoặc **.ppk**) sẽ được tự động tải về trình duyệt của bạn. **Lưu trữ tệp này ở nơi an toàn và không chia sẻ nó.**
![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh16.png)