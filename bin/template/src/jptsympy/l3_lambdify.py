#!/usr/bin/python3
# coding: utf-8
from sympy import *  # 标准引入姿势
import numpy as np
init_session(use_latex=True)
init_printing(use_latex=True)
x, y, z = symbols("x y z")
expr = 2*x
##################################################################
## lambdify()
# 如果你想对表达式在多个点进行取值, 例如, 想得到表达式在 1000 个点上的结果, 此时若只使用 SymPy, 效率就不太高; 更加有效的方法是, 使用 NumPy 库或者 SciPy 库
# 将 SymPy 表达式转换为能够代数求解的最简单方法, 就是使用 lambdify 函数; lambdify 有点像 lambda 函数, 它将 SymPy 中的术语转为给定数值库（通常是 NumPy 库）中的术语,
a = np.arange(10)
f = lambdify(x, expr, "numpy")
f(a)  # array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
# a 为要取值的点的横坐标, x 为表达式 expr 中的变量, 指定转换为 NumPy 库中的术语; f(a)表示进行取值, 返回一个含有纵坐标的列表
# 这样可以提高执行效率
