import re
import math
import random
import fileinput
import numpy as np
import matplotlib.pyplot as plt
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
## 上面是通用的, 下面开始算法, 结合 第23章++现代优化算法
numant = numcity = len(s); numiter = 50  # 101 只蚂蚁和城市, 迭代 50 次
alpha = 1; beta = 1; rho = 0.5; Q = 1
# alpha: 信息素重要程度因子(轨迹相对重要性); beta: 启发函数重要程度因子(能见度相对重要性); rho: 信息素的挥发速度(轨迹持久性)
heutable = 1.0 / (d + np.diag([1e10] * numcity))  # 启发函数矩阵, 表示蚂蚁从城市 i 转移到矩阵 j 的期望程度, 对角线长度 101; 是定值, 初始化以后不会改变
phetable = np.ones((numcity, numcity))  # 信息素矩阵 Pheromones; 城市之间的信息素的轨迹强度
len_min = float('inf'); path_min = None  # 记录最短距离
##################################################################
## 蚁群模拟
for _ in range(numiter):
	# 初始化
	pathtable = np.zeros((numant, numcity))  # 路径记录表
	pathtable[:, 0] = np.random.permutation(numcity); length = np.zeros(numant)  # 初始化蚂蚁所在的城市, 每个城市一只蚂蚁
	# 轮盘赌, 每个蚂蚁走一次, 循环完以后更新 phetable
	for i in range(numant):
		visiting = pathtable[i, 0]; print(visiting)  # 初始点加入 visiting
		unvisited = list(range(numcity)); unvisited.remove(visiting)  # unvisited 删除初始点
		for j in range(1, numcity):  # 循环 numcity - 1 次, 访问剩余的 numcity - 1 个城市
			probtrans = np.array([phetable[int(visiting)][int(unvisited[k])]**alpha * heutable[int(visiting)][int(unvisited[k])]**beta for k in range(len(unvisited))])
			probtranscumsum = (probtrans/probtrans.sum()).cumsum() - np.random.rand()
            # 上面两行是轮盘法计算公式里面的概率
			k = unvisited[np.where(probtranscumsum > 0)[0][0]]  # 每次用轮盘法选择下一个要访问的城市
			pathtable[i, j] = k; unvisited.remove(k)
			length[i] += d[int(visiting)][k]
			visiting = k
		length[i] += d[int(visiting)][int(pathtable[i, 0])]  # 蚂蚁的路径距离包括最后一个城市和第一个城市的距离
	# 更新最短路径
	if length.min() < len_min: len_min = length.min(); path_min = pathtable[length.argmin()].copy().astype(int)
	# 信息素释放和更新
	phetabledelta = np.zeros((numcity, numcity))  # 上一轮走过的路径上的信息素需要增加 phetabledelta
	for i in range(numant):  # 遍历, 将上一轮所有走过的路径添加信息素
		for j in range(numcity - 1):
			phetabledelta[int(pathtable[i, j])][int(pathtable[i, j + 1])] += Q / d[int(pathtable[i, j])][int(pathtable[i, j + 1])]
		phetabledelta[int(pathtable[i, -1])][int(pathtable[i, 0])] += Q / d[int(pathtable[i, -1])][int(pathtable[i, 0])]
	phetable = (1 - rho) * phetable + phetabledelta  # 所有路径上的信息素更新
# 绘图
path_min = np.hstack([path_min, [path_min[0]]])
a, b = s[path_min][:, 0], s[path_min][:, 1]
plt.plot(a, b, '-', linewidth=2)
plt.plot(s[:, 0], s[:, 1], '*')
plt.show()
