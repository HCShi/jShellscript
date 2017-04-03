#!/usr/bin/python3
# coding: utf-8
import math
from l1_exercise_2_myInterval_plus_minux_multiplication_division_exp_log_sqr_min_max import *
class Box:
    def __init__(X, a, b):  # 将二维的定义成大写
        X.x, X.y = a, b
    def __repr__(X):
        return "[%f, %f] X [%f, %f]" % (X.x.lb, X.x.ub, X.y.lb, X.y.ub)
    def width(X):
        if X.x.is_empty() or X.y.is_empty(): return -oo
        else: return max(X.x.width(), X.y.width())  # 在两个区间中选最长的
    def left(X):
        if X.x.width() > X.y.width(): return Box(X.x.left(), X.y)  # 将 X.x 左右分, 取左边
        else: return Box(X.x, X.y.left())  # 上下分
    def right(X):
        if X.x.width() > X.y.width(): return Box(X.x.right(), X.y)  # 将 X.x 左右分, 取右边
        else: return Box(X.x, X.y.right())
