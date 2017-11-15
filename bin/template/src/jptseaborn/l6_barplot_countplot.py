#!/usr/bin/python3
# coding: utf-8
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(sum(map(ord, "distributions")))
##################################################################
## barplot() 利用矩阵条的高度反映数值变量的集中趋势, 以及使用 errorbar 功能（差棒图）来估计变量之间的差值统计.
# 请谨记 bar plot 展示的是某种变量分布的平均值, 当需要精确观察每类变量的分布趋势, boxplot 与 violinplot 往往是更好的选择.
## seaborn.barplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None,ci=95, n_boot=1000, units=None, orient=None, color=None, palette=None, saturation=0.75, errcolor='.26', errwidth=None, capsize=None, ax=None, estimator=<function mean>, **kwargs)
# x, y, hue : names of variables in data or vector data, optional  # 设置 x, y 以及颜色控制的变量
# data : DataFrame, array, or list of arrays, optional  # 设置输入的数据集
# order, hue_order : lists of strings, optional  # 控制变量绘图的顺序
# estimator : callable that maps vector -> scalar, optional  # 设置对每类变量的计算函数, 默认为平均值, 可修改为 max 、 median 、 max 等
# Statistical function to estimate within each categorical bin.
# ax : matplotlib Axes, optional  # 设置子图位置, 将在下节介绍绘图基础
# orient : " v " | " h ", optional  # 控制绘图的方向, 水平或者竖直
# capsize : float, optional  # 设置误差棒帽条的宽度
# Width of the "caps" on error bars
tips = sns.load_dataset("tips")  # 载入自带数据集
# x 轴为分类变量 day, y 轴为数值变量 total_bill, 利用颜色再对 sex 分类
ax = sns.barplot("day", "total_bill", "sex", data=tips); plt.show()
from numpy import median
ax = sns.barplot("day", "tip", data=tips, estimator=median); plt.show()  # 设置中位数为计算函数, 注意 y 轴已显示为 median
##################################################################
## countplot 故名思意, 计数图, 可将它认为一种应用到分类变量的直方图, 也可认为它是用以比较类别间计数差, 调用 count 函数的 barplot.
## seaborn.countplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, ax=None, **kwargs)
# x, y, hue : names of variables in data or vector data, optional
# data : DataFrame, array, or list of arrays, optional
# order, hue_order : lists of strings, optional  # 设置顺序
# orient : "v" | "h", optional  # 设置水平或者垂直显示
# ax : matplotlib Axes, optional  # 设置子图位置, 将在下节介绍绘图基础
titanic = sns.load_dataset("titanic")  # titanic 经典数据集, 带有登船人员的信息
# 源数据集 class 代表三等舱位, who 代表人员分类, 男女小孩, 对每一类人数计数
ax = sns.countplot(x="class", hue="who", data=titanic); plt.show()
