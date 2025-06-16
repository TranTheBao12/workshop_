---
title: "Tạo IAM Role cho EC2 Instance Profile"
date: "2025-05-28"
weight: 1
chapter: false
pre: " <b> 5.1.1 </b> "
---

### 5.1.1. Tạo IAM Role cho EC2 Instance Profile (Role mà máy chủ EC2 sẽ sử dụng)

Đây là **role** mà các **instance EC2** trong môi trường **Elastic Beanstalk** của bạn sẽ đảm nhiệm. Nó cần các quyền tối thiểu để hoạt động trong môi trường Elastic Beanstalk, bao gồm việc giao tiếp với các dịch vụ AWS khác như S3, CloudWatch, v.v.

#### Các bước:

1.  **Đăng nhập vào AWS Management Console** và điều hướng đến dịch vụ **IAM (Identity and Access Management)**.
2.  Trong thanh điều hướng bên trái, chọn **Roles**.
3.  Nhấp vào nút **Create role**.
4.  Tại mục **Select type of trusted entity**, chọn **AWS service**.
5.  Tại mục **Choose a use case**, chọn **EC2**, sau đó nhấp **Next**.
![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh12.png)
6.  **Thêm permissions:**
    * Tìm kiếm và chọn policy **AWSElasticBeanstalkWebTier**.
    * Tìm kiếm và chọn policy **AWSElasticBeanstalkWorkerTier** (nếu ứng dụng của bạn có thể sử dụng worker environment, mặc dù cho ứng dụng web thông thường thì WebTier thường là đủ, nhưng thêm vào sẽ an toàn hơn).
    * Tìm kiếm và chọn policy **AmazonS3FullAccess** (hoặc một policy S3 tùy chỉnh với các quyền cụ thể hơn nếu bạn muốn hạn chế quyền truy cập S3).
    
7.  Nhấp **Next**.
9.  **Review và Create:**
    * Đặt **Role name** (ví dụ: `ImageToVideoWeb-EC2-InstanceRole`).
    * Kiểm tra lại các policy đã đính kèm.
    * Nhấp **Create role**.
![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh13.png)
---