---
title: "Create Key Pair"
date: "2025-05-28"
weight: 3
chapter: false
pre: " <b> 5.1.3 </b> "
---

### 5.1.3. Create Key Pair

Key pairs are required to enable SSH (or RDP for Windows) connections to EC2 instances in your Elastic Beanstalk environment for testing or debugging purposes.

#### Steps:

1. **Log in to the AWS Management Console** and navigate to the **EC2 (Elastic Compute Cloud)** service.

2. In the left navigation bar, under **Network & Security**, select **Key Pairs**.

3. Click the **Create key pair** button.

4. Give the Key pair a name (e.g. `ImageToVideoWeb-KeyPair`).

5. Select **Key pair type** as **RSA** and **Private key format** as **.pem** (for Linux SSH client) or **.ppk** (if you use PuTTY on Windows). For Windows environment, .pem also works with built-in SSH tools or you can convert to .ppk later. Choose **.pem** for dissemination.
6. Click **Create key pair**. The private key file (**.pem** or **.ppk**) will be automatically downloaded to your browser. **Store this file in a safe place and do not share it.**