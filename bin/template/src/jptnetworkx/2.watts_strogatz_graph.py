#!/usr/bin/python
# coding: utf-8

# 在NetworkX中，可以用random_graphs.watts_strogatz_graph(n, k, p)方法
# 生成一个含有n个节点、每个节点有k个邻居、以概率p随机化重连边的WS小世界网络，下面是一个例子：

import networkx as nx
import matplotlib.pyplot as plt
WS = nx.random_graphs.watts_strogatz_graph(20, 4, 0.3)
# 生成包含20个节点、每个节点4个近邻、随机化重连概率为0.3的小世界网络
pos = nx.circular_layout(WS)  # 定义一个布局，此处采用了circular布局方式
nx.draw(WS, pos, with_labels=False, node_size=30)  # 绘制图形
plt.show()
