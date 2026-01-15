import os
def rename_images_in_directory(directory):
    files = os.listdir(directory)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg'))]
    image_files.sort()

    global name

    for index, filename in enumerate(image_files, start=1):
        file_extension = os.path.splitext(filename)[1]
        # Tạo tên mới theo định dạng số thứ tự
        new_name = f"{name}_{index}{file_extension}"
        # Đường dẫn đầy đủ của file cũ và file mới
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
      
        os.rename(old_file, new_file)

if __name__ == "__main__":
    global name
    path = "data\\raw\\Anthracnose"

    name = input("Nhập tên cần thay đổi (default is 'image'): ") or "image"
    current_directory = os.path.abspath(path)
    rename_images_in_directory(current_directory)

    print("Hoàn tất.")
