#!/usr/bin/python3
# coding: utf-8
# 参考: http://www.vision.ime.usp.br/~igor/articles/optimization-linprog.html
import numpy as np
from scipy.optimize import linprog
from numpy.linalg import solve
##################################################################
## 1. Write the problem above using LP and give a solution
# minimize f(x) = 70*x1 + 80*x2 + 85*x3
# x1 + x2 + x3 = 999
# x1 + 4*x2 + 8*x3 ≤ 4500
# 40*x1 + 30*x2 + 20*x3 ≤ 36000
# 3*x1 + 2*x2 + 4*x3 ≤ 2700
# x_i≥0
A_eq = np.array([[1, 1, 1]])
b_eq = np.array([999])
A_ub = np.array([
    [1, 4, 8],
    [40, 30, 20],
    [3, 2, 4]])
b_ub = np.array([4500, 36000,2700])
c = np.array([70, 80, 85])
## linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None, method='simplex', callback=None, options=None)
# Minimize a linear objective function subject to linear equality and inequality constraints.
res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=(0, None))
print('Optimal value:', res.fun, '\nX:', res.x)
# Optimal value: 73725.0
# X: [ 636.  330.   33.]
##################################################################
## 2. Convert the problem into the standard form; Add slack variables for all inequality constraints
# minimize f(x) = 70*x1 + 80*x2 + 85*x3
# x1 + x2 + x3 = 999
# x1 + 4*x2 + 8*x3 + s1 = 4500
# 40*x1 + 30*x2 + 20*x3 + s2 = 36000
# 3*x1 + 2*x2 + 4*x3 + s3 = 2700
# x≥0, s≥0
A = np.array([
    [1, 1, 1, 0, 0, 0],
    [1, 4, 8, 1, 0, 0],
    [40, 30, 20, 0, 1, 0],
    [3, 2, 4, 0, 0, 1]])
b = np.array([999, 4500, 36000, 2700])
c = np.array([70, 80, 85, 0, 0, 0])
res = linprog(c, A_eq=A, b_eq=b, bounds=(0, None))
res = linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method='simplex')  # 看不出来单纯形算法在哪里用到了
print('Optimal value:', res.fun, '\nX:', res.x)
# Optimal value: 73725.0
# X: [  636.   330.    33.  2280.     0.     0.]
# Note that s_1 = 2280 implies that x1 + 4*x2 + 8*x3 <= 4500
##################################################################
# 3. Present the dual of the problem above and show that both problems achieve the same results
# maximize f(y) = 999*y1 + 4500*y2 + 360000*y3 + 2700*y4
# y1 + y2 + 40*y3 + 3*y4 ≤ 70
# y1 + 4*y2 + 30*y3 + 2*y4 ≤ 80
# y1 + 8*y2 + 20*y3 + 4*y4 ≤ 85
# y2≤0, y3≤0, y4≤0
res = linprog(-b, A_ub=A.T, b_ub=c, bounds=[(None, None), (None, None), (None, None), (None, None)])
y = res.x
print('Optimal value:', -res.fun, '\nY:', y)
# Optimal value: 73725.0
# Y: [ 108.33333333    0.           -0.83333333   -1.66666667]

u = c - A.T.dot(y)
Ar = A[:, np.abs(u)< 1e-10]
x_1 = solve(Ar, b); print(x_1)  # [  636.   330.    33.  2280.]
x = np.array([0.0] * len(c))
x[np.abs(u)< 1e-10] = x_1
x[np.abs(u)> 1e-10] = 0
print('Primal solution from the dual:', x)
# Primal solution from the dual: [  636.   330.    33.  2280.     0.     0.]
