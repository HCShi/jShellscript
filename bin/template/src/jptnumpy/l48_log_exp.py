#!/usr/bin/python3
# coding: utf-8
import numpy as np
##################################################################
## np.log()
print(np.log(10))  # 2.30258509299; 默认是以 e 为底
print(np.log2(8))  # 3.0; numpy 没有像 math.log(x, base) 那样的语法
print(np.log10(10))  # 1.0
# 常用的就那三个, 剩下的要多写异步
print(np.log(16) / np.log(4))  # 2.0
##################################################################
## np.exp()
print(np.exp(1))  # 2.71828182846
print(np.exp([1, 2]))  # [ 2.71828183  7.3890561 ]
print(np.exp([[1, 2], [1, 1]]))  # [[ 2.71828183  7.3890561 ] [ 2.71828183  2.71828183]]

print(2**np.array(3))  # 8
print(2**np.array([1, 2]))  # [2 4]
print(2**np.array([[1, 2], [2, 3]]))  # [[2 4] [4 8]]
# print(2**[2, 3])  # 直接用 list 会报错
