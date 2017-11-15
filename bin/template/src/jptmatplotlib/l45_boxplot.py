#!/usr/bin/python3
# coding: utf-8
# 箱线图, 又称箱形图(boxplot)或盒式图, 不同于一般的折线图、柱状图或饼图等传统图表, 只是数据大小、占比、趋势等等的呈现,
# 其包含一些统计学的均值、分位数、极值等等统计量, 因此, 该图信息量较大, 不仅能够分析不同类别数据平均水平差异(需在箱线图中加入均值点),
# 还能揭示数据间离散程度、异常值、分布差异等等
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.random.seed(2)  # 设置随机种子
##################################################################
## (1) 简单应用
df = pd.DataFrame(np.random.rand(5, 4), columns=['A', 'B', 'C', 'D'])  # 先生成 0-1 之间的 5*4 维度数据, 再装入 4 列 DataFrame 中
df.boxplot()  # 也可用 plot.box()
plt.show()
# A 、 D 数据较集中(大部分在上下四分位箱体内), 但都有异常值,
# C 的离散程度最大(最大值与最小值之间距离), 以均值为中心,
# B 分布都有明显右偏(即较多的值分布在均值的右侧), A 、 C 则有明显左偏.
##################################################################
## (2) 从分析的角度来说, 上面 boxplot 最初始图形已经够用
# 但是在 matplotlib 库下 boxplot 函数中包含 n 多参数, 涉及到对框的颜色及形状、线段线型、均值线、异常点的形状大小等等设置,
# 由于大多并不常用, 用了几个常用参数, 作图如下:
df.boxplot(sym='r*', vert=False, patch_artist=True, meanline=False, showmeans=True)
plt.show()
# sym='r*', 表示异常点的形状; vert=False, 表示横向还是竖向(True); patch_artist=True (上下四分位框内是否填充, True 为填充)
# meanline=False, showmeans=True, 是否有均值线及其形状; meanline=True 时, 均值线也像中位数线一样是条红色线段, 这样容易与中位数线混淆.
# 另外, 还有其他参数, 比如 notch 表示中间箱体是否缺口, whis 为设置数据的范围, showcaps 、 showbox 是否显示边框, 可以参见
# http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.boxplot
##################################################################
## (3) 还可以做子图, 如我们在最开始的 DataFrame 数据中加入分类数据列:
df['E'] = np.random.choice(['X', 'Y'], size=5)  # 加入以 X 、 Y 随机分类的 E 列
print(df)
plt.figure()
df.boxplot(by='E')
plt.show()
# 这样我们就可以比较, 不同类别 X 、Y 在同一列下的数据分布情况及其差异.
