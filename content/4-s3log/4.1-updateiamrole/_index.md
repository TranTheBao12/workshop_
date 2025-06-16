---
title : "Image Upload Test"
date : "2025-05-28"
weight : 1
chapter : false
pre : " <b> 4.1 </b> "
---

### Step 1: Upload an Image

To verify that the image upload functionality is working correctly, follow the steps below:

---

#### Instructions:

1. **Run the Application:**
   - Start your backend server or frontend application that handles image uploads.

2. **Upload a Test Image:**
   - Use the web interface to upload a sample image.
   - For example: an image containing Vietnamese text to verify multilingual support.

3. **Check the S3 Bucket:**
   - Open the AWS S3 Console.
   - Navigate to your bucket.
   - Verify that the image appears inside the `uploads/` folder.

---

#### Screenshot Requirements:
- A screenshot of the web interface with the image upload form.
- A screenshot of the S3 Console showing the uploaded image inside the `uploads/` folder.
![Ảnh chụp giao diệnAWS S3 Console hiển thị ảnh đã được tải lên trong thư mục `uploads/`](/images/2.prerequisite/anh11.png)

---

{{% notice tip %}}
Make sure the application has permission to upload to S3. If you encounter errors, check the IAM Role and bucket policy settings.
{{% /notice %}}
