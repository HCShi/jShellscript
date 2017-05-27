#!/usr/bin/python3
# coding: utf-8
# 这里只是自己用到过的, 详细 API 见下面链接
# http://networkx.readthedocs.io/en/stable/reference/algorithms.shortest_paths.html
import networkx as nx
##################################################################
## path_graph(n, create_using=None) Return the Path graph P_n of n nodes linearly connected by n-1 edges.
# Node labels are the integers 0 to n - 1. If create_using is a DiGraph then the edges are directed in increasing order.
G = nx.path_graph(5);
print(G.nodes(), G.edges())  # [0, 1, 2, 3, 4] [(0, 1), (1, 2), (2, 3), (3, 4)]
##################################################################
## all_pairs_shortest_path(G[, cutoff])  # Compute shortest paths between all nodes. 针对没有权重的 G
# G (NetworkX graph); cutoff (integer, optional) – Depth at which to stop the search. Only paths of length at most cutoff are returned.
# Returns: Dictionary, keyed by source and target, of shortest paths.
path = nx.all_pairs_shortest_path(G); print(path[0][4])  # [0, 1, 2, 3, 4]
print(path)
# {0: {0: [0], 1: [0, 1], 2: [0, 1, 2], 3: [0, 1, 2, 3], 4: [0, 1, 2, 3, 4]},
#  1: {1: [1], 0: [1, 0], 2: [1, 2],    3: [1, 2, 3],    4: [1, 2, 3, 4]},
#  2: {2: [2], 1: [2, 1], 3: [2, 3],    0: [2, 1, 0],    4: [2, 3, 4]},
#  3: {3: [3], 2: [3, 2], 4: [3, 4],    1: [3, 2, 1],    0: [3, 2, 1, 0]},
#  4: {4: [4], 3: [4, 3], 2: [4, 3, 2], 1: [4, 3, 2, 1], 0: [4, 3, 2, 1, 0]}}
##################################################################
## dijkstra_path(G, source, target[, weight])  # Returns the shortest path from source to target in a weighted graph G.
# G(NetworkX graph); source(node) – Starting node; target(node) – Ending node; weight(string, optional (default='weight'))
# Returns: path – List of nodes in a shortest path.
print(nx.dijkstra_path(G, 0, 4))  # [0, 1, 2, 3, 4]
