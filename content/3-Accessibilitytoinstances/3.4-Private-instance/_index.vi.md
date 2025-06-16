---
title : "Kiểm tra S3"
date : "2025-05-28"
weight : 4
chapter : false
pre : " <b> 3.4. </b> "
---

### Bước 4: Kiểm tra S3

Sau khi đã tạo thư mục và cấu hình quyền truy cập, giờ là lúc kiểm tra việc tải file lên bucket bằng AWS CLI.

#### Hướng dẫn:

**Bước 1:**  
- Chạy lệnh sau trong Terminal (thay `test.jpg` bằng tên file bạn muốn tải):
- Kiểm tra trong S3 Console, thư mục uploads/ có test.jpg.    
```bash
aws s3 cp test.jpg s3://imagetovideoweb-demo-20250608/uploads/
