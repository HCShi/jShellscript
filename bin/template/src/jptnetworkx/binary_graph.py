#!/usr/bin/python
# coding: utf-8
# 建立二分图与建立普通的图方法比较类似，需要注意的是，
# 边只能在不同类节点之间添加，同类节点之间不要添加边就可以。
# 下面是一个简单的例子
# 本例中用1开头的编号表示项目节点，用2开头的编号表示参与者节点

import networkx as nx
B = nx.Graph()
# 添加一个项目101，它有3个参与者：201,202,203
B.add_edge(101, 201)
B.add_edge(101, 202)
B.add_edge(101, 203)
# 添加一个项目102，它有2个参与者：203,202,2034
B.add_edge(102, 203)
B.add_edge(102, 204)
# 用networkx.is_bipartite()方法可以检测一个图是否是二分图
print nx.is_bipartite(B)
