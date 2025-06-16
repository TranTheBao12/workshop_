---
title: "Create an IAM Role for Elastic Beanstalk Service"
date: "2025-05-28"
weight: 2
chapter: false
pre: " <b> 5.1.2 </b> "
---

### 5.1.1. Create an IAM Role for Elastic Beanstalk Service (Role that EC2 server will use)

This is the **role** that the **EC2** instances in your **Elastic Beanstalk** environment will assume. It needs minimal permissions to operate in the Elastic Beanstalk environment, including communicating with other AWS services like S3, CloudWatch, etc.

#### Steps:

1.  **Log in to the AWS Management Console** and navigate to the **IAM (Identity and Access Management)** service.
2.  In the left navigation bar, select **Roles**.
3.  Click the **Create role** button.
4.  In the **Select type of trusted entity** section, select **AWS service**.
5.  In the **Choose a use case** section, select **EC2**, then click **Next**.
![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh12.png)
6.  **Add permissions:**
    * Search for and select the **AWSElasticBeanstalkWebTier** policy.
    * Search for and select the **AWSElasticBeanstalkWorkerTier** policy (if your application can use a worker environment, although for a typical web application WebTier is usually sufficient, it is safer to add it).
    * Search for and select the **AmazonS3FullAccess** policy (or a custom S3 policy with more specific permissions if you want to restrict S3 access).
    * If your application needs access to other AWS services (e.g. DynamoDB, RDS, SQS, SNS), add the corresponding policies.
7.  Click **Next**.
8.  **Tags (Optional):** Add key-value tag pairs as needed to organize your resources, then click **Next**.
9.  **Review and Create:**
    * Set the **Role name** (e.g. `ImageToVideoWeb-EC2-InstanceRole`).
    * Review the attached policies.
    * Click **Create role**.
![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh13.png)
---