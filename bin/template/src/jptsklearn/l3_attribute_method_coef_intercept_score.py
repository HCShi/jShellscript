#!/usr/bin/python3
# coding: utf-8
from sklearn import datasets
from sklearn.linear_model import LinearRegression
##################################################################
## 加载数据
loaded_data = datasets.load_boston(); print(loaded_data)
data_X = loaded_data.data
data_y = loaded_data.target
##################################################################
## 加载 Model
model = LinearRegression()
model.fit(data_X, data_y)
##################################################################
## Model attribute && method
# 下面的要在 Model fit() 结束以后执行
print(model.predict(data_X[:4, :]))
print(model.coef_)  # 系数, 很多; y = 0.1x + 0.3 中的 0.1
print(model.intercept_)  # 常数; 和 y 轴的交点
print(model.get_params())  # LinearRegression() 定义的参数
print(model.score(data_X, data_y))  # R^2 coefficient of determination; 使用参数进行打分
