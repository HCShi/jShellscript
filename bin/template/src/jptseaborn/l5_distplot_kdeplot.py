#!/usr/bin/python3
# coding: utf-8
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(sum(map(ord, "distributions")))
##################################################################
## seaborn.distplot(a, bins=None, hist=True, kde=True, rug=False, fit=None, hist_kws=None, kde_kws=None, rug_kws=None, fit_kws=None, color=None, vertical=False, norm_hist=False, axlabel=None, label=None, ax=None)
# seaborn 的 displot()集合了 matplotlib 的 hist()与核函数估计 kdeplot 的功能, 增加了 rugplot 分布观测条显示与利用 scipy 库 fit 拟合参数分布的新颖用途
# a: Series, 1d-array, or list.
#    Observed data. If this is a Series object with a name attribute, the name will be used to label the data axis.
# bins: argument for matplotlib hist(), or None, optional  # 设置矩形图数量
# hist: bool, optional                   # 控制是否显示条形图
# kde: bool, optional                    # 控制是否显示核密度估计图
# rug: bool, optional                    # 控制是否显示观测的小细条(边际毛毯)
# fit: random variable object, optional  # 控制拟合的参数分布图形
# An object with fit method, returning a tuple that can be passed to a pdf method a positional arguments following an grid of values to evaluate the pdf on.
# {hist, kde, rug, fit}_kws : dictionaries, optional
# Keyword arguments for underlying plotting functions.
# vertical : bool, optional               # 显示正交控制
#     If True, oberved values are on y-axis.
x = np.random.normal(size=100)
sns.distplot(x); plt.show()
sns.distplot(x, kde=False); plt.show()  # 没有那条拟合的曲线了
sns.distplot(x, rug=True); plt.show()
sns.distplot(x, kde=False, rug=True); plt.show()  # kde=False 关闭核密度分布曲线, rug 表示在 x 轴上每个观测上生成的小细条(边际毛毯)
sns.distplot(x, bins=20, kde=False, rug=True); plt.show()  # 设置了 20 个矩形条

## 四种对比图
rs = np.random.RandomState(10)
d = rs.normal(size=100)  # Generate a random univariate dataset
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.despine(left=True)
sns.distplot(d, kde=False, color="b", ax=axes[0, 0])                            # Plot a simple histogram with binsize determined automatically
sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])                 # Plot a kernel density estimate and rug plot
sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])  # Plot a filled kernel density estimate
sns.distplot(d, color="m", ax=axes[1, 1])                                       # Plot a historgram and kernel density estimate

plt.setp(axes, yticks=[]); plt.tight_layout(); plt.show()
##################################################################
## Kernel density estimaton 核密度估计
# 核密度估计是在概率论中用来估计未知的密度函数, 属于非参数检验方法之一.
# 由于核密度估计方法不利用有关数据分布的先验知识, 对数据分布不附加任何假定, 是一种从数据样本本身出发研究数据分布特征的方法,
# 因而, 在统计学理论和应用领域均受到高度的重视
