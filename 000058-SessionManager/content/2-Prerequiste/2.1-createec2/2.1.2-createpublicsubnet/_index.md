---
title : "Install AWS Toolkit for Visual Studio"
date : "2025-05-28"
weight : 2
chapter : false
pre : " <b> 2.1.2 </b> "
---

#### Install and Set Up AWS Toolkit for Visual Studio

1. After restarting Visual Studio, go to:
**Extentions** → **AWS Toolkit for .NET Refactoringr**.

2. In the AWS Toolkit for .NET Refactoringr frame, click **GET START** to enter the user information.

3. In the **Online** tab, search for **AWS Toolkit for Visual Studio**.

4. Click **Download** and then restart Visual Studio to complete the installation.

![AWS Explorer](/images/2.prerequisite/anh3.png)

---

### Initial Setup

1. After Visual Studio restarts, open it and go to:  
   **View** → **AWS Explorer**.

2. In the AWS Explorer pane, click **Add Account** to sign in.

3. You can sign in using either:
   - **AWS IAM credentials**
![AWS Explorer](/images/2.prerequisite/anh4.png)

---
### Notes

- Make sure your IAM account has full permissions to work with EC2, Lambda, S3, and the AWS services you will use in your project.
- AWS Toolkit allows you to deploy ASP.NET Core applications to services like Elastic Beanstalk or Lambda directly from Visual Studio.