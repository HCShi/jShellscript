#!/usr/bin/python3
# coding: utf-8
# 部分参考自: [数据可视化 Seaborn ——(第二章)](https://zhuanlan.zhihu.com/p/27971446)
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
np.random.seed(sum(map(ord, 'aesthetics')))  # 好亮眼...
def sinplot(flip=1):  # 优美的函数
    x = np.linspace(0, 14, 100)
    for i in range(1, 7): plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
    plt.show()
##################################################################
## Seaborn 和 Matplotlib 区别
sinplot()  # Matplotlib 直接画出来, 没有背景, 不好看
import seaborn as sns  # 这里的 sns 不能写到上面, 否则直接会添加上背景, 看不到原始的
sinplot()  # 添加 darkgrid 黑色网格(默认), 好看了
##################################################################
## Seaborn 在底层将 matplotlib 参数分成了两个独立的组.
#     第一组设定了美学风格, 第二组则是不同的数据元素, 这样就可以很容易地添加到代码当中了
# 为了控制风格, 使用 axes_style() 和 set_style() 函数.
# 为了绘图, 请使用 plotting_context() 和 set_context() 函数.
# 在这两种情况下, 第一个函数返回一个参数字典, 第二个函数则设置 matplotlib 默认属性.
# 可以简写为: sns.set() 来包含上面两种设置
##################################################################
## axes_style(style=None, rc=None)
# 风格控制: axes_style() and set_style() seaborn默认设置了5 个不同的主题, 适用于不同的应用和人群偏好:
# darkgrid 黑色网格(默认); whitegrid 白色网格; dark 黑色背景; white 白色背景; ticks 加上刻度的白色背景
print(sns.axes_style())  # {'axes.facecolor': 'white', 'axes.edgecolor': '.8', ..., }
# boxplot() 适合用 whitegrid, 此时需要的是数值场景, 用 whitegrid
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
sns.set_style("whitegrid"); sns.boxplot(data=data); plt.show()  # 默认有 (x=None, y=None, hue=None, data=None), 所以 data= 必须写
# 对于一些主要是想提供数据轮廓, 而不是数据值的场景, 这个时候不需要方框可能会更加完美。
sns.set_style("dark"); sinplot()
sns.set_style("ticks"); sinplot()
sns.set_style("white"); sinplot()
# 临时修改风格, 用 with sns.axes_style():
with sns.axes_style("white"): # 背景设置为白的(默认灰色); 必须写到 with 里面, 单独修改用下面的 set_style()
    sns.swarmplot(x="species", y="petal_length", data=iris)
    plt.show()
##################################################################
## set_context(context=None, font_scale=1, rc=None)
# 四种预设, 按相对尺寸的顺序(线条越来越粗), 分别是 paper, notebook, talk, and poster; notebook 的样式是默认的
# context : dict, None, or one of {paper, notebook, talk, poster. A dictionary of parameters or the name of a preconfigured set.
#     The four predefined contexts are "paper", "notebook", "talk" and "poster".
sns.set_context("paper"); sinplot()  # 小
sns.set_context("notebook"); sinplot()  # 较小
sns.set_context("talk"); sinplot()  # 中等
sns.set_context("poster"); sinplot()  # 大, 很好看; 这四个只是控制纸张大小
# font_scale : float, optional;
#     Separate scaling factor to independently scale the size of the font elements.
sns.set_context("poster", font_scale=1)  # 改变字体大小; 数字越大, 字体越大
# rc : dict, optional
#     Parameter mappings to override the values in the preset seaborn context dictionaries.
#     This only updates parameters that are considered part of the context definition.
sns.set_context("poster", rc={"font.size":15, "axes.labelsize":15})  # 15 算是正常大小, 和 font_scale=1 相仿
sns.set_context("poster", font_scale=1, rc={"font.size":8, "axes.labelsize":8})  # 这里的 font.size 和 font_scale 有很神奇的反应...
##################################################################
## despine() Remove the top and right spines from plot(s). 边框控制
# 在很多图中, 我们可能不需要上方和右方坐标轴边框, 这在 matplotlib 中是无法通过参数实现的, 却可以在 seaborn 中通过 despine() 函数轻松实现
ax = sns.boxplot(data=data); sns.despine(ax=ax); plt.show()
# FacetGrid 直接 grid.despine()...
##################################################################
## color_palette(palette=None, n_colors=None, desat=None) Return a list of colors defining a color palette.
color = sns.color_palette()[2]  # palette=None
print(color)  # (0.7686274509803922, 0.3058823529411765, 0.3215686274509804); 粉红色
print(type(sns.color_palette()))  # <class 'seaborn.palettes._ColorPalette'>
print(len(sns.color_palette()))  # 6; 6 种颜色

# deep, muted, bright, pastel, dark, colorblind; 默认有 6 个 palette
print(len(sns.color_palette('pastel')))  # 6; 粉色 palette 中也有 6 个
