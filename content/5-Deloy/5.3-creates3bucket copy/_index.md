---
title: "Deploy Application"
date: "2025-05-28"
weight: 3
chapter: false
pre: " <b> 5.3 </b> "
---

### 5.3 Deploy Application:

1. Wait **5-10 minutes** (or longer depending on the complexity of your environment and AWS traffic) for Elastic Beanstalk to create the environment, including EC2 instances, load balancer (if applicable), auto scaling group, etc., and deploy your application.

2. **Monitor the deployment progress:**
* You can monitor the progress in the **Output** window of Visual Studio (select "AWS Deployment" or "AWS Toolkit").

* Or monitor it directly on the **AWS Elastic Beanstalk Console** in your browser.

3. **Get the Environment URL:** Once the environment is in the "**Health: Ok**" or "**Ready** state, you should see the environment URL (e.g. `http://imagetovideoweb-env.eba-xxxx.us-east-1.elasticbeanstalk.com`) displayed in the AWS Toolkit or on the Elastic Beanstalk console.

---

#### Take a screenshot:

* **AWS Toolkit** with a successful publish status (e.g. "Deployment successful").

* The **Elastic Beanstalk Console** interface displays your environment with a "**Health: Ok**" status and the environment URL.

---

### Test the Application:

1. Visit the **Environment URL** obtained in the previous step in your web browser.

2. Test the web interface to ensure your **ASP.NET Core** application is running properly and displaying the desired interface.

3. Perform the main functions of the app (including the "**Image to Video**" function if that is a main feature) to confirm everything works as expected.
 ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh21.png)