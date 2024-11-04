# -*- coding:utf-8 -*-  # 指定源文件的编码为UTF-8

import json  # 导入JSON模块，用于处理JSON文件
from matplotlib import pyplot as plt  # 从matplotlib库导入pyplot模块用于绘图
import numpy as np  # 导入NumPy库，用于数组和数学操作

# 数据集路径
train_label_dir = 'D:/ai  homework\AI-Challenger-Plant-Disease-Recognition\submit\image_labels.json'  # 训练集标签文件路径
save_dir = './'  # 结果保存目录

classes = 61  # 定义类别数量

# 处理训练集
with open(train_label_dir, 'r', encoding='utf-8') as f_train:  # 添加encoding参数指定文件编码为utf-8
    image_label_list_train = json.load(f_train)  # 读取JSON内容并加载为Python对象

# 初始化每个标签的计数
num_per_label_train = np.zeros(classes, dtype=np.int32)  # 创建一个数组，用于存储每个类别的样本数量
labels_train = []  # 存储训练集标签的列表

# 遍历训练集标签
for index in range(len(image_label_list_train)):
    image_label_train = image_label_list_train[index]  # 获取当前图像的标签信息
    label_train = image_label_train['disease_class']  # 提取疾病类别
    num_per_label_train[int(label_train)] += 1  # 更新对应类别的计数
    labels_train.append(int(label_train))  # 将标签添加到列表中

# 打印训练集中每个类别的样本数量
print('trainset:{}'.format(num_per_label_train))  # 输出训练集样本统计
plt.hist(labels_train, bins=classes)  # 绘制训练集标签的直方图
plt.xlabel('label')  # 设置x轴标签
plt.ylabel('num_per_label')  # 设置y轴标签
plt.title('Plant-Disease-Recognition-Trainset')  # 设置图表标题
plt.show()  # 显示图表
