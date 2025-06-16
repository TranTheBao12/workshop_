---
title : "Chuẩn bị mã nguồn"
date : "2025-05-28"
weight : 3
chapter : false
pre : " <b> 2.3 </b> "
---

{{% notice info %}}
Trước khi bắt đầu lab, bạn cần hoàn tất các bước thiết lập môi trường và công cụ dưới đây.
{{% /notice %}}

### Nội dung chuẩn bị:

1. **Clone mã nguồn hoặc tải file ZIP:**
   - Clone từ GitHub hoặc tải file nén (ZIP) của dự án **ImageToVideoWeb**.
   - Giải nén và mở trong IDE (Visual Studio, VS Code, Rider...).
link: https://github.com/TranTheBao12/Workshop1_AWS.git
2. **Cập nhật file `appsettings.json`:**

```json
{
  "Gemini": {
    "ApiKey": "AIzaSyDJfsJxA67gB7IHc-lCedeX26I6YXcuJkA"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  "GeminiApiKey": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
  "AWS": {
    "Region": "us-east-1",
    "S3_BUCKET_NAME": "imagetovideoweb-demo-20250608",
    "AccessKeyId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "SecretAccessKey": "xxxxxxxxxxxxxxxxxx"
  }
}
