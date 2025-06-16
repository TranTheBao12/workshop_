---
title : "Configure Bucket Access Permissions"
date : "2025-05-28"
weight : 3
chapter : false
pre : " <b> 3.3. </b> "
---

### Step 3: Configure Access Permissions

To allow read/write access for demo purposes, we will add a **bucket policy** that grants permissions to a specific IAM user.

> **Note**: This policy allows public-like access for demo use. In a production environment, consider using fine-grained IAM roles and private access only.

#### Instructions:

**Step 1:**  
- Open your bucket in the **S3 Console**.
- Go to the **Permissions** tab.

**Step 2:**  
- In the **Bucket policy** section, click **Edit**.

**Step 3:**  
- Paste the following bucket policy JSON into the editor:

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