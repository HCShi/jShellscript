#!/usr/bin/python
# coding: utf-8

# 在NetworkX中，可以用random_graphs.barabasi_albert_graph(n, m)方法
# 生成一个含有n个节点、每次加入m条边的BA无标度网络，下面是一个例子：

import networkx as nx
import matplotlib.pyplot as plt
BA = nx.random_graphs.barabasi_albert_graph(20, 1)  # 生成n=20、m=1的BA无标度网络
pos = nx.spring_layout(BA)  # 定义一个布局，此处采用了spring布局方式
nx.draw(BA, pos, with_labels=False, node_size=30)  # 绘制图形
nx.draw(BA)  # 两个会画到一个图里
plt.savefig("jrp.png")
plt.show()
