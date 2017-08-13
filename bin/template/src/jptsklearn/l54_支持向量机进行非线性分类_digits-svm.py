#!/usr/bin/python3
# coding: utf-8
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 导入数据集切分模块
from sklearn.svm import SVC  # 导入非线性支持向量机分类器
from sklearn.metrics import accuracy_score  # 导入评估模块
import matplotlib.pyplot as plt
##################################################################
## 准备数据
digits = datasets.load_digits()
# 绘制数据集前 5 个手写数字的灰度图
for index, image in enumerate(digits.images[:5]):
    plt.subplot(2, 5, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

# 训练手写数字识别模型
feature = digits.data
target = digits.target
images = digits.images
train_feature, test_feature, train_target, test_target, train_images, test_images = train_test_split(feature, target, images, test_size=0.33)

# 加载模型, 计算结果
model = SVC()  # scores: 0.531986531987
# model = SVC(gamma=0.001)  # scores: 0.991582491582; gamma 是核函数因数..., 具体解释见 实验楼
model.fit(train_feature, train_target)
results = model.predict(test_feature)
scores = accuracy_score(test_target, results)
print(scores)

# 可视化查看前 4 项预测结果
images_labels_and_prediction = list(zip(test_images, test_target, results))
for index, (image, true_label, prediction_label) in enumerate(images_labels_and_prediction[:4]):
    plt.subplot(2, 4, index + 5)
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.xlabel("prediction:%i" % prediction_label)
    plt.title("True:%i" % true_label)
plt.show()
##################################################################
## 总结:
# 1. 参数选取, 见 莫烦 Python
