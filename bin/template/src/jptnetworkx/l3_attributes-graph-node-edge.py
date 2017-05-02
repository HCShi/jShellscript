#!/usr/bin/python3
# coding: utf-8
import networkx as nx
##################################################################
# Graph attributes
G = nx.Graph(day="Friday"); print(G.graph)  # {'day': 'Friday'}; 构造时候添加
G.graph['day']='Monday'; print(G.graph)  # {'day': 'Monday'}; 后来修改
##################################################################
# Node attributes; add_node(), add_nodes_from() or G.node
G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm'); print(G.node[1])  # {'time': '5pm'}; 构造时候添加
G.node[1]['room'] = 714  # 后来修改
print(G.nodes(data=True))  # [(1, {'room': 714, 'time': '5pm'}), (3, {'time': '2pm'})]
print(G.nodes(), G.node[1])  # [1, 3], {'time': '5pm', 'room': 714}
# Note that adding a node to G.node does not add it to the graph, use G.add_node() to add new nodes.
##################################################################
# Edge Attributes; add_edge(), add_edges_from(), subscript notation, or G.edge.
G.add_edge(1, 2, weight=4.7 )
G.add_edges_from([(3, 4), (4, 5)], color='red')  # 下面是分开添加
G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])  # 构造时候添加
G[1][2]['weight'] = 4.7; G.edge[1][2]['weight'] = 4  # 后来修改
print(G.edges(), G.edges(data=True))  # [(1, 2), (3, 4), (3, 2), (4, 5)],
# [(1, 2, {'weight': 4, 'color': 'blue'}), (3, 4, {'color': 'red'}), (3, 2, {'weight': 8}), (4, 5, {'color': 'red'})]
# The special attribute ‘weight’ should be numeric and holds values used by algorithms requiring weighted edges.
