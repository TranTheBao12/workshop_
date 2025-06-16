---
title: "Dọn dẹp tài nguyên"
date: "2025-05-28"
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

### 6. Dọn dẹp tài nguyên (15 phút)

**Mục tiêu:** Xóa tất cả các tài nguyên AWS đã tạo trong workshop để tránh phát sinh chi phí không mong muốn.

---

#### Thao tác:

1.  **Xóa Môi trường Elastic Beanstalk:**
    * **Đăng nhập vào AWS Management Console** và điều hướng đến dịch vụ **Elastic Beanstalk**.
    * Trong danh sách các ứng dụng, chọn **ứng dụng ImageToVideoWeb** của bạn.
    * Nhấp vào **Environment name** (ví dụ: `ImageToVideoWeb-env`).
    * Trong trang chi tiết môi trường, chọn **Actions** (Hành động) và sau đó chọn **Terminate Environment** (Chấm dứt môi trường).
    * Xác nhận việc chấm dứt môi trường khi được yêu cầu. Quá trình này có thể mất vài phút.

    ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh22.png)

---

2.  **Xóa S3 Bucket:**
    * Sau khi môi trường Elastic Beanstalk đã được chấm dứt hoàn toàn (đảm bảo không còn instance nào đang sử dụng bucket), điều hướng đến dịch vụ **Amazon S3**.
    * Tìm và chọn **bucket** có tên `imagetovideoweb-demo-<UNIQUE-ID>` của bạn.
    * Để xóa một bucket, trước tiên bạn cần **xóa tất cả các đối tượng (files/folders) bên trong nó**. Nhấp vào bucket, chọn tất cả các đối tượng, sau đó chọn **Delete** và làm theo hướng dẫn xác nhận.
    * Sau khi bucket trống, quay lại danh sách các bucket, chọn bucket của bạn và nhấp **Delete bucket**.
    * Nhập tên bucket để xác nhận việc xóa.
 ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh23.png)


---

3.  **Xóa IAM Roles và Key Pair:**
    * **Đăng nhập vào AWS Management Console** và điều hướng đến dịch vụ **IAM (Identity and Access Management)**.
    * Trong thanh điều hướng bên trái, chọn **Roles**.
    * Tìm và chọn các role bạn đã tạo: `ImageToVideoWeb-EC2-InstanceRole` và `ImageToVideoWeb-ServiceRole`.
    * Với mỗi role, nhấp **Delete role** và xác nhận việc xóa.
    * Điều hướng đến dịch vụ **EC2**.
    * Trong thanh điều hướng bên trái, dưới mục **Network & Security**, chọn **Key Pairs**.
    * Tìm và chọn **Key pair** bạn đã tạo: `ImageToVideoWeb-KeyPair`.
    * Nhấp **Actions** và chọn **Delete**. Xác nhận việc xóa.

    ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh24.png)

       ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh25.png)

---

4.  **Kiểm tra Tài nguyên và Chi phí:**
    * Truy cập **AWS Billing Dashboard** (`https://console.aws.amazon.com/billing/`).
    * Kiểm tra phần **Bills** hoặc **Cost Explorer** để đảm bảo không còn tài nguyên nào đang chạy và không có chi phí phát sinh bất thường sau workshop.



---

{{% notice tip %}}
Bạn nên tạo thói quen dọn dẹp tài nguyên sau mỗi buổi thực hành hoặc bài lab, đặc biệt khi dùng tài khoản trong Free Tier hoặc học tập.
{{% /notice %}}