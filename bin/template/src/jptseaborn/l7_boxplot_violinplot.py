#!/usr/bin/python3
# coding: utf-8
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(sum(map(ord, "distributions")))
##################################################################
## "盒式图"或叫"盒须图" "箱形图", 其绘制须使用常用的统计量, 能提供有关数据位置和分散情况的关键信息, 尤其在比较不同的母体数据时更可表现其差异
## 主要包含五个数据节点, 将一组数据从大到小排列, 分别计算出他的上边缘, 上四分位数, 中位数, 下四分位数, 下边缘
## seaborn.boxplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, width=0.8, fliersize=5, linewidth=None, whis=1.5, notch=False, ax=None, **kwargs)
# x, y, hue : names of variables in data or vector data, optional  # 设置 x, y 以及颜色控制的变量
# data : DataFrame, array, or list of arrays, optional  # 设置输入的数据集
# order, hue_order : lists of strings, optional  # 控制变量绘图的顺序
tips = sns.load_dataset("tips")  # 载入自带数据集
# 研究三个变量之间的关系, 是否抽烟与日期为分类变量, 消费是连续变量; 结论发现吸烟者在周末消费明显大于不吸烟的人
ax = sns.boxplot("day", "total_bill", "smoker", data=tips, palette="Set3"); plt.show()
##################################################################
## Violinplot 结合了箱线图与核密度估计图的特点, 它表征了在一个或多个分类变量情况下, 连续变量数据的分布并进行了比较, 它是一种观察多个数据分布有效方法
## seaborn.violinplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, bw='scott', cut=2, scale='area', scale_hue=True, gridsize=100, width=0.8, inner='box', split=False, orient=None, linewidth=None, color=None, palette=None, saturation=0.75, ax=None, **kwargs)
# split : bool, optional  # 琴形图是否从中间分开两部分
#     When using hue nesting with a variable that takes two levels, setting split to True will draw half of a violin for each level. This can make it easier to directly compare the distributions.
# scale : {"area", "count", "width"}, optional  # 用于调整琴形图的宽带, area ——每个琴图拥有相同的面域; count ——根据样本数量来调节宽度; width ——每个琴图则拥有相同的宽度
# inner : {"box", "quartile", "point", "stick", None}, optional  # 控制琴图内部数据点的形态, box ——绘制微型 boxplot; quartiles ——绘制四分位的分布; point/stick ——绘制点或小竖条
# Representation of the datapoints in the violin interior. If box, draw a miniature boxplot. If quartiles, draw the quartiles of the distribution. If point or stick, show each underlying datapoint. Using None will draw unadorned violins.
# 以速度为 y 轴, 世代为 x 轴区分"传奇",来绘制攻击能力的分布图
# 由于传奇系很稀少, scale 选择 width, 保持两边宽度相同, inder 选择 stick 加入分布竖条
