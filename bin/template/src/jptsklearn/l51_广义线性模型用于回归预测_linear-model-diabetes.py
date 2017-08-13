#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split  # 导入数据集切分模块
##################################################################
## 准备数据
diabetes = datasets.load_diabetes()
diabetes_feature = diabetes.data[:, np.newaxis, 2]
diabetes_target = diabetes.target
train_feature, test_feature, train_target, test_target = train_test_split(diabetes_feature, diabetes_target, test_size=0.33, random_state=56)
##################################################################
## 模型
model = linear_model.LinearRegression()
model.fit(train_feature, train_target)
##################################################################
## 画出来
plt.scatter(train_feature, train_target,  color='black')
plt.scatter(test_feature, test_target,  color='red')
plt.plot(test_feature, model.predict(test_feature), color='blue',
         linewidth=3)
plt.legend(('Fit line', 'Train Set', 'Test Set'), loc='lower right')  # 这里与 plot scatter 的对应顺序...
plt.title('LinearRegression Example')

plt.xticks(())
plt.yticks(())

plt.show()
##################################################################
## 总结:
# 1. 'Fit line' 可以看到, 预测的值会是线性分布的, 所以和 test_target 差别很大
# 2. 线性模型不适合用于回归, 勉强用于分类
