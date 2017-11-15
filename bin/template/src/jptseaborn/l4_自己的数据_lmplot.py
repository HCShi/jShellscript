#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
##################################################################
## 自己准备数据
x = np.arange(1, 10); print(x)  # [1 2 3 4 5 6 7 8 9]
y = x * 2; print(y)  # [ 2  4  6  8 10 12 14 16 18]
data = pd.DataFrame(data={'x': x, 'y': y})
##################################################################
## lmplot(x, y, data)
grid = sns.lmplot('x', 'y', data, size=7, truncate=True, scatter_kws={"s": 100})
plt.show()

##################################################################
## lmplot 是一种集合基础绘图与基于数据建立回归模型的绘图方法. 旨在创建一个方便拟合数据集回归模型的绘图方法
## 利用'hue'、'col'、'row'参数来控制绘图变量. 同时可以使用模型参数来调节需要拟合的模型: order 、 logistic 、 lowess 、 robust 、 logx.
## seaborn.lmplot(x, y, data, hue=None, col=None, row=None, palette=None, col_wrap=None, size=5, aspect=1, markers='o', sharex=True, sharey=True, hue_order=None, col_order=None, row_order=None, legend=True, legend_out=True, x_estimator=None, x_bins=None, x_ci='ci', scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None, order=1, logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, truncate=False, x_jitter=None, y_jitter=None, scatter_kws=None, line_kws=None)
# hue, col, row : strings  # 定义数据子集的变量, 并在不同的图像子集中绘制
# size : scalar, optional  # 定义子图的高度
# markers : matplotlib marker code or list of marker codes, optional  # 定义散点的图标
# col_wrap : int, optional  # 设置每行子图数量
# order : int, optional  # 多项式回归, 设定指数
# logistic : bool, optional  # 逻辑回归
# logx : bool, optional  # 转化为 log(x)
tips = sns.load_dataset("tips")  # 载入自带数据集
# 研究小费 tips 与总消费金额 total_bill 在吸烟与不吸烟人之间的关系
g = sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips, palette="Set1"); plt.show()
# 通过回归模型发现 total_bill=20 为分界点, 不吸烟者的小费高于吸烟者
# 研究在不同星期下, 消费总额与消费的回归关系, col|hue 控制子图不同的变量 day, col_wrap 控制每行子图数量, size 控制子图高度
g = sns.lmplot(x="total_bill", y="tip", col="day", hue="day",data=tips, col_wrap=2, size=3); plt.show()
