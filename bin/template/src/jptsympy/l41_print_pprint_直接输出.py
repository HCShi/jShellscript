#!/usr/bin/python3
# coding: utf-8
from sympy import *  # 标准引入姿势
init_session(use_latex=True)
init_printing(use_latex=True)
x = Symbol('x')
f = 2*x - diff(f(x), x)
##################################################################
## 1. 直接输出; 图片渲染的形式输出
f
##################################################################
## 2. print(); 字符的形式输出
print(2*x - diff(f(x), x))  # 2*x - Derivative(f(x), x)
##################################################################
## 3. pprint(); 字符画的形式输出
pprint(2*x - diff(f(x), x))
#       d
# 2*x - --(f(x))
#       dx
