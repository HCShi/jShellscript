#!/usr/bin/python
# coding: utf-8

import networkx as nx

G = nx.Graph()
G.add_edge(1, 2, weight=4.7)
# G.add_edges_from([(3, 4), (4, 5)], color='red')
# G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
# G[1][2]['weight'] = 4.7
# G.edge[1][2]['weight'] = 4
print G.edge[1][2]['weight']

# for edge in G.edges():
    # print edge,
    # print edge(data='weight')
