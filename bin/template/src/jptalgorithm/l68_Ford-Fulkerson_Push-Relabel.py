#!/usr/bin/python3
# coding: utf-8
# + 是边的起点
import pprint
import numpy as np
##################################################################
## 原始图:                            最大流: 最终结果为 23
#           12                               12
#      1+-------->3                     1+-------->3
#     /+^        /^+                   /^          ^+
# 16 / ||       / | \20            11 / |          | \19
#   /  ||4     /  |  \               /  |          |  \
#  +   ||   9 /   |   \             +   |          |   \
# 0  10||    /    |7   5           0    |1         |7   5
#  +   ||   /     |   /             +   |          |   /
# 13\  ||  /      |  /             12\  |          |  /
#    \ || /       | /4                \ |          | /4
#     \v++        ++                   \+          ++
#      2+-------->4                     2+-------->4
#           14                               11
graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]
##################################################################
## 一: Ford Fulkerson
class Graph:  # 虽然很不喜欢 class, 但这里确实比较方便
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)
    def BFS(self, s, t, parent):  # Returns true if there is a path from source 's' to sink 't' in residual graph. Also fills parent[] to store the path
        vis, queue = {s}, [s]  # Mark all the vertices as not visited
        while queue:
            u = queue.pop(0)  # Dequeue a vertex from queue
            for ind, val in enumerate(self.graph[u]):  # 这里的 ind 是刚好表示 ID
                if ind not in vis and val > 0 :
                    vis.add(ind)
                    queue.append(ind)
                    parent[ind] = u  # 存储每次找到的路径, FordFulkerson() 会用
        return True if t in vis else False
    def FordFulkerson(self, source, sink):  # Returns tne maximum flow from s to t in the given graph
        parent = [-1] * (self.ROW)  # This array is filled by BFS and to store path
        max_flow = 0  # There is no flow initially
        while self.BFS(source, sink, parent):  # 每执行一次 BFS, parent 中就会存一次从 s -> t 的路径
            path_flow = float("Inf")
            s = sink
            while(s != source):  # Find minimum residual capacity of the edges along the path filled by BFS. Or we can say find the maximum flow through the path found.
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]  # 这里的循环很不和谐, 下一步用函数式改写
            # 上面的循环不能和下面的合并, 因为要先找到瓶颈 path_flow
            max_flow += path_flow  # Add path flow to overall flow
            v = sink
            while(v != source):  # update residual capacities of the edges and reverse edges along the path
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow
#################################
## 测试 graph 矩阵
g = Graph(graph)
print("The maximum possible flow is %d " % g.FordFulkerson(0, 5))
#################################
## 测试 算法作业数据集
# For each data set, the first line has two number N and M, which means the number of jobs and the number of computers.
# Next N line, each line for a job, has two number which means the two computers.
raw = "4 2\n 1 2\n 1 2\n 1 2\n 1 2"  # file = open(problem1.data).read()
jobs, computers = [int(x) for x in raw.split('\n')[0].split()]
# 构造 graph; 好不美观啊...
graph = np.zeros((jobs + computers + 2, jobs + computers + 2), dtype=np.int); pprint.pprint(graph)
for i in range(jobs): graph[0][i + 1] = 1  # s 到 jobs 边填充 1; 单向的
for idx, line in enumerate(raw.split('\n')[1:]):  # 这里以后也要用函数式写出来
    print(idx, line)
    for computer_id in [int(x) for x in line.split()]:
        graph[idx + 1][jobs + computer_id] = 1  # 单向, 从 jobs 到 computers
# 二分法查找
L, R = jobs // computers, jobs; print(L, R)
while L < R:
    tmp = graph.copy()
    k = (L + R) // 2; print(k)
    tmp[jobs + 1:-1, -1] = k
    pprint.pprint(tmp)
    flow = Graph(tmp).FordFulkerson(0, jobs + computers + 1)
    if flow == jobs: R = k
    else: L = k
print('The min-max load is', k)
print("The maximum possible flow is %d " % flow)

