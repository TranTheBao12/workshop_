---
title : "Preparation"
date : "2025-05-28"
weight : 2
chapter : false
pre : " <b> 2.3 </b> "
---

{{% notice info %}}
Before starting the lab, make sure to complete the following environment and tool setup steps.
{{% /notice %}}

### Preparation Steps:

1. **Clone or download the source code:**
   - Clone the **ImageToVideoWeb** project from GitHub or download the ZIP file.
   - Extract the files and open the project in your preferred IDE (Visual Studio, VS Code, etc.).

2. **Update the `appsettings.json` file:**

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
  "GeminiApiKey": "xxxxxxxxxxxxxxxxxxxxx",
  "AWS": {
    "Region": "us-east-1",
    "S3_BUCKET_NAME": "imagetovideoweb-demo-20250608",
    "AccessKeyId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "SecretAccessKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  }
}
 
 Please enter your AccessKeyId and SecretAccessKey