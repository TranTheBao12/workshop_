---
title : "Tạo thư mục trong S3 Bucket"
date : "2025-05-28"
weight : 2
chapter : false
pre : " <b> 3.2. </b> "
---

### Bước 2: Tạo thư mục trong bucket

Sau khi đã tạo bucket, bạn cần tạo các thư mục con để lưu trữ tệp một cách có tổ chức.

#### Thực hiện:

**Bước 1:**
- Truy cập vào bucket vừa tạo.
- Nhấn nút **Create folder**.

**Bước 2:**
- Nhập tên thư mục, ví dụ:
  - `uploads/` (dùng để lưu ảnh đầu vào)
  - `temp/` (dùng để lưu file văn bản và âm thanh tạm)
  - `outputs/` (dùng để lưu video đầu ra)
- Nhấn **Create folder** để tạo từng thư mục.

Sau khi tạo xong, giao diện cây thư mục trong bucket sẽ như sau:


![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh10.png)



{{% notice tip %}}
Các thư mục này không thực sự là thư mục vật lý mà chỉ là key prefix trong S3, nhưng vẫn rất hữu ích để tổ chức nội dung dễ quản lý.
{{% /notice %}}
