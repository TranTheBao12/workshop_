---
title: "Triển khai (Deploy) lên Elastic Beanstalk từ Visual Studio 2022"
date: "2025-05-28"
weight: 2
chapter: false
pre: " <b> 5.2 </b> "
---

### Triển khai (Deploy) lên Elastic Beanstalk từ Visual Studio 2022

**Điều kiện tiên quyết:** Đảm bảo bạn đã cài đặt **AWS Toolkit for Visual Studio** và đã kết nối với tài khoản AWS của mình trong Visual Studio.

#### Các bước:

1.  Trong Visual Studio, nhấp chuột phải vào dự án ASP.NET Core của bạn trong **Solution Explorer**.
2.  Chọn **Publish to AWS Elastic Beanstalk...**.
    * (Đảm bảo bạn đã đăng nhập và kết nối đúng tài khoản AWS trong AWS Explorer của Visual Studio trước khi thực hiện bước này.)
3.  Hộp thoại **Publish to Elastic Beanstalk** sẽ xuất hiện. Cấu hình các mục sau:
    * **Deployment Target:** Chọn **Create a new application environment**.
    * **Account Region:** Chọn khu vực AWS mà bạn muốn triển khai (ví dụ: `US East (N. Virginia) us-east-1`).
    * Nhấp **Next**.
    ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh17.png)
4.  **Application Environment:**
    * **Application Name:** Nhập `ImageToVideoWeb`.
    * **Environment Name:** Nhập `ImageToVideoWeb-env`.
    * **Platform:**
        * **Environment type:** Chọn **Web server environment**.
        * **Platform:** Chọn **.NET on Windows Server**.
        * **Platform Branch:** Chọn phiên bản Windows Server phù hợp (ví dụ: `Windows Server Core` hoặc `Windows Server full`).
        * **Platform Version:** Chọn phiên bản .NET (ví dụ: `.NET 8 (64bit Amazon Linux 2 / Windows Server 2022)`) hoặc phiên bản .NET 8 mới nhất được hỗ trợ.
    * Nhấp **Next**.
    ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh19.png)
5.  **AWS Options:**
    * **Instance type:** Chọn `t3.micro` (đủ điều kiện Free Tier cho mục đích thử nghiệm).
    * **EC2 Key pair:** Chọn `ImageToVideoWeb-KeyPair` đã tạo ở bước 4.1.3.
    * **EC2 security groups:** Để mặc định hoặc tạo một nhóm bảo mật mới nếu cần các quy tắc tùy chỉnh.
    * **Application Health Check URL:** Để mặc định hoặc tùy chỉnh nếu ứng dụng của bạn có health check endpoint riêng.
    * **Root Folder:** Mặc định là `/` cho ứng dụng web.
    * **Use Enhanced Health Reporting:** Có thể bật hoặc tắt tùy nhu cầu giám sát.
    * **Enable Rolling Deployments:** Có thể bật hoặc tắt.
    * **Service role:** Chọn role đã tạo ở bước 4.1.2 (ví dụ: `ImageToVideoWeb-ServiceRole`).
    * **Instance profile:** Chọn role đã tạo ở bước 4.1.1 (ví dụ: `ImageToVideoWeb-EC2-InstanceRole`).
    * Nhấp **Next**.
    ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh18.png)

     ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh20.png)
6.  **Application Options:**
    * **Deployment bundle type:** Chọn **Full .NET Core deployment (Self-contained)** nếu bạn muốn ứng dụng chứa tất cả các dependencies của .NET runtime. Chọn **Framework-dependent deployment** nếu bạn tin rằng .NET runtime đã được cài đặt sẵn trên instance hoặc bạn sẽ tự cài đặt nó. Với Elastic Beanstalk cho .NET trên Windows, Self-contained thường được khuyến nghị để đảm bảo môi trường đầy đủ.
    * Các tùy chọn khác (**Environment Variables**, **.NET Core Build and Publish Options**) có thể cấu hình nếu cần.
    * Nhấp **Next**.
7.  **Review:**
    * Kiểm tra lại tất cả các cài đặt.
    * Nhấp **Publish** để bắt đầu quá trình tạo ứng dụng và môi trường Elastic Beanstalk.

 ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh21.png)