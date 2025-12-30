# Chẩn đoán Bệnh hại trên Cây Dưa hấu bằng Deep Learning

>  Graduation Thesis: Watermelon Disease Detection through Leaf Images using Deep Learning

---

## Tổng quan đề tài

Khóa luận này tập trung vào việc nghiên cứu và xây dựng mô hình học sâu (Deep Learning) nhằm tự động nhận diện các loại bệnh phổ biến trên cây dưa hấu thông qua hình ảnh lá. Giải pháp hướng đến việc hỗ trợ người nông dân phát hiện sớm bệnh hại, từ đó đưa ra biện pháp xử lý kịp thời, nâng cao năng suất cây trồng

- Thời gian thực hiện: 
- Công nghệ cốt lõi: Transfer Learning, Convolutional Neural Networks (CNN)
- Mô hình đề xuất:

---

## Dữ liệu (Dataset)

Do đặc thù dữ liệu nông nghiệp khan hiếm, dự án được thực hiện qua quy trình làm giàu dữ liệu nghiêm ngặt:

- **Dữ liệu gốc**: X ảnh thu thập từ thực tế
- **Tiền xử lý**:
  + Sử dụng các scripts Python để đổi tên và xoay ảnh ($90^\circ, 180^\circ, 270^\circ$)
  + Sử dụng Roboflow để tăng cường dữ liệu (Augmentation): lật, thay đổi độ sáng, thêm nhiễu, ...
- **Tổng quan dữ liệu sau khi tăng cường**: ~ X ảnh
- **Các lớp ảnh nhận diện**:
  + Anthracnose (Bệnh thán thư)
  + Downy Mildew (Bệnh sương mai)
  + Mosaic Virus (Virus khảm)
  + Healthy (Khỏe mạnh)

---

## Cấu trúc dự án
```
├── ai_assistance/          
├── app/                    # Web Demo 
│   └── main.py
├── data/                   # Quản lý dữ liệu 
│   ├── raw/                # Ảnh gốc 
│   └── processed/          # Dữ liệu sau augmentation
├── docs/                   # Báo cáo PDF và Slide
├── models/                 # Lưu trữ file trọng số (.h5, .pth)
├── notebooks/              # Quá trình thực nghiệm (Google Colab)
│   ├── 00_Preprocessing.ipynb
│   ├── 01_EDA.ipynb
│   └── 02_Training_Evaluation.ipynb
├── src                     # Mã nguồn
├── scripts/                # Tiện ích đổi tên, xoay ảnh
├── requirements.txt        # Danh sách thư viện cần thiết
└── README.md               
```
---

## Công nghệ và thư việ
- Ngôn ngữ lập trình: Python
- Framework: 
- Xử lý ảnh:
- Huấn luyện: Google Colab (GPU Tesla T4)

## Liên hệ
- Người thực hiện: Nguyễn Hoàng Thi
- MSSV: DTH225770