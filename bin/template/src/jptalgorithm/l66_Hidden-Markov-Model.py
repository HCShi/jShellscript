#!/usr/bin/python3
# coding: utf-8
# 周晓飞 王泉老师, 第二次作业 手写题, 但是计算麻烦...
# 题目见 王泉老师 slide / jLatex/Course/Statistic_Machine_learning/Assignment_2
import numpy as np
##################################################################
## \lambda 三个参数已知
pi = np.array([0.5, 0.5]); print(pi)  # [ 0.5  0.5]
A = np.array([[0, 1], [0.5, 0.5]]); print(A)  # [[ 0.   1. ] [ 0.5  0.5]]
B = np.array([[0.5, 0.5], [0, 1]]); print(B)  # [[ 0.5  0.5] [ 0.   1. ]]

## 观测序列与状态序列
X = [0, 1, 1, 1, 0]  # 代表 {红, 黑, 黑, 黑, 红} 的观测序列
# Y = [...]  # 状态序列未知
## 观测集合与状态集合
# X = {0, 1} 分别代表 摸到红球/摸到黑球
# Y = {0, 1} 分别代表 有红球信封/无红球信封

##################################################################
## 前向算法
## 前向概率即初始化
alpha = np.zeros((5, 2)); print(alpha.shape)  # (5, 2)
# 初始化前向概率: \alpha_1(i) = \pi_ib_i(x_1)
alpha[0][0] = pi[0] * B[0][X[0]]; print(alpha[0][0])  # 0.25
alpha[0][1] = pi[1] * B[1][X[0]]; print(alpha[0][1])  # 0.0

## 循环计算
for t in range(4):
    for i in range(2):
        alpha[t+1][i] = B[i][X[t+1]] * sum([alpha[t][j] * A[j][i] for j in range(2)])
print(alpha)
# [[ 0.25     0.     ]
#  [ 0.       0.25   ]
#  [ 0.0625   0.125  ]
#  [ 0.03125  0.125  ]
#  [ 0.03125  0.     ]]
result = sum([alpha[4][i] for i in range(2)]); print(result)  # 0.03125

##################################################################
## 后向算法
beta = np.zeros((5, 2)); print(beta.shape)  # (5, 2)
# 初始化后向概率: \beta_n(i) = 1
beta[4][0], beta[4][1] = 1, 1; print(beta[4][0])  # 0.0

## 循环计算
for t in range(3, -1, -1):  # 3 2 1 0
    for i in range(2):
        beta[t][i] = sum([A[i][j] * B[j][X[t+1]] * beta[t+1][j] for j in range(2)])
print(beta)
# [[ 0.125    0.09375]
#  [ 0.125    0.125  ]
#  [ 0.25     0.125  ]
#  [ 0.       0.25   ]
#  [ 1.       1.     ]]
result = sum([pi[i] * B[i][X[0]] * beta[0][i] for i in range(2)]); print(result)  # 0.03125

##################################################################
## 维特比算法
delta = np.zeros((5, 2)); print(delta.shape)  # (5, 2)
phi = np.zeros((5, 2)); print(phi.shape)  # (5, 2)
# 初始化维特比变量 和 路径变量
delta[0][0] = pi[0] * B[0][X[0]]
delta[0][1] = pi[1] * B[1][X[0]]; print(delta[0])  # [ 0.25  0.  ]
phi[0][0], phi[0][1] = 0, 0; print(phi[0])  # [ 0.  0.]

## 循环计算
for t in range(1, 5):
    for i in range(2):
        delta[t][i] = max([delta[t-1][j] * A[j][i] * B[i][X[t]] for j in range(2)])
        phi[t][i] = np.argmax([delta[t-1][j] * A[j][i] * B[i][X[t]] for j in range(2)])
print(delta)
# [[ 0.25      0.      ]
#  [ 0.        0.25    ]
#  [ 0.0625    0.125   ]
#  [ 0.03125   0.0625  ]
#  [ 0.015625  0.      ]]
print(phi)
# [[ 0.  0.]
#  [ 0.  0.]
#  [ 1.  1.]
#  [ 1.  0.]
#  [ 1.  0.]]
