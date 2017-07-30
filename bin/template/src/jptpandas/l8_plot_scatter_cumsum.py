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
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
data = data.cumsum()
data.plot(); plt.show()  # 有4组数据, 所以4组数据会分别plot出来
##################################################################
## scatter 散点图 (plot methods: 'bar', 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie')
# scatter 只有 x, y 两个属性, 我们我们就可以分别给 x, y 指定数据
# 然后我们在可以再画一个在同一个 ax 上面, 选择不一样的数据列, 不同的 color 和 label
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label="Class 1")
data.plot.scatter(x='A', y='C', color='LightGreen', label='Class 2', ax=ax)
plt.show()