##################################################################
## 二: Push Relabel
## 这里没用 class; 但还是用 class 方便
def push(Gf, height, excess_flow, u):
    if excess_flow[u] <= 0: return False
    for v in range(len(Gf)):
        if v != u and Gf[u][v] > 0 and height[u] == height[v] + 1:
            df = min(excess_flow[u], Gf[u][v])
            Gf[u][v] -= df
            Gf[v][u] += df
            excess_flow[u] -= df
            excess_flow[v] += df
            return True
    return False
def relabel(Gf, height, excess_flow, u):
    if excess_flow[u] <= 0: return False
    min_h = np.inf
    for v in range(len(Gf)):
        if v != u and Gf[u][v] > 0:
            if height[u] > height[v]: return False
            else: min_h = min(min_h, height[v])
    height[u] = min_h + 1
    return True
def initialize_preflow(G, s):
    n = len(G)
    height = [0] * n
    excess_flow = [0] * n
    height[s] = n
    for v in range(n):  # 将 excess_flow 中与 s 紧邻的进行初始化
        if v != s and G[s][v] != 0:  # 写的不好...
            excess_flow[v] = G[s][v]
            excess_flow[s] -= G[s][v]
            G[v][s] = G[s][v]
            G[s][v] = 0
    return G, height, excess_flow
def push_relabel(G, s, t):  # 算法实现主体
    n = len(G)
    Gf, height, excess_flow = initialize_preflow(G, s)
    while True:
        push_or_relabel = False
        for u in range(n):
            if u != s and u != t:
                if push(Gf, height, excess_flow, u):
                    push_or_relabel = True
                    break
                if relabel(Gf, height, excess_flow, u):
                    push_or_relabel = True
                    break
        if not push_or_relabel: break
        # else: print(Gf)
    max_flow = 0
    for j in range(n): max_flow += Gf[j][s]
    return max_flow
#################################
## 卜东波 老师作业 Network Flow 第二题
# For each data set, the first line has two number M and N, which means the matrix is M*N.
# Next 2 line, the first line has M number, which indicate the sum of rows and the second line means the sum of columns.
# 10 10
# 5 5 7 7 6 3 5 7 7 3
# 6 6 7 4 5 6 6 4 4 7
## 数据预处理
raw = '10 10\n 5 5 7 7 6 3 5 7 7 3\n 6 6 7 4 5 6 6 4 4 7'  # raw = open('problem2.data').read()
row, col = [int(x) for x in raw.split('\n')[0].split()]; print(row, col)
graph = np.zeros((row + col + 2, row + col + 2), dtype=np.int)
print(graph.shape)  # (22, 22)
for idx, value in enumerate(raw.split('\n')[1].split()): graph[0][idx + 1] = value
for idx, value in enumerate(raw.split('\n')[2].split()): graph[row + idx + 1][-1] = value
# 二分图之间全连接, 对角连接
graph[1:-1, 1:-1][:row, -col:] = 1
# graph[1:-1, 1:-1][row:, :-col] = 1
pprint.pprint(graph)

## 用 Flow Fulkerson 进行验证
tmp = graph.copy()
flow = Graph(tmp).FordFulkerson(0, row + col + 1)
print(flow)  # 55

## 用 Push Relabel 运行
tmp = graph.copy()
max_flow = push_relabel(tmp, 0, row + col + 1)
pprint.pprint(tmp)
matrix = tmp[row+1:-1, 1:row+1].T  # tmp 右上角为剩余网络, 左下角为反向网络, 所以取左下角的转置
print(matrix)
# [[1 0 0 0 0 0 1 1 1 1]
#  [1 0 0 0 0 0 1 1 1 1]
#  [1 0 0 0 1 1 1 1 1 1]
#  [1 0 1 0 0 1 1 1 1 1]
#  [0 1 1 1 1 1 0 0 0 1]
#  [0 1 1 0 0 1 0 0 0 0]
#  [0 1 1 1 1 0 0 0 0 1]
#  [0 1 1 1 1 1 1 0 0 1]
#  [1 1 1 1 1 1 1 0 0 0]
#  [1 1 1 0 0 0 0 0 0 0]]

##################################################################
## 总结:
# 1. 网络流关键使用 (V+2) * (V+2) 的矩阵来表示
#    这样最后的结果:
#    右上角小矩阵为残差网络/剩余网络, 用来找增广路
#    左下角小矩阵为反向边, 记录了每条边现有的流量
