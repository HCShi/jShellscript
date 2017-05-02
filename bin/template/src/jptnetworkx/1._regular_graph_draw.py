#!/usr/bin/python
# coding: utf-8
import networkx as nx
import matplotlib.pyplot as plt
##################################################################
# random_graphs.random_regular_graph(d, n)方法可以生成一个含有 n 个节点, 每个节点有 d 个邻居节点的规则图
RG = nx.random_graphs.random_regular_graph(3, 20)  # 生成包含 20 个节点、每个节点有 3 个邻居的规则图 RG
pos = nx.spectral_layout(RG)  # 定义一个布局, 此处采用了 spectral 布局方式, 后变还会介绍其它布局方式, 注意图形上的区别
# 绘制规则图的图形, with_labels决定节点是非带标签（编号）, node_size是节点的直径
nx.draw(RG, pos, with_labels=False, node_size=30)
plt.show()  # 显示图形
