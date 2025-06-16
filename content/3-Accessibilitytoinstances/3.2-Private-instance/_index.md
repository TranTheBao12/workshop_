---
title : "Create folders in S3 Bucket"
date : "2025-05-28"
weight : 2
chapter : false
pre : " <b> 3.2. </b> "
---

### Step 2: Create folders in the bucket

After creating the bucket, you need to organize your storage by creating folders for specific types of files.

#### Instructions:

**Step 1:**
- Open the bucket you just created.
- Click on the **Create folder** button.

**Step 2:**
- Enter folder names, for example:
  - `uploads/` (to store input images)
  - `temp/` (to store temporary text and audio files)
  - `outputs/` (to store the final video output)
- Click **Create folder** for each.

After creating the folders, your folder structure in the bucket will look like this:


![S3 Folder Structure Screenshot](/images/2.prerequisite/anh10.png)

{{% notice tip %}}
Note: These folders are not physical directories but are treated as key prefixes in S3. They help organize your content more clearly and efficiently.
{{% /notice %}}
