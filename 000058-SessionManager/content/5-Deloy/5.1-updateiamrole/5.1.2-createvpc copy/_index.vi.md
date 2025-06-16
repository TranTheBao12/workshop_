---
title: "Tạo IAM Role cho Elastic Beanstalk Service"
date: "2025-05-28"
weight: 2
chapter: false
pre: " <b> 5.1.2 </b> "
---

### 5.1.1. Tạo IAM Role cho Elastic Beanstalk Service (Vai trò mà máy chủ EC2 sẽ sử dụng)

Đây là **vai trò** mà các phiên bản **EC2** trong môi trường **Elastic Beanstalk** của bạn sẽ đảm nhiệm. Nó cần các quyền tối thiểu để hoạt động trong môi trường Elastic Beanstalk, bao gồm giao tiếp với các dịch vụ AWS khác như S3, CloudWatch, v.v.

#### Các bước:

1. **Đăng nhập vào AWS Management Console** và điều hướng đến dịch vụ **IAM (Quản lý danh tính và quyền truy cập)**.
2. Trong thanh điều hướng bên trái, chọn **Vai trò**.
3. Nhấp vào nút **Tạo vai trò**.
4. Trong phần **Chọn loại thực thể đáng tin cậy**, hãy chọn **Dịch vụ AWS**.
5. Trong phần **Chọn trường hợp sử dụng**, hãy chọn **EC2**, sau đó nhấp vào **Tiếp theo**.
![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh12.png)
6. **Thêm quyền:**
* Tìm kiếm và chọn chính sách **AWSElasticBeanstalkWebTier**.
* Tìm kiếm và chọn chính sách **AWSElasticBeanstalkWorkerTier** (nếu ứng dụng của bạn có thể sử dụng môi trường worker, mặc dù đối với ứng dụng web thông thường, WebTier thường đủ, nhưng sẽ an toàn hơn nếu thêm chính sách này).
* Tìm kiếm và chọn chính sách **AmazonS3FullAccess** (hoặc chính sách S3 tùy chỉnh với các quyền cụ thể hơn nếu bạn muốn hạn chế quyền truy cập S3).
* Nếu ứng dụng của bạn cần truy cập vào các dịch vụ AWS khác (ví dụ: DynamoDB, RDS, SQS, SNS), hãy thêm các chính sách tương ứng.
7. Nhấp vào **Tiếp theo**.
8. **Thẻ (Tùy chọn):** Thêm các cặp thẻ khóa-giá trị khi cần để sắp xếp tài nguyên của bạn, sau đó nhấp vào **Tiếp theo**.
9. **Xem lại và Tạo:**
* Đặt **Tên vai trò** (ví dụ: `ImageToVideoWeb-EC2-AWSElasticBeanstalkWebTier-InstanceRole`).
* Xem lại các chính sách đính kèm.
* Nhấp vào **Tạo vai trò**.
![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh13.png)
---