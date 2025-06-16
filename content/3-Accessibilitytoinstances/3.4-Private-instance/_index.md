---
title : "Check S3 Upload"
date : "2025-05-28"
weight : 4
chapter : false
pre : " <b> 3.4. </b> "
---

### Step 4: Check S3 Upload

Now that you've created the folders and configured access, it's time to verify that you can upload files to your bucket using the AWS CLI.

#### Instructions:

**Step 1:**  
- Use the following AWS CLI command to upload a file (replace `test.jpg` with your actual file):

```bash
aws s3 cp test.jpg s3://imagetovideoweb-demo-20250608/uploads/
