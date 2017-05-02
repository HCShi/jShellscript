#!/usr/bin/python3
# coding: utf-8
import networkx as nx
##################################################################
# Weighted-Edges, Adjacency_iter, 遍历无向边
FG = nx.Graph()
FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])  # 自动添加 weight 属性
for n, nbrs in FG.adjacency_iter(): print(n, nbrs)
# 1 {2: {'weight': 0.125}, 3: {'weight': 0.75}}
# 2 {1: {'weight': 0.125}, 4: {'weight': 1.2}}
# 3 {1: {'weight': 0.75}, 4: {'weight': 0.375}}
# 4 {2: {'weight': 1.2}, 3: {'weight': 0.375}}
for n, nbrs in FG.adjacency_iter():
    for nbr, eattr in nbrs.items():
        data = eattr['weight']
        if data < 0.5: print('(%d, %d, %.3f)' % (n, nbr, data))
# (1, 2, 0.125), (2, 1, 0.125), (3, 4, 0.375), (4, 3, 0.375)
##################################################################
# edges() 更加简单的实现遍历, 同一个边只遍历一次
for (u, v, d) in FG.edges(data='weight'): print(u, v, d)
# 1 2 0.125; 1 3 0.75; 2 4 1.2; 3 4 0.375
for (u, v, d) in FG.edges(data='weight'):
    if d < 0.5: print('(%d, %d, %.3f)' % (u, v, d))
# (1, 2, 0.125), (3, 4, 0.375)
