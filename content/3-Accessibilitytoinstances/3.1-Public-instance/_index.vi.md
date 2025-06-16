---
title : "Tạo S3 Bucket"
date : "2025-05-28"
weight : 1
chapter : false
pre : " <b> 3.1. </b> "
---

### Bước 1: Tạo một S3 Bucket

1. Truy cập [AWS Management Console](https://console.aws.amazon.com/) và vào dịch vụ **S3**.

2. Nhấn **Create bucket**.
![AWS Explorer](/images/2.prerequisite/anh8.png)
3. Nhập các thông tin sau:
   - **Bucket name**: `imagetovideoweb-demo-<UNIQUE-ID>` (ví dụ: `imagetovideoweb-demo-20250608`)
   - **Region**: `us-east-1` (N. Virginia)

4. Trong phần **Block Public Access**, bỏ chọn **Block all public access** (chỉ áp dụng cho demo, trong thực tế nên sử dụng IAM để kiểm soát truy cập).

5. Nhấn **Create bucket** để hoàn tất.
![AWS Explorer](/images/2.prerequisite/anh9.png)


{{% notice note %}}
Cấu hình này chỉ dùng để trình diễn. Trong môi trường triển khai thực tế, bạn nên kiểm soát quyền truy cập thông qua IAM thay vì cho phép truy cập công khai.
{{% /notice %}}
