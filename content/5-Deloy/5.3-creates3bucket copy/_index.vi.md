---
title: "Triển khai Ứng dụng"
date: "2025-05-28"
weight: 3
chapter: false
pre: " <b> 5.3 </b> "
---

### 5.3 Triển khai Ứng dụng:

1.  Chờ **5-10 phút** (hoặc có thể lâu hơn tùy thuộc vào độ phức tạp của môi trường và lưu lượng truy cập AWS) để Elastic Beanstalk tạo môi trường, bao gồm các instance EC2, load balancer (nếu có), auto scaling group, v.v., và triển khai ứng dụng của bạn.

2.  **Theo dõi tiến trình triển khai:**
    * Bạn có thể theo dõi tiến trình trong cửa sổ **Output** của Visual Studio (chọn "AWS Deployment" hoặc "AWS Toolkit").
    * Hoặc theo dõi trực tiếp trên **AWS Elastic Beanstalk Console** trong trình duyệt của bạn.

3.  **Lấy URL môi trường:** Sau khi môi trường chuyển sang trạng thái "**Health: Ok**" hoặc "**Ready**", bạn sẽ thấy URL môi trường (ví dụ: `http://imagetovideoweb-env.eba-xxxx.us-east-1.elasticbeanstalk.com`) hiển thị trong AWS Toolkit hoặc trên bảng điều khiển Elastic Beanstalk.

---

 ![Giao diện cây thư mục trong S3 Console](/images/2.prerequisite/anh21.png)

---

### Kiểm tra Ứng dụng:

1.  Truy cập **URL môi trường** đã lấy được ở bước trước trong trình duyệt web của bạn.
2.  Kiểm tra giao diện web để đảm bảo ứng dụng **ASP.NET Core** của bạn đang chạy đúng cách và hiển thị giao diện mong muốn.
3.  Thực hiện các chức năng chính của ứng dụng (bao gồm chức năng "**Image to Video**" nếu đó là tính năng chính) để xác nhận mọi thứ hoạt động như mong đợi.