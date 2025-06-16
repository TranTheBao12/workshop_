---
title : "Giới thiệu"
date :  "2025-05-28"
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

### Giới thiệu (45 phút)

- **Mục tiêu**: Giới thiệu dự án và dịch vụ AWS.

- **Nội dung**:

  - **Dự án ImageToVideoWeb**:  
    - Ứng dụng web ASP.NET Core cho phép tải ảnh, trích xuất văn bản (OCR), dịch văn bản (Google Translate), tạo âm thanh (Google TTS), và tạo video (FFmpeg).  
    - Sử dụng Amazon S3 để lưu trữ tệp để triển khai.

  - **Amazon S3**:  
    - Lưu trữ ảnh đầu vào trong thư mục `uploads/`.  
    - Lưu trữ văn bản và âm thanh tạm thời trong thư mục `temp/`.  
    - Lưu trữ video đầu ra trong thư mục `outputs/`.

  - **Kiến trúc hoạt động**:  
    - Giao diện frontend gọi controller → Tải ảnh lên S3 → Xử lý cục bộ (OCR, dịch, TTS, tạo video) → Lưu video lên S3 → Hiển thị video từ S3.

  - **Chụp ảnh**:  
    - Slide trình bày kiến trúc (vẽ trên PowerPoint hoặc bảng trắng).
