#!/usr/bin/python3
# coding: utf-8
import networkx as nx
##################################################################
# Directed graphs; out_edges(), in_degree(), predecessors(), successors(); methods specific to directed edges
# To allow algorithms to work with both classes easily, the directed versions of neighbors() and degree()
# are equivalent to successors() and the sum of in_degree() and out_degree() respectively even though that may feel inconsistent at times.
DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
print(DG.out_degree(1, weight='weight'), DG.degree(1,weight='weight'))  # 0.5, 1.25
print(DG.out_degree(1))  # 1
print(DG.successors(1), DG.neighbors(1))  # [2], [2]
##################################################################
# Convert
# Indeed the tendency to lump directed and undirected graphs together is dangerous.
# If you want to treat a directed graph as undirected for some measurement you should probably convert it using Graph.to_undirected() or with
H = nx.Graph.to_undirected(DG); print(H.nodes())  # [1, 2, 3]
H = nx.Graph(DG) # convert DG to undirected graph
