#!/usr/bin/python3
# coding: utf-8
#          1
#         /|\
#        / | \
#       2  3  4
#      /|     |\
#     / |     | \
#    5  6     7  8
#   /|        |\
#  / |        | \
# 9  10       11 12
graph = {  # graph is in adjacent list representation
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '5': ['9', '10'],
    '4': ['7', '8'],
    '7': ['11', '12']
}
##################################################################
## 寻找路径
# 其实直接从 graph 中往上直接找就行了
#################################
## BFS: Breadth-First Search
def bfs(graph, start, end):
    queue = [start]  # maintain a queue of paths, and push the first path into the queue
    while queue:  # Not null
        path = queue.pop(0)  # get the first path from the queue
        node = path[-1]  # get the last node from the path
        if node == end: return path  # path found
        for adjacent in graph.get(node, []):  # enumerate all adjacent nodes, construct a new path and push it into the queue
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)  # 这里是加一整个 list, 虽然很麻烦, 但最后输出路径的时候方便
print(bfs(graph, '1', '11'))  # ['1', '4', '7', '11']
##################################################################
## 遍历
# 这个才是重要的
#################################
## BFS
def bfs(graph, root):
    vis, queue = set(root), [root]  # ACM 比赛的时候 vis 习惯开一个 M 的 0/1 数组
    while queue:
        vertex = queue.pop(0)  # 左侧第一个
        print(vertex)
        for neighbour in graph.get(vertex, []):  # for neighbour, val in enumerate(self.graph[u]): 用矩阵形式存储的时候...
            if neighbour not in vis:
                vis.add(neighbour)
                queue.append(neighbour)
bfs(graph, '1')
