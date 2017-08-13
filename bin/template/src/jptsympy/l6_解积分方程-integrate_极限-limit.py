#!/usr/bin/python3
# coding: utf-8
from sympy import *  # 标准引入姿势
init_session(use_latex=True)
init_printing(use_latex=True)
n, t, x = symbols('n t x')
##################################################################
## limit(e, z, z0) Compute the limit of e(z) at the point z0.
print(limit(1/x**2, x, 0))  # oo
print(limit(x * (sqrt(x**2 + 1) - x), x, oo))  # 1/2
##################################################################
## 题目一: 求 s 表达式的极限
s = ((n + 3) / (n + 2))**n; s  # 执行结果会显示要求极限的表达式
print(limit(s, n, oo))  # 以字符形式显示
limit(s, n, oo)  # 和上面的显示结果不一样
##################################################################
## integrate(f, var) 用于积分问题; var 是 x 表示不定积分, (x, a, b) 表示在 (a, b) 上的不定积分
integrate(6 * x**5, x)  # x^6
integrate(cos(x), x)  # sin(x)
##################################################################
## 题目二: 求两重定积分
f = sin(t) / (pi - t); f  # 要积分的式子
m = integrate(f, (t, 0, x)); m  # 这句话执行效率慢...
n = integrate(m, (x, 0, pi)); n  # 2; 嵌套双重积分
