---
title : "Preparation"
date : "2025-05-28"
weight : 2
chapter : false
pre : " <b> 2. </b> "
---

{{% notice info %}}
Before starting the lab, you need to complete the following environment and tool setup steps.
{{% /notice %}}

### Preparation Content:

1. **Install required tools:**  
   - Install **.NET SDK** (ASP.NET Core).  
   - Install **FFmpeg** to generate video files.  
   - Install **Tesseract OCR** to extract text from images.  
   - Install **Google Cloud SDK** if using Google Translate and TTS services.  

2. **Configure AWS CLI:**  
   - Install AWS CLI appropriate for your operating system.  
   - Configure AWS CLI using the command:  
     ```bash
     aws configure
     ```  
     Provide your Access Key, Secret Key, region, and output format when prompted.

3. **Prepare source code:**  
   - Clone or download the **ImageToVideoWeb** project.  
   - Ensure directories such as `uploads/`, `temp/`, and `outputs/` exist or create them manually.  
   - Update `appsettings.json` with your S3 bucket configuration and API keys (Google API Key, AWS settings, etc.).

4. **Test locally:**  
   - Run the application in your local environment:  


### Reference Links:
- [Install .NET SDK](https://learn.microsoft.com/en-us/dotnet/core/install/)  
- [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)  
- [Install Google Cloud SDK](https://cloud.google.com/sdk/docs/install)  
