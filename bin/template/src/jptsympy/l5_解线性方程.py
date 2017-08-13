#!/usr/bin/python3
# coding: utf-8
from sympy import *  # 标准引入姿势
init_session(use_latex=True)
init_printing(use_latex=True)
##################################################################
## solve: 第一个参数为要解的方程, 要求右端等于 0, 第二个参数为要解的未知数
x, y, z = symbols("x y z")
print(solve(x * 2 - 4, x))  # [2]
##################################################################
## 解方程组:
# 2x - y = 3
# 3x + y = 7
print(solve([2 * x - y - 3, 3 * x + y - 7], [x, y]))  # {x: 2, y: 1}
