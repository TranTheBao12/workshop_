---
title : "Cài đặt AWS Toolkit cho Visual Studio"
date : "2025-05-28"
weight : 2
chapter : false
pre : " <b> 2.1.2 </b> "
---

#### Cài đặt và thiết lập AWS Toolkit cho Visual Studio

1. Mở **Visual Studio 2022**.

2. Trên thanh menu trên cùng, chọn:  
   **Extensions** → **Manage Extensions**.

3. Trong tab **Online**, nhập từ khóa **AWS Toolkit for Visual Studio** để tìm kiếm.

4. Nhấn **Download**, sau đó khởi động lại Visual Studio để hoàn tất quá trình cài đặt.

![Create ASP.NET Project](/images/2.prerequisite/anh3.png)

---

### Thiết lập ban đầu

1. Sau khi khởi động lại Visual Studio, vào:
**Extentions** → **AWS Toolkit for .NET Refactoringr**.

2. Trong khung AWS Toolkit for .NET Refactoringr, nhấn **GET START** để nhập thông tin người dùng.

3. Bạn có thể đăng nhập bằng một trong hai cách sau:

- **Thông tin xác thực IAM (ID khóa truy cập và Khóa truy cập bí mật)** hoặc

- **SSO (Đăng nhập một lần)** nếu tổ chức của bạn sử dụng AWS SSO.

4. Sau khi đăng nhập thành công, bạn sẽ thấy danh sách các dịch vụ và tài nguyên AWS trong tài khoản của mình.

![AWS Explorer](/images/2.prerequisite/anh4.png)

---

### Ghi chú

- Hãy đảm bảo tài khoản IAM của bạn có đầy đủ quyền để thao tác với EC2, Lambda, S3 và các dịch vụ AWS mà bạn sẽ sử dụng trong dự án.
- AWS Toolkit cho phép bạn triển khai ứng dụng ASP.NET Core lên các dịch vụ như Elastic Beanstalk hoặc Lambda trực tiếp từ Visual Studio.

