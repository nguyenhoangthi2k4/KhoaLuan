import cv2
import os
import numpy as np

def slice_image(path, output_dir, tile_size=640, overlap=0.2):
    """
    Cắt ảnh lớn thành các mảnh nhỏ có độ chồng lấn.
    """
    files = os.listdir(path)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg'))] 
    image_files.sort()

    for image_file in image_files:
        img_path = os.path.join(path, image_file)
        img = cv2.imread(img_path)

        if img is None:
            continue

        h, w, _ = img.shape
        stride = int(tile_size * (1 - overlap)) # Khoảng cách giữa các nhát cắt
    
        base_name = os.path.splitext(os.path.basename(image_file))[0]

        if not os.path.exists(os.path.join(output_dir, base_name)):
            os.makedirs(os.path.join(output_dir, base_name), exist_ok=True)
    
        count = 0
        for y in range(0, h, stride):
            for x in range(0, w, stride):
                # Tính toán tọa độ cắt, đảm bảo không vượt quá kích thước ảnh gốc
                y_end = min(y + tile_size, h)
                x_end = min(x + tile_size, w)
                y_start = y_end - tile_size
                x_start = x_end - tile_size
                
                tile = img[max(0, y_start):y_end, max(0, x_start):x_end]
                
                # Lưu mảnh cắt
                tile_name = f"{base_name}_tile_{count}.jpg"
                cv2.imwrite(os.path.join(output_dir, base_name, tile_name), tile)
                count += 1
                
        print(f"Đã cắt xong {count} mảnh từ ảnh {base_name}")

if __name__ == "__main__":
    path = "data\\raw\\Mosaic_Virus" 
    output_folder = "output_tiles"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)

    slice_image(path, output_folder, tile_size=640, overlap=0.2)