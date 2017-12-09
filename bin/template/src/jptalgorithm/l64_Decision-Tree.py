#!/usr/bin/python3
# coding: utf-8
## 数据挖掘第二次作业, 手写题, 但是计算太麻烦...
import numpy as np
from math import log
##################################################################
## 大量计算  Gain(D) = Info(D) - Info_feature(D)
def Gain(data, num_yes):  # 题目是二分类, 所以这里也就是 二分类
    sum_data = np.sum([item for line in data for item in line]);
    prob = num_yes / sum_data
    Info_D = -prob*log(prob, 2) - (1 - prob)*log((1-prob), 2)
    print(Info_D)

    Info_D_feature = 0.0
    for line in data:
        sum_line = np.sum(line)
        splitInfo = 0.0
        for item in line:
            prob = item / sum_line
            splitInfo += -prob * log(prob, 2)
        Info_D_feature += sum_line / sum_data * splitInfo
    print(Info_D_feature)
    return Info_D - Info_D_feature
## 计算第一层
print(Gain(np.array([[3, 2], [2, 1], [1]]), 4), '\n')  # 特征按特征值分类, 每类数据里面再按 label 分类
print(Gain(np.array([[2, 2], [3, 1], [1]]), 4), '\n')
print(Gain(np.array([[3], [2, 4]]), 4), '\n')
## 计算第二层
print(Gain(np.array([[1, 2], [1, 1], [1]]), 2), '\n')
print(Gain(np.array([[2, 1], [1], [2]]), 2), '\n')
