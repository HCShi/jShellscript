#!/usr/bin/python3
# coding: utf-8
# 情景分析: 720 x 720 大型稀疏矩阵求逆
from numpy import *
from scipy.linalg import *
# Mat = random.rand(700, 700)  # random.rand 是 numpy 中的函数, 生成随机矩阵
Mat = eye(720)  # eye 生成单位矩阵
q = [0.9096, 0.7382, 0.585, 0.494, 0.4496, 0.4217, 0.3941, 0.3556, 0.3244, 0.3348, 0.3959, 0.4532]  # list 和下面的 for 循环是为了添加一些对称元素
print(Mat.I)
print(inv(Mat))  # 这样打印会在中间有好多省略号, 最好用 for 打印
