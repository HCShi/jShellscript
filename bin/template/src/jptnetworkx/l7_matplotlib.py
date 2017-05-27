#!/usr/bin/python3
# coding: utf-8
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph(); G.add_edges_from([(1, 2), (1, 3)]); G.add_node("spam")  # Graph Initial
nx.draw(G, nx.spring_layout(G), with_labels=True, node_size=500)
nx.draw_random(G)
nx.draw_circular(G)
nx.draw_spectral(G)
plt.show()  # 自己的代码里只有这里有 plt, nx.draw 中以及处理好了
