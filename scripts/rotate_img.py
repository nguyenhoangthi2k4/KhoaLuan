import os
from PIL import Image

def rotate_images_in_directory(directory, angle):
    # Lấy danh sách ảnh trong thư mục
    image_files = [
        f for f in os.listdir(directory)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))
    ]

    # Tạo thư mục theo góc xoay
    save_folder = os.path.join(directory, str(angle))
    os.makedirs(save_folder, exist_ok=True)

    print(f"Ảnh xoay sẽ được lưu trong: {save_folder}")

    # Xoay ảnh
    for filename in image_files:
        source_path = os.path.join(directory, filename)
        save_path   = os.path.join(save_folder, filename)

        try:
            img = Image.open(source_path)
            rotated = img.rotate(angle, expand=True)
            rotated.save(save_path)
            print(f"Đã xoay: {filename}")
        except Exception as e:
            print(f"Lỗi với {filename}: {e}")

if __name__ == "__main__":
    # Lấy đường dẫn thư mục hiện tại giống rename.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print(f"Thư mục đang xử lý: {current_directory}")

    # Nhập góc xoay
    try:
        angle = int(input("Nhập góc xoay (VD: 90, 180, 270): ").strip())
    except:
        print("Góc không hợp lệ!")
        exit()

    rotate_images_in_directory(current_directory, angle)
    print("\nHoàn tất xoay ảnh!")