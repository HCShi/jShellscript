#!/usr/bin/python
# coding: utf-8
import networkx as nx

# 有向图 & 无向图
# G = nx.Graph()  # 建立一个空的无向图G
G = nx.DiGraph()  # 建立一个空的有向图G
G.add_node(1)  # 添加一个节点1
G.add_edge(2, 3)  # 添加一条边2-3（隐含着添加了两个节点2、3）
G.add_edge(3, 2)  # 对于无向图，边3-2与边2-3被认为是一条边
print G.nodes()  # 输出全部的节点： [1, 2, 3]
print G.edges()  # 无向图输出全部的边：[(2, 3)]
print G.number_of_edges()  # 输出边的数量：1
print

# 加权图
G.add_weighted_edges_from([(0, 1, 3.0), (1, 2, 7.5)])  # 添加两边,权重3.0和7.5
print G.nodes()
print G.edges()
print G.number_of_edges()
print G.get_edge_data(1, 2)  # 输出{'weight': 7.5} 即该边的权值
print

# 最短路径
path = nx.all_pairs_shortest_path(G)  # 调用多源最短路径算法，计算图G所有节点间的最短路径
print path[0][2]  # 输出节点0、2之间的最短路径序列： [0, 1, 2]
