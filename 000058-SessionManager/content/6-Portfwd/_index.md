---
title: "Resource Cleanup"
date: "2025-05-28"
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

### 6. Resource Cleanup (15 minutes)

**Objective:** Delete all AWS resources created during the workshop to avoid incurring unexpected costs.

---

#### Steps:

1.  **Delete Elastic Beanstalk Environment:**
    * **Log in to the AWS Management Console** and navigate to the **Elastic Beanstalk** service.
    * From the list of applications, select your **ImageToVideoWeb application**.
    * Click on the **Environment name** (e.g., `ImageToVideoWeb-env`).
    * On the environment details page, choose **Actions** and then select **Terminate Environment**.
    * Confirm the environment termination when prompted. This process may take several minutes.

      ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh22.png)

---

2.  **Delete S3 Bucket:**
    * Once the Elastic Beanstalk environment has been fully terminated (ensure no instances are still using the bucket), navigate to the **Amazon S3** service.
    * Find and select your bucket named `imagetovideoweb-demo-<UNIQUE-ID>`.
    * To delete a bucket, you first need to **delete all objects (files/folders) within it**. Click into the bucket, select all objects, then choose **Delete** and follow the confirmation prompts.
    * After the bucket is empty, return to the list of buckets, select your bucket, and click **Delete bucket**.
    * Enter the bucket name to confirm deletion.

     ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh23.png)

---

3.  **Delete IAM Roles and Key Pair:**
    * **Log in to the AWS Management Console** and navigate to the **IAM (Identity and Access Management)** service.
    * In the left navigation pane, select **Roles**.
    * Find and select the roles you created: `ImageToVideoWeb-EC2-InstanceRole` and `ImageToVideoWeb-ServiceRole`.
    * For each role, click **Delete role** and confirm the deletion.
    * Navigate to the **EC2** service.
    * In the left navigation pane, under **Network & Security**, select **Key Pairs**.
    * Find and select the **Key pair** you created: `ImageToVideoWeb-KeyPair`.
    * Click **Actions** and select **Delete**. Confirm the deletion.

      ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh24.png)

       ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh25.png)

---

4.  **Check Resources and Costs:**
    * Access the **AWS Billing Dashboard** (`https://console.aws.amazon.com/billing/`).
    * Check the **Bills** or **Cost Explorer** sections to ensure no resources are still running and no unusual charges are incurring after the workshop.

    **Screenshot Requirement:**
    * Screenshot of the Billing Dashboard showing that resources have been cleaned up or estimated costs are low/zero.

---

{{% notice tip %}}
It's a good habit to clean up resources after every practice session or lab, especially when using a Free Tier account or for learning purposes.
{{% /notice %}}