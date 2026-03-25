<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓 Faculty of Information Technology (DaiNam University)
    </a>
</h2>
<h2 align="center">
    PLATFORM ERP
</h2>
<div align="center">
    <p align="center">
        <img src="docs/logo/aiotlab_logo.png" alt="AIoTLab Logo" width="170"/>
        <img src="docs/logo/fitdnu_logo.png" alt="AIoTLab Logo" width="180"/>
        <img src="docs/logo/dnu_logo.png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)

</div>

## 📖 1. Giới thiệu
Platform ERP được áp dụng vào học phần Thực tập doanh nghiệp dựa trên mã nguồn mở Odoo. 

## 🔧 2. Các công nghệ được sử dụng
<div align="center">

### Hệ điều hành
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
### Công nghệ chính
[![Odoo](https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![XML](https://img.shields.io/badge/XML-FF6600?style=for-the-badge&logo=codeforces&logoColor=white)](https://www.w3.org/XML/)
### Cơ sở dữ liệu
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
</div>

## 🚀 3. Các project đã thực hiện dựa trên Platform

Một số project sinh viên đã thực hiện:
- #### [Khoá 15](./docs/projects/K15/README.md)
- #### [Khoá 16](./docs/projects/K16/README.md)
- #### [Khoá 17](./docs/projects/K17/README.md)
## ⚙️ 4. Cài đặt

### 4.1. Cài đặt công cụ, môi trường và các thư viện cần thiết

#### 4.1.1. Tải project.
```
git clone https://github.com/FIT-DNU/Business-Internship.git
```
#### 4.1.2. Cài đặt các thư viện cần thiết
Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết

```
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
```
#### 4.1.3. Khởi tạo môi trường ảo.
- Khởi tạo môi trường ảo
```
python3.10 -m venv ./venv
```
- Thay đổi trình thông dịch sang môi trường ảo
```
source venv/bin/activate
```
- Chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu
```
pip3 install -r requirements.txt
```
### 4.2. Setup database

Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.
```
sudo docker-compose up -d
```
### 4.3. Setup tham số chạy cho hệ thống
Tạo tệp **odoo.conf** có nội dung như sau:
```
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5431
xmlrpc_port = 8069
```
Có thể kế thừa từ file **odoo.conf.template**
### 4.4. Chạy hệ thống và cài đặt các ứng dụng cần thiết
Lệnh chạy
```
python3 odoo-bin.py -c odoo.conf -u all
```
Người sử dụng truy cập theo đường dẫn _http://localhost:8069/_ để đăng nhập vào hệ thống.

## 📝 5. License

© 2024 AIoTLab, Faculty of Information Technology, DaiNam University. All rights reserved.

## 📂 6. Dự án BTL_QLVB-NS (Kết hợp Quản lý Văn bản, Nhân sự, Tài sản & Phòng họp)

Dự án này là sự hợp nhất của 4 module nghiệp vụ chính, được đồng bộ hóa về dữ liệu và quy trình hoạt động.

### 6.1. Các Module tích hợp
- **Nhân sự (nhan_su)**: Module nền tảng quản lý thông tin nhân viên, chức vụ, đơn vị công tác và hồ sơ cá nhân.
- **Quản lý Văn bản (quan_ly_van_ban)**: Quản lý luồng văn bản đến và văn bản đi, liên kết trực tiếp với nhân viên xử lý.
- **Quản lý Tài sản (quan_ly_tai_san)**: Theo dõi danh mục tài sản, phân bổ, khấu hao và lịch sử mượn trả tài sản.
- **Quản lý Phòng họp (phong_hop)**: Đặt lịch phòng họp, kiểm tra trạng thái phòng real-time và tích hợp mượn thiết bị đi kèm.

### 6.2. Các thay đổi chính và Cải tiến
- **Thống nhất sơ đồ tổ chức**: Toàn bộ hệ thống sử dụng chung model `don_vi` (Đơn vị) thay vì tách biệt nhiều khái niệm phòng ban khác nhau.
- **Khử lỗi phụ thuộc vòng (Circular Dependency)**: Cấu trúc lại quan hệ giữa Nhân sự và Văn bản bằng kỹ thuật kế thừa model (`_inherit`), đảm bảo hệ thống ổn định khi cài đặt mới.
- **Liên kết Tài khoản**: Tích hợp chặt chẽ giữa `res.users` (Tài khoản Odoo) và `nhan_vien` (Thông tin nhân sự) để tự động hóa phân quyền.

### 6.3. Nguyên lý hoạt động
Hệ thống hoạt động dựa trên nguyên tắc **Dữ liệu tập trung (Centralized Data)**:
1. **Nhân viên & Đơn vị** là thực thể trung tâm.
2. Mọi hoạt động như **Xử lý văn bản**, **Mượn tài sản**, hay **Đặt phòng họp** đều truy xuất thông tin từ thực thể trung tâm này để đảm bảo tính toàn vẹn dữ liệu.
3. **Phòng họp** tích hợp với **Tài sản**: Khi đặt phòng có yêu cầu thiết bị, hệ thống tự động kiểm tra và tạo đơn mượn tài sản tương ứng.

---
