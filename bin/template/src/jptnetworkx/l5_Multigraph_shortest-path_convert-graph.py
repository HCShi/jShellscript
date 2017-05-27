#!/usr/bin/python3
# coding: utf-8
import networkx as nx
##################################################################
# Multigraphs; allow multiple edges between any pair of nodes
# but many algorithms are not well defined on such graphs. Shortest path is one example.
MG = nx.MultiGraph()
MG.add_weighted_edges_from([(1, 2, .5), (1, 2, .75), (2, 3, .5)])
print(MG.degree(weight='weight'))  # {1: 1.25, 2: 1.75, 3: 0.5}
print(MG.edges())  # [(1, 2), (1, 2), (2, 3)]
print(nx.shortest_path(MG, 1, 3))  # [1, 2, 3]
##################################################################
# Convert; you should convert to a standard graph in a way that makes the measurement well defined
GG = nx.Graph()
for n, nbrs in MG.adjacency_iter(): print(n, nbrs)
# 1 {2: {0: {'weight': 0.5}, 1: {'weight': 0.75}}}
# 2 {1: {0: {'weight': 0.5}, 1: {'weight': 0.75}}, 3: {0: {'weight': 0.5}}}
# 3 {2: {0: {'weight': 0.5}}}
for n, nbrs in MG.adjacency_iter():  # 将 MultiGraph 转化为 Graph
   for nbr, edict in nbrs.items():
       minvalue = min([d['weight'] for d in edict.values()])
       GG.add_edge(n, nbr, weight=minvalue)
print(GG.edges())  # [(1, 2), (2, 3)]
print(nx.shortest_path(GG, 1, 3))  # [1, 2, 3]
