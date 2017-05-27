#!/usr/bin/python3
# coding: utf-8
import networkx as nx
##################################################################
# Analyzing graph
G = nx.Graph(); G.add_edges_from([(1, 2), (1, 3)]); G.add_node("spam")  # Graph Initial
nx.connected_components(G)
print(nx.degree(G), G.degree())  # {1: 2, 2: 1, 3: 1, 'spam': 0}; 两种写法一样
print(sorted(nx.degree(G).values()))  # [0, 1, 1, 2]
print(nx.clustering(G))  # {1: 0.0, 2: 0.0, 3: 0.0, 'spam': 0.0}
print(nx.degree(G, 1), G.degree(1))  # 2, 2; a single value is returned for a single node
print(G.degree([1, 2]))  # {1: 2, 2: 1}; dict returned for nbunch
