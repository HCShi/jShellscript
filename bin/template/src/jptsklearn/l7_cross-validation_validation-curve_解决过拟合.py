#!/usr/bin/python3
# coding: utf-8
from sklearn.learning_curve import  validation_curve  # 将 learning_curve 改为 validation_curve, 因为后者的 Model 参数是可以改变的...
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
##################################################################
## 准备数据
digits = load_digits()
X = digits.data
y = digits.target
##################################################################
## 准备测试...
param_range = np.logspace(-6, -2.3, 5)
train_loss, test_loss = validation_curve(  # 这个不会返回 train_sizes 了
        SVC(), X, y, param_name='gamma', param_range=param_range, cv=10,  # 将 SVC() 的参数外置了
        scoring='mean_squared_error')
##################################################################
## 取平均值 && 画图..., 和上一个基本上一样
train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)
plt.plot(param_range, train_loss_mean, 'o-', color="r",  # 这里没有了 train_sizes, 改为 param_range
             label="Training")
plt.plot(param_range, test_loss_mean, 'o-', color="g",
             label="Cross-validation")
plt.xlabel("gamma")  # 这里图的名字不同了
plt.ylabel("Loss")
plt.legend(loc="best")
plt.show()
##################################################################
## 总结:
# 1. 上一个是根据 train_sizes 的变化来显示有 over-fitting 的存在
# 2. 这里是根据 gamma 的变化来寻找那个参数使 over-fitting 的影响最小, 此时 train_sizes 已经是整个数据集, 因此不需要变化了
