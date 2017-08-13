#!/usr/bin/python3
# coding: utf-8
import pandas as pd
from sklearn.svm import LinearSVC  # 导入线性支持向量机分类器
from sklearn.linear_model import Perceptron  # 导入感知机分类器
from sklearn.model_selection import train_test_split  # 导入数据集切分模块
##################################################################
## 准备数据
df = pd.read_csv("data.csv", header=0)
x = df[["x", "y"]]
y = df["class"]
train_feature, test_feature, train_target, test_target = train_test_split(x, y, train_size=0.77, random_state=56)
import matplotlib.pyplot as plt
plt.scatter(x['x'], x['y'], c=y)
plt.show()  # 可以看到数据是分成两部分的, 有两个噪声...

# 构建感知机预测模型
model = Perceptron()
model.fit(train_feature, train_target)
results = model.score(test_feature, test_target); print(results)  # 0.913043478261; 感知机分类准确度
# 构建线性支持向量机分类模型
model2 = LinearSVC()
model2.fit(train_feature, train_target)
results2 = model2.score(test_feature, test_target); print(results2)  # 1.0; 支持向量机分类准确度
##################################################################
## 总结:
# 1. 具体解释见: 实验楼相关参考, README.md
# 2. data.csv 数据放置的很合理...
