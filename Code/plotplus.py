# -*- coding:utf-8 -*-  # 指定源文件的编码为UTF-8

import json  # 导入JSON模块，用于处理JSON文件
import numpy as np  # 导入NumPy库，用于数组和数学操作
import matplotlib.pyplot as plt  # 从matplotlib库导入pyplot模块用于绘图
from sklearn.utils import shuffle  # 用于打乱数据集
from PIL import Image  # 用于图像处理
import os  # 用于文件路径操作
import random  # 用于随机数生成

# 数据集路径
train_label_dir = 'D:/ai  homework\AI-Challenger-Plant-Disease-Recognition\submit\image_labels.json'   # 训练集标签文件路径
image_dir = "D:/ai  homework/train/train" # 图像文件夹路径
save_dir = './augmented_images/'  # 数据增强后保存的图像目录

classes = 61  # 定义类别数量

# 创建保存增强后图像的目录
os.makedirs(save_dir, exist_ok=True)

# 处理训练集
with open(train_label_dir, 'r', encoding='utf-8') as f_train:
    image_label_list_train = json.load(f_train)

# 数据清洗：去除无效标签（假设标签应该是整数，并在0到60之间）
cleaned_data = [img for img in image_label_list_train if 0 <= int(img['disease_class']) < classes]

# 数据增强
def augment_image(image_path):
    # 打开图像并进行增强操作
    img = Image.open(image_path)
    img_rotated = img.rotate(random.randint(1, 30))  # 随机旋转
    img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)  # 水平翻转
    return img_rotated, img_flipped


# 遍历清洗后的数据进行增强
for index, image_label in enumerate(cleaned_data):
    image_path = os.path.join(image_dir, image_label['image_name'])  # 构建图像路径
    if os.path.exists(image_path):
        # 增强图像并保存
        img_rotated, img_flipped = augment_image(image_path)

        # 保存增强后的图像
        img_rotated.save(os.path.join(save_dir, f'rotated_{index}.jpg'))
        img_flipped.save(os.path.join(save_dir, f'flipped_{index}.jpg'))

# 可视化增强后的样本数量
augmented_count = len(os.listdir(save_dir))  # 计算增强后图像的数量
print(f'Number of augmented images: {augmented_count}')  # 输出增强后图像的数量

# 示例可视化
# 随机展示部分增强后的图像
augmented_images = os.listdir(save_dir)
sample_images = random.sample(augmented_images, min(5, len(augmented_images)))

plt.figure(figsize=(10, 5))
for i, img_name in enumerate(sample_images):
    img_path = os.path.join(save_dir, img_name)
    img = Image.open(img_path)
    plt.subplot(1, 5, i + 1)
    plt.imshow(img)
    plt.axis('off')
    plt.title(img_name)

plt.show()  # 显示示例图像
