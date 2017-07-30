#!/usr/bin/python3
# coding: utf-8
from sklearn import datasets
from sklearn.linear_model import LinearRegression
##################################################################
## load dataset 的统一格式
loaded_data = datasets.load_boston()  # 加载数据
data_X = loaded_data.data  # 得到数据
data_y = loaded_data.target  # 得到属性
print(len(data_X), len(data_y), data_X.shape, data_y.shape)  # 506, 506, (506, 13), (506,)
print(data_X, '\n', data_y)
##################################################################
## 加载模型 并 进行训练
model = LinearRegression()
model.fit(data_X, data_y)
##################################################################
## 预测数据
print(model.predict(data_X[:4, :]))
print(data_y[:4])  # 预测数据和真实数据有一定的区别

##################################################################
## 下面是自己 生成数据, 并且图像化
import matplotlib.pyplot as plt
X, y = datasets.make_regression(n_samples=5, n_features=1, n_targets=1, noise=10)  # 10 个数据, 1 个特征
print(len(X), len(y), X.shape, y.shape)  # 5, 5, (5, 1), (5,)
print(X)  # [[-0.86958646] [-1.71682126] [-0.6265871 ] [ 0.82419042] [-0.08056284]]
print(y)  # [-36.53755489 -59.18291396 -34.0576309   23.62646674  -0.25897597]
X, y = datasets.make_regression(n_samples=3, n_features=2, n_targets=1, noise=10)  # 10 个数据, 1 个特征
print(len(X), len(y), X.shape, y.shape)  # 3, 3, (3, 2), (3,)
print(X)  # [[ 0.69076872 -1.51310813] [-0.49550397 -0.38044674] [-1.78348976  1.38575244]]
print(y)  # [-39.96334922 -58.77593593 -35.87022518]
X, y = datasets.make_regression(n_samples=3, n_features=1, n_targets=2, noise=10)  # 10 个数据, 1 个特征
print(len(X), len(y), X.shape, y.shape)  # 3, 3, (3, 1), (3, 2)
print(X)  # [[-0.39471974] [ 0.81290018] [-2.06060568]]
print(y)  # [[ -16.04815958  -23.6711522 ] [  12.7321429    50.2537519 ] [   0.87336622 -132.63712312]]
# 总结:
# 1. n_samples 和 n_features 表示 X 的维度
# 2. n_samples 和 n_targets 表示 y 的维度
# 3. n_features 和 n_targets 表示的是维度, 也就是 特征的数量

##################################################################
## 使用 plt 进行绘制
X, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=10)  # 100 个数据, 1 个特征
plt.scatter(X, y)
plt.show()
