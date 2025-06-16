---
title : "Cấu hình quyền truy cập"
date : "2025-05-28"
weight : 3
chapter : false
pre : " <b> 3.3. </b> "
---

### Bước 3: Cấu hình quyền truy cập

Để cho phép quyền đọc/ghi cho mục đích demo, ta sẽ thêm một **bucket policy** cấp quyền cho một người dùng IAM cụ thể.

> **Lưu ý**: Chính sách này cấp quyền truy cập tương đối mở để phục vụ demo. Trong môi trường thực tế, bạn nên sử dụng IAM role với quyền hạn chế và chỉ cho truy cập riêng tư.

#### Hướng dẫn:

**Bước 1:**  
- Truy cập vào bucket của bạn trong **S3 Console**.
- Chuyển đến tab **Permissions**.

**Bước 2:**  
- Trong phần **Bucket policy**, nhấn **Edit**.

**Bước 3:**  
- Dán đoạn JSON sau vào trình soạn thảo:
- Nhớ thay bằng thông tin ngươi dùng đã tạo trước đó 
```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Principal": {
				"AWS": "arn:aws:iam::612674025610:user/laptrinh"
			},
			"Action": [
				"s3:PutObject",
				"s3:GetObject",
				"s3:DeleteObject"
			],
			"Resource": "arn:aws:s3:::imagetovideoweb-demo-20250608/*"
		},
		{
			"Effect": "Allow",
			"Principal": {
				"AWS": "arn:aws:iam::612674025610:user/laptrinh"
			},
			"Action": "s3:ListBucket",
			"Resource": "arn:aws:s3:::imagetovideoweb-demo-20250608"
		},
		{
			"Effect": "Allow",
			"Principal": "*",
			"Action": "s3:GetObject",
			"Resource": "arn:aws:s3:::imagetovideoweb-demo-20250608/*"
		}
	]
}
