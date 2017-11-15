#!/usr/bin/python3
# coding: utf-8
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# As for Seaborn, you have two types of functions: axes-level functions and figure-level functions.
# The ones that operate on the Axes level are, for example, regplot(), boxplot(), kdeplot(), swarmplot(), ...
# while the functions that operate on the Figure level are lmplot(), factorplot(), jointplot() and a couple others.
# 数据分布的可视化:
#     简单的单变量分布可以使用 matplotlib 的 hist() 函数绘制直方图, 双变量可以使用 sns.jointplot() 函数绘制六边形箱图阵
#     如果需要更进一步的描述数据分布, 可以使用地毯图(rug plot)和核密度估计图(Kernel Density Estimate plot, KDE plot).
#     Seaborn 的 KDE 图默认使用的是高斯核函数.
# 定量数据的线性模型绘图:
#     线性模型用于理解激励(自变量)与响应(因变量)之间的线性关系. 下面以介绍 lmplot() 函数的使用为主.
#     lmplot() 函数的数据参数使用 Pandas 的 DataFrame 类型, 并且需要提供激励和响应变量的在 DataFrame 中的 name.
# Data-aware 网格绘图:
#     多维数据需要将数据分为子集依次画图, 这种绘图称为 lattice(或者 trellis) 绘图. Seaborn 基于 matplotlib 提供绘制多维数据的函数.
#     Seaborn 的接口要求使用 Pandas 的 DataFrame 作为数据参数, 并且必须是结构化的数据 (tidy data), 每一行为一个观测, 每一列为一个变量.
#     FacetGrid 类能够方便的绘制这类图像. FacetGrid 对象有三个维度： row,col 和 hue. 下面是几个例子.
##################################################################
## 一: Axes
##################################################################
## 准备数据
iris = sns.load_dataset("iris")  # Load iris data
ax = sns.swarmplot(x="species", y="petal_length", data=iris)  # Construct iris plot
print(type(ax))  # <class 'matplotlib.axes._subplots.AxesSubplot'>

x = np.random.normal(size=100)
ax = sns.distplot(x);
print(type(ax))  # <class 'matplotlib.axes._subplots.AxesSubplot'>

data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
ax = sns.boxplot(data=data)  # 默认有 (x=None, y=None, hue=None, data=None), 所以 data= 必须写
print(type(ax))  # <class 'matplotlib.axes._subplots.AxesSubplot'>
## 准备结束
##################################################################
## set(), set_*()
ax.set_title('Hello')  # 设置 Title
ax.set_ylim(1, 10)  # 设置坐标范围
# ax.set(xscale="log", yscale="log")  # 对 x, y = 10 ** np.arange(1, 10), x * 2 这种好用
# set_xticklabels(labels, **kwargs): Set the xtick labels with list of strings *labels*
print(list(set(iris.species.values)))  # ['virginica', 'versicolor', 'setosa']
ax.set_xticklabels('abc', rotation=30)  # labels 参数必须显示指定...; 标签对不上怎么办...
# set() 和 set_*(): 前者可以包含后者, 将其作为参数
ax.set(ylim=(1, 10))

plt.show()
##################################################################
## 二: FacetGrid 可以从中提取 grid.data, 有是一个 DataFrame
##################################################################
## 准备数据
titanic = sns.load_dataset("titanic")  # class: category; survived
print(titanic[['class', 'survived', 'sex']].values)  # [['Third' 0 'male'], ...]
grid = sns.factorplot("class", "survived", "sex", data=titanic)  # 有 legend 反而不好看
print(type(grid))  # <class 'seaborn.axisgrid.FacetGrid'>
print(grid.data.shape)  # (891, 15); 虽然只取了 三个属性分析, 但是其他属性还在...

tips = sns.load_dataset("tips")
print(tips[['total_bill', 'tip']].values)  # [[ 12.74   2.01], ...]
grid = sns.jointplot("total_bill", "tip", data=tips, kind="reg")
print(type(gird))  # <class 'seaborn.axisgrid.FacetGrid'>

x = np.arange(1, 10); y = x * 2
data = pd.DataFrame(data={'x': x, 'y': y})
grid = sns.lmplot('x', 'y', data)
print(type(grid))  # <class 'seaborn.axisgrid.FacetGrid'>
## 准备结束
##################################################################
ax = grid.ax  # 和上面的 ax 一毛一样
print(type(ax))  # <class 'matplotlib.axes._subplots.AxesSubplot'>
fig = grid.fig; print(type(fig))  # <class 'matplotlib.figure.Figure'>
data = grid.data; print(type(data))  # <class 'pandas.core.frame.DataFrame'>

grid.despine()  # Remove axis spines from the facets; 这么好用的方法 ax 没有, 只能通过 sns.despine(ax=ax)
##################################################################
## ax, set(), ax().set_()
# 设置标题
ax.set_title('World')  # 这个可以, 下面那行没找到
grid.set_titles('Hello World')  # Draw titles either above each facet or on the grid margins.; 没看到...
grid.set_xticklabels(rotation=30)  # 这个就不需要指定 labels, 比上面的好
# 下面两行效果一样
grid.set(xlim=(0, 20))  # 这里
grid.ax.set(xlim=(0, 20))  # 这里

plt.show()
