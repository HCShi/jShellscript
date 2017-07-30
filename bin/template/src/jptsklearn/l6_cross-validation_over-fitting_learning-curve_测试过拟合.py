#!/usr/bin/python3
# coding: utf-8
# 请参考 莫烦Python 视频: 交叉验证 2 Cross-validation; 会有图文解释
from sklearn.learning_curve import  learning_curve  # 可视化学习的整个过程, 从而降低误差
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
##################################################################
## 准备数据
digits = load_digits()
X = digits.data
y = digits.target
print(X[:1], '\n', y)
print(X.shape, y.shape)  # (1797, 64) (1797,)
##################################################################
## 检测过拟合化
# SVC() 内部直接构造一个带参数的 Model; cv=10, 表示生成 10 份的交叉检验数据
# mean_squared_error 用方差值进行测试
# train_sizes 表示采用数据样本的 10%, 25%, 50%, 75%, 100% 来进行模型训练
# 意思就是找几个点, 计算这几个点上的精确度, 并画出来
train_sizes, train_loss, test_loss = learning_curve(
        SVC(gamma=0.01), X, y, cv=10, scoring='mean_squared_error',
        train_sizes=[0.1, 0.25, 0.5, 0.75, 1])  # 这条语句执行会很费时间, 不要每次都执行
print(train_sizes)  # [ 161  403  806 1209 1612]; 代表了测试的数据的个数
print(train_loss, '\n', train_loss.shape)  # 一堆 -0; (5, 10)
print(test_loss, '\n', test_loss.shape)  # 一堆负数; (5, 10)
##################################################################
## 结果取平均数
# 因为是负数, 所以要取相反数
train_loss_mean = -np.mean(train_loss, axis=1); print(train_loss_mean)  # [-0. -0. -0. -0. -0.]
test_loss_mean = -np.mean(test_loss, axis=1); print(test_loss_mean)  # [ 13.02983078   5.41292631   8.00192675   6.72970955   5.56857195]
plt.plot(train_sizes, train_loss_mean, 'o-', color="r", label="Training")
plt.plot(train_sizes, test_loss_mean, 'o-', color="g", label="Cross-validation")
plt.xlabel("Training examples")
plt.ylabel("Loss")
plt.legend(loc="best")
plt.show()
##################################################################
# 会发现随着 train_sizes 的增加,
# 1. train_loss_mean 误差越来越小, 因为是按照训练数据进行拟合
# 2. test_loss_mean 会波动, 因为随着 train_sizes 的增加, train_loss 拟合的程度会越来越好, 曲线会更加复杂,
#    但 test_loss 的效果不会和 train_sizes 一样越来越好; 自行 Google: over-fitting
