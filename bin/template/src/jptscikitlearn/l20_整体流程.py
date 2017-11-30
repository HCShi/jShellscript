#!/usr/bin/python3
# coding: utf-8
from sklearn import datasets
from sklearn.linear_model import LinearRegression
##################################################################
## 分类
X_train, y_train = datasets.load_iris(True); print(X_train.shape, y_train.shape)  # (150, 4) (150,)

##################################################################
## 回归
X_train, y_train = datasets.load_boston(True); print(X_train.shape, y_train.shape)  # (506, 13) (506,)
## 模型 (建立 训练 预测)
model = LinearRegression()
model.fit(X_train, y_train)
print(model.predict(X_train[:4, :]))  # [ 30.00821269  25.0298606   30.5702317   28.60814055]
print(y_train[:4])  # [ 24.   21.6  34.7  33.4]; 预测数据和真实数据有一定的区别
## 查看参数
print(model.coef_)  # [ -1.07170557e-01   4.63952195e-02   2.08602395e-02   2.68856140e+00 ... -5.25466633e-01]
