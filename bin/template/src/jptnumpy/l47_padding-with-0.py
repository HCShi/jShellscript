#!/usr/bin/python3
# coding: utf-8
import numpy as np
##################################################################
## 将 a 填充 0 成 b 的样子
a = np.ones((3, 3)); print(a)
b = np.ones((4, 4)); print(b)
res = np.zeros(b.shape); print(res)
res[:a.shape[0], :a.shape[1]] = a; print(res)
##################################################################
## np.pad(Mat, ()); mode='constant' 填充的是 0
# 一维: (n, m); 左边填充 n 个 0, 右边填充 m 个 0
A = np.ones(3); print(A)  # [ 1.  1.  1.]
B = np.pad(A, (3, 4), 'constant'); print(B)  # [ 1.  1.  1.  0.  0.  0.  0.]
B = np.pad(A, (1, 1), 'constant', constant_values=4); print(B)  # [ 4.  1.  1.  1.  4.]; 改变填充值
# 二维:
# (n, m); 坐上角填 nxn 个 0 , 右下角填 mxm 个 0
# ((n1, m1), (n2, m2)); 首行添加 n1 行, 尾行添加 m1 行; 首列添加 n2 列, 尾列添加 m2 列
# 二维的改变填充值比较奇怪
x = np.array([[1, 2], [3, 4]]); print(x)  # [[1 2] [3 4]]
y = np.pad(x, (1, 1), 'constant'); print(y)  # [[0 0 0 0] [0 1 2 0] [0 3 4 0] [0 0 0 0]]
y = np.pad(x, (1, 1), 'constant', constant_values=(4, 6)); print(y)  # [[4 4 4 6] [4 1 2 6] [4 3 4 6] [4 6 6 6]]
y = np.pad(x, (1, 2), 'constant'); print(y)  # [[0 0 0 0 0] [0 1 2 0 0] [0 3 4 0 0] [0 0 0 0 0] [0 0 0 0 0]]
y = np.pad(x, ((1, 1),(1, 2)), 'constant'); print(y)  # [[0 0 0 0 0] [0 1 2 0 0] [0 3 4 0 0] [0 0 0 0 0] [0 0 0 0 0]]
# 三维:
# ((n1, m1), (n2, m2), (n3, m3)); 和上面差不多, 依次是 d, h, w
# 玩不起 (n, m) 和 ((n1, m1), (n2, m2)) 的, 会很大的
c_x = np.array([[[2, 2], [2, 3]], [[3, 2], [2, 3]]]); print(c_x)  # [[[2 2] [2 3]] [[3 2] [2 3]]]
c_y = np.pad(c_x, ((0, 0), (1, 1), (0, 0)), 'constant'); print(c_y)  # [[[0 0] [2 2] [2 3] [0 0]] [[0 0] [3 2] [2 3] [0 0]]];
c_y = np.pad(c_x, ((1, 1), (0, 0), (0, 0)), mode='constant'); print(c_y)  # [[[0 0] [0 0]] [[2 2] [2 3]] [[3 2] [2 3]] [[0 0] [0 0]]]
c_y = np.pad(c_x, ((0, 0), (1, 1), (1, 1)), mode='constant'); print(c_y)  # [[[0 0 0 0] [0 2 2 0] [0 2 3 0] [0 0 0 0]] [[0 0 0 0] [0 3 2 0] [0 2 3 0] [0 0 0 0]]]
