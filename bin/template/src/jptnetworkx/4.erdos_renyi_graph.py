#!/usr/bin/python
# coding: utf-8
# ER随机图是早期研究得比较多的一类“复杂”网络，这个模型的基本思想是以概率p连接N个节点中的每一对节点。在NetworkX中，可以用random_graphs.erdos_renyi_graph(n,p)方法生成一个含有n个节点、以概率p连接的ER随机图：

import networkx as nx
import matplotlib.pyplot as plt
ER = nx.random_graphs.erdos_renyi_graph(20, 0.2)  # 生成包含20个节点、以概率0.2连接的随机图
pos = nx.shell_layout(ER)  # 定义一个布局，此处采用了shell布局方式
nx.draw(ER, pos, with_labels=False, node_size=30)
plt.show()
