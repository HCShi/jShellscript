#!/usr/bin/python3
# coding: utf-8
from sympy import *  # 标准引入姿势
init_session(use_latex=True)
init_printing(use_latex=True)
##################################################################
## SymPy 能够表示方程, 计算导数, 积分, 求极限, 解方程, 矩阵运算等等
x, t, z, nu = symbols('x t z nu')  # 创建符号
Eq(x + 1, 4)  # 表示方程 x + 1 = 4
diff(sin(x) * exp(x), x)  # 计算表达式对 x 的导数 (不定积分)
integrate(exp(x) * sin(x) + exp(x) * cos(x), x)  # 计算不定积分
integrate(sin(x**2), (x, -oo, oo))  # 计算定积分
Integral(sqrt(1 / x), x)  # 生成积分的图片, 最好先定义 x
limit(sin(x)/x, x, 0)  # 1; 求极限
solve(x**2 - 2, x)  # [-sqrt(2), sqrt(2)]; 解方程
y = Function('y')
dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t))  # 求解微分方程
Matrix([[1, 2], [2, 2]]).eigenvals()  # 得到两个值; 求矩阵的特征值
latex(Integral(cos(x)**2, (x, 0, pi)))  # 生成 LaTex 代码
