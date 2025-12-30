import os
import random
import shutil
from tqdm import tqdm

# --- Cấu hình ---
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
ORIG_DIR = os.path.join(CURR_DIR, 'original_dataset')  # nơi chứa ảnh gốc
TARGET_DIR = 'dataset'        # nơi sẽ lưu train/val
train_ratio = 0.7             # 70% train, 20% val, 10% test

# --- Tạo thư mục đích ---
for folder in ['train', 'val', 'test']:
    os.makedirs(os.path.join(TARGET_DIR, folder), exist_ok=True)

# --- Duyệt qua từng lớp ---
classes = os.listdir(ORIG_DIR)
for cls in classes:
    cls_path = os.path.join(ORIG_DIR, cls)
    if not os.path.isdir(cls_path):
        continue

    images = os.listdir(cls_path)
    random.shuffle(images)

    split_index1 = int(len(images) * train_ratio)
    split_index2 = int(len(images) * (train_ratio + 0.2))
    train_images = images[:split_index1]
    val_images = images[split_index1:split_index2]
    test_images = images[split_index2:]

    # tạo thư mục đích cho mỗi lớp
    os.makedirs(os.path.join(TARGET_DIR, 'train', cls), exist_ok=True)
    os.makedirs(os.path.join(TARGET_DIR, 'val', cls), exist_ok=True)
    os.makedirs(os.path.join(TARGET_DIR, 'test', cls), exist_ok=True)

    # copy ảnh
    print(f"Đang xử lý lớp: {cls} ({len(images)} ảnh)")

    for img in tqdm(train_images, desc=f"Train {cls}"):
        shutil.copy(
            os.path.join(cls_path, img),
            os.path.join(TARGET_DIR, 'train', cls, img)
        )

    for img in tqdm(val_images, desc=f"Val {cls}"):
        shutil.copy(
            os.path.join(cls_path, img),
            os.path.join(TARGET_DIR, 'val', cls, img)
        )

    for img in tqdm(test_images, desc=f"Test {cls}"):
        shutil.copy(
            os.path.join(cls_path, img),
            os.path.join(TARGET_DIR, 'test', cls, img)
        )
# for cls in classes:
#     cls_path = os.path.join(ORIG_DIR, cls)
#     if not os.path.isdir(cls_path):
#         continue

#     images = os.listdir(cls_path)
#     random.shuffle(images)

#     split_index = int(len(images) * train_ratio)
#     train_images = images[:split_index]
#     val_images = images[split_index:]
#     test_images = images[split_index + len(val_images):]

#     # tạo thư mục đích cho mỗi lớp
#     os.makedirs(os.path.join(TARGET_DIR, 'train', cls), exist_ok=True)
#     os.makedirs(os.path.join(TARGET_DIR, 'val', cls), exist_ok=True)

#     # copy ảnh
#     print(f"Đang xử lý lớp: {cls} ({len(images)} ảnh)")

#     for img in tqdm(train_images, desc=f"Train {cls}"):
#         shutil.copy(
#             os.path.join(cls_path, img),
#             os.path.join(TARGET_DIR, 'train', cls, img)
#         )

#     for img in tqdm(val_images, desc=f"Val {cls}"):
#         shutil.copy(
#             os.path.join(cls_path, img),
#             os.path.join(TARGET_DIR, 'val', cls, img)
#         )


print("\nHoàn tất tách dữ liệu!")