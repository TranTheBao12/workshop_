---
title : "Create S3 Bucket"
date : "2025-05-28"
weight : 1
chapter : false
pre : " <b> 3.1. </b> "
---

### Step 1: Create an S3 Bucket

1. Go to the [AWS Management Console](https://console.aws.amazon.com/), and navigate to the **S3** service.

2. Click **Create bucket**.
![AWS Explorer](/images/2.prerequisite/anh8.png)

3. Enter the following:
   - **Bucket name**: `imagetovideoweb-demo-<UNIQUE-ID>` (e.g., `imagetovideoweb-demo-20250608`)
   - **Region**: `us-east-1` (N. Virginia)

4. In the **Block Public Access settings**, uncheck **Block all public access** (only for demo purposes; use IAM for secure production environments).

5. Click **Create bucket**.

![AWS Explorer](/images/2.prerequisite/anh9.png)


{{% notice note %}}
This configuration is intended for demonstration purposes. In a production environment, you should manage access using IAM policies instead of allowing public access.
{{% /notice %}}
