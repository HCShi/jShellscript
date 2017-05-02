#!/usr/bin/python3
# coding: utf-8
import networkx as nx
G = nx.Graph()  # 建立一个空的无向图 G
##################################################################
# Node, node can be any hashable object
G.add_node(1)             # 添加一个节点 1
G.add_nodes_from([2, 3])  # 可以是任何可迭代的参数
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
##################################################################
# Edge
G.add_edge(4, 5)                    # 添加一条边 4-5 (隐含着添加了两个节点 4, 5)
e = (2, 3); G.add_edge(*e)          # unpack edge tuple*
G.add_edges_from([(1, 2), (1, 3)])  # 参数可迭代
##################################################################
# Info
print(G.nodes())  # [1, 2, 3, 4, 5, 'spam', 's', 'p', 'a', 'm']; 全部节点
print(G.edges())  # [(1, 2), (1, 3), (2, 3), (4, 5)]; 全部边
print(G.number_of_nodes(), G.number_of_edges())  # 10, 4
print(G.neighbors(1))  # [2, 3]
##################################################################
# Remove
G.remove_nodes_from("spam"); print(G.nodes())  # [1, 2, 3, 4, 5, 'spam']
G.remove_edge(1,3); print(G.edges());  # [(1, 2), (2, 3), (4, 5)]
##################################################################
# Access
print(G[1], G[2])  # {2: {}} {3: {}, 1: {}}
G[1][2]['color'] = 'blue'; print(G[1], G[1][2], G[1][2]['color'])  # {2: {'color': 'blue'}} {'color': 'blue'} blue
##################################################################
# Clear
G.clear()  # removing all nodes and edges
