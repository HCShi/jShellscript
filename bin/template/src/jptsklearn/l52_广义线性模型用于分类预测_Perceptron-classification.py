#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split  # 导入数据集切分模块
from sklearn.linear_model import Perceptron
# 感知机模型非常简单, 输入为一些特征向量, 输出则由正类和负类组成; 而输入和输出之间, 则是由符号函数连接
##################################################################
## 使用 scikit-learn 提供的 make_classification 方法生成一组可被二分类的二维数组作为数据集
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1)
train_feature, test_feature, train_target, test_target = train_test_split(X1, Y1, train_size=0.77, random_state=56)

model = Perceptron()
model.fit(train_feature, train_target)
results = model.predict(test_feature)  # 结果是 0, 1

plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1)  # 包括两种颜色 红色和黄色
plt.scatter(test_feature[:, 0], test_feature[:, 1], marker=',')  # 一种颜色 蓝色
for i, txt in enumerate(results):
    plt.annotate(txt, (test_feature[:, 0][i],test_feature[:, 1][i]))  # 可以看到 蓝色分为两部分, 正好与红色和黄色分界线相同

plt.show()
##################################################################
## 总结:
# 1. 广义线性模型是机器学习中十分简单基础的模型; 但是由于其本身的特点, 只能用于二分类问题;
# 2. 对于实际生活中经常遇到的多分类及非线性分类问题, 无法适用; 但对于刚刚入门机器学习的朋友来说, 线性分类模型是不错范例
# 3. 这个实验的结果还可以
# 4. results 得到的是 0, 1; Y1 得到的也是 0, 1
