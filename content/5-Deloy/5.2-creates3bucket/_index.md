---
title: "Deploy to Elastic Beanstalk from Visual Studio 2022"
date: "2025-05-28"
weight: 2
chapter: false
pre: " <b> 5.2 </b> "
---

### Deploy to Elastic Beanstalk from Visual Studio 2022

**Prerequisites:** Make sure you have installed **AWS Toolkit for Visual Studio** and are connected to your AWS account in Visual Studio.

#### Steps:

1. In Visual Studio, right-click your ASP.NET Core project in **Solution Explorer**.

2. Select **Publish to AWS Elastic Beanstalk...**.

* (Make sure you are logged in and connected to the correct AWS account in Visual Studio's AWS Explorer before performing this step.)
3. The **Publish to Elastic Beanstalk** dialog box will appear. Configure the following:

* **Deployment Target:** Select **Create a new application environment**.

* **Account Region:** Select the AWS region you want to deploy to (e.g., `US East (N. Virginia) us-east-1`).

* Click **Next**.
   ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh17.png)
4. **Application Environment:**
* **Application Name:** Enter `ImageToVideoWeb`.

* **Environment Name:** Enter `ImageToVideoWeb-env`.

* **Platform:**
* **Environment type:** Select **Web server environment**.

* **Platform:** Select **.NET on Windows Server**.

* **Platform Branch:** Select the appropriate Windows Server edition (e.g., `Windows Server Core` or `Windows Server full`).

* **Platform Version:** Select the .NET version (e.g. `.NET 8 (64bit Amazon Linux 2 / Windows Server 2022)`) or the latest supported .NET 8 version.
* Click **Next**.
 ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh19.png)
5. **AWS Options:**
* **Instance type:** Select `t3.micro` (eligible for Free Tier for testing purposes).
* **EC2 Key pair:** Select the `ImageToVideoWeb-KeyPair` created in step 4.1.3.
* **EC2 security groups:** Leave the default or create a new security group if custom rules are needed.
* **Application Health Check URL:** Leave the default or customize if your application has its own health check endpoint.
* **Root Folder:** Defaults to `/` for web applications.
* **Use Enhanced Health Reporting:** Can be enabled or disabled depending on monitoring needs.
* **Enable Rolling Deployments:** Can be enabled or disabled.
* **Service role:** Select the role created in step 4.1.2 (e.g. `ImageToVideoWeb-ServiceRole`).
* **Instance profile:** Select the role created in step 4.1.1 (e.g. `ImageToVideoWeb-EC2-InstanceRole`).
* Click **Next**.
    ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh18.png)

     ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh20.png)
6. **Application Options:**
* **Deployment bundle type:** Select **Full .NET Core deployment (Self-contained)** if you want the application to include all the dependencies of the .NET runtime. Select **Framework-dependent deployment** if you believe the .NET runtime is already installed on the instance or you will install it yourself. With Elastic Beanstalk for .NET on Windows, Self-contained is generally recommended to ensure a full environment.
* Other options (**Environment Variables**, **.NET Core Build and Publish Options**) can be configured as needed.

* Click **Next**.

7. **Review:**
* Review all settings.

* Click **Publish** to start the process of creating the Elastic Beanstalk application and environment.

**Screenshot:** The AWS Toolkit interface in Visual Studio after you have configured and are ready to press "Publish".