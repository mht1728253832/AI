import os
import json

# 图像根目录（已修正，去除了前导空格）
image_root = "D:/ai  homework/train/train"
# 初始化JSON数据列表
image_data = []

# 遍历根目录下的所有子目录
for disease_class in os.listdir(image_root):
    disease_class_path = os.path.join(image_root, disease_class)
    # 确保是目录且不是隐藏目录
    if os.path.isdir(disease_class_path) and not disease_class.startswith('.'):
        for filename in os.listdir(disease_class_path):
            if filename.endswith('.jpg'):
                image_path = os.path.join(disease_class_path, filename)
                # 将'category'更改为'disease_class'
                image_data.append({"image_name": filename, "disease_class": disease_class})

# 写入JSON文件
with open('image_labels.json', 'w', encoding='utf-8') as json_file:
    json.dump(image_data, json_file, ensure_ascii=False, indent=4)

print("JSON文件创建成功。")
