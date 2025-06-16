---
title : "Cấu hình AWS CLI"
date : "2025-05-28"
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---

### Cấu hình AWS CLI

Trong bước này, chúng ta sẽ cấu hình AWS Command Line Interface (CLI) để có thể thao tác với các dịch vụ AWS từ dòng lệnh.

---

#### 1. Mở Terminal hoặc Command Prompt

Tùy theo hệ điều hành bạn sử dụng:

- **Windows**: Mở Command Prompt hoặc PowerShell.
- **Linux/macOS**: Mở Terminal.

---

#### 2. Chạy lệnh `aws configure`

Nhập Access Key, Secret Key, region (us-east-1), output (json) sau đó kiểm tra bằng lệnh aws sts get-caller-identity
![AWS Explorer](/images/2.prerequisite/anh6.png)
```bash
aws configure
