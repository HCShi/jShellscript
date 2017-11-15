#!/usr/bin/python3
# coding: utf-8
from sklearn import datasets
from sklearn.svm import LinearSVR  # 导入线性支持向量机回归模块
from matplotlib import pyplot as plt
from sklearn.model_selection import cross_val_predict  # 导入交叉验证模块

boston = datasets.load_boston()
print(boston.DESCR)  # 输出数据集介绍文档
# 该数据集有 506 条数据, 每条数据包含 13 个特征变量和对应的房屋价格; 其中, 特征变量包含房屋所在位置的人口比例、交通方便程度、空气质量等
feature = boston.data
target = boston.target

model = LinearSVR()
# 这一次, 我们不再像之前的内容, 将数据集划分为 70% 训练集和 30% 测试集; 而是采用机器学习中另一种十分常见的测试方式: 交叉验证;
# 交叉验证, 就是将整个数据集等分为 n 等份, 然后使用其中 n-1 等份训练模型, 再使用另外的 1 份测试模型, 循环验证
predictions = cross_val_predict(model, feature, target, cv=10)  # cv = 10 就是指将整个数据集等分为 10 份

plt.scatter(target, predictions)
plt.plot([target.min(), target.max()], [target.min(), target.max()], 'k--', lw=4)
plt.xlabel("true_target")
plt.ylabel("prediction")
plt.show()
# 可以看出, 预测的效果还是很不错的。大部分都均匀分布在 45 度参考线的左右, 即代表真实值与预测值之间的绝对误差较小
