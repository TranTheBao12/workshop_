---
title : "Configure AWS CLI"
date : "2025-05-28"
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---

### Configure AWS CLI

In this step, we will configure the AWS Command Line Interface (CLI) to allow interaction with AWS services from your terminal.

---

#### 1. Open Terminal or Command Prompt

Depending on your OS:

- **Windows**: Use Command Prompt or PowerShell.
- **Linux/macOS**: Use the terminal.

---

#### 2. Run the `aws configure` Command

Enter Access Key, Secret Key, region (us-east-1), output (json) then check with command aws sts get-caller-identity
![AWS Explorer](/images/2.prerequisite/anh6.png)
```bash
aws configure
