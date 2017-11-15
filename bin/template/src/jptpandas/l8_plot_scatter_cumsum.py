#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import numpy as np  # 使用 numpy 生成一些数据
import matplotlib.pyplot as plt  # 使用的 matplotlib 仅仅是用来 show 图片的, 即 plt.show()
##################################################################
## Series 随机生成 1000 个数据, Series 默认的 index 就是从 0 开始的整数, 这里显式赋值看的更清楚
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()  # 为了方便观看效果, 我们累加这个数据; 功能就是将前面的数据进行累加并且替换
data.plot()  #  pandas 数据可以直接观看其可视化形式
plt.show()  # 只有这一句话是用到了 matplotlib
# 如果需要 plot 一个数据, 我们可以使用 plt.plot(x=, y=), 把 x, y 的数据作为参数存进去
# 但是 data 本来就是一个数据, 所以我们可以直接 plot
##################################################################
## DataFrame
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))  # header 就是 ABCD
data = data.cumsum(); print(data)
data.plot(); plt.show()  # 有 4 组数据, 所以 4 组数据会分别 plot 出来
##################################################################
## hist()
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
data.plot(bins=50, kind='hist'); plt.show()  # 所有挤在一块
data['A'].plot(bins=50, kind='hist'); plt.show()  # plot() 不支持 column 参数

data.hist(column='A', bins=50, figsize=(10, 4)); plt.show()
data.hist(column=['A', 'B'], bins=50, figsize=(10, 4)); plt.show()  # 分成两个图
data = pd.DataFrame(np.random.randn(10, 4), index=np.arange(10), columns=list("ABCD"))
data.hist(column='A', by='B', bins=50, figsize=(10, 4)); plt.show()  # 按照 B 来分类, 每一类在按 A 来画图
# bins: integer, default 10; Number of histogram bins to be used; 画多少个 hist 柱子
##################################################################
## scatter 散点图 (plot methods: 'bar', 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie')
# scatter 只有 x, y 两个属性, 我们我们就可以分别给 x, y 指定数据
# 然后我们在可以再画一个在同一个 ax 上面, 选择不一样的数据列, 不同的 color 和 label
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label="Class 1")
data.plot.scatter(x='A', y='C', color='LightGreen', label='Class 2', ax=ax); plt.show()
