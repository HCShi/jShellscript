import re
import math
import random
import fileinput
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
# 数据导入
data = np.array([[float(x) for x in re.split(r'\s+', line.strip())] for line in fileinput.input('TSP_Data')])
# 距离计算, 这部分可以不用看, 只要知道最终 d[i, j] 是实对称矩阵, 表示 i, j 之间的地表距离, 计算公式在 README.md 中
x, y = np.hstack(data[:, 0::2].T), np.hstack(data[:, 1::2].T)  # 将 x, y 坐标分开, len = 100, .T 干什么?
s = np.array([[70, 40]] + [[a, b] for a, b in zip(x, y)]) * np.pi / 180  # 转化为弧度, 往 s 中添加了一个点, 不是逐项相加
d = np.zeros((len(s), len(s)))  # len(d) = len(s) = 101
for i in range(len(s)):
	for j in range(len(s)):
		d[i, j] = d[j, i] = 6370 * np.arccos(np.cos(s[i, 0] - s[j, 0]) * np.cos(s[i, 1]) * np.cos(s[j, 1]) + np.sin(s[i, 1]) * np.sin(s[j, 1]))
##################################################################
## 上面是通用的, 下面是算法
# 初始解
path_min, length_min = None, float("inf")
for _ in range(1000):
    path = np.hstack([[0], np.random.permutation(len(s) - 2) + 1, [len(s) - 1]])
    length = sum([d[path[i]][path[i + 1]] for i in range(len(path) - 1)])
    if length < length_min:
        path_min, length_min = path, length
def compute_len(array): return sum([d[array[i]][array[i + 1]] for i in range(len(array) - 1)])
# 禁忌搜索
L = 20000; Nb = 30; Tabu = OrderedDict(); Tabu_size = 100;
for k in range(L):
    candidate = []
    # 二邻域
    for _ in range(Nb):
        c = sorted([int(random.random() * (len(s) - 2) + 1) for _ in range(2)])
        l = length_min + (d[path_min[c[0] - 1]][path_min[c[1]]] + d[path_min[c[0]]][path_min[c[1] + 1]]) - \
                         (d[path_min[c[0] - 1]][path_min[c[0]]] + d[path_min[c[1]]][path_min[c[1] + 1]])
        p = path_min.copy(); p[c[0]: c[1] + 1] = p[c[0]:c[1] + 1][::-1]
        if not tuple(p) in Tabu: candidate.append((tuple(p), l))
    # 三邻域
    for _ in range(Nb):
        c = sorted([int(random.random() * (len(s) - 2) + 1) for _ in range(3)])
        l = length_min + (d[path_min[c[0] - 1]][path_min[c[1] + 1]] + d[path_min[c[1]]][path_min[c[2] + 1]] + d[path_min[c[2]]][path_min[c[0]]]) - \
                         (d[path_min[c[0] - 1]][path_min[c[0]]] + d[path_min[c[1]]][path_min[c[1] + 1]] + d[path_min[c[2]]][path_min[c[2] + 1]])
        p = path_min.copy(); p[c[0]: c[2] + 1] = np.hstack([p[c[1] + 1:c[2] + 1],p[c[0]:c[1] + 1]])
        if not tuple(p) in Tabu: candidate.append((tuple(p),l))
    # 更新
    path_new, length_new = sorted(candidate, key=lambda x:x[1])[0]
    if length_new < length_min: path_min, length_min = np.array(path_new), length_new
    Tabu.update({_p:_l for _p, _l in candidate})
    while len(Tabu) > Tabu_size: Tabu.popitem(last=False)
# 绘图
a, b = s[path_min][:, 0], s[path_min][:, 1]
plt.plot(a, b, '-', linewidth=2)
plt.plot(s[:, 0], s[:, 1], '*')
plt.show()
