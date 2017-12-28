#!/usr/bin/python3
# coding: utf-8
# 卜东波老师算法课 第四次作业编程
import numpy as np
from scipy.optimize import linprog
A = np.array([
    [3, -1, 1, -2, 0, 0],
    [2, 1, 0, 1, 1, 0],
    [-1, 3, 0, -3, 0, 1]], dtype=float)
b = np.array([-3, 4, 12], dtype=float)
c = np.array([-7, 7, -2, -1, -6, 0], dtype=float)
##################################################################
## 1. scipy 求解
print(linprog(c, A_eq=A, b_eq=b, bounds=(0, None)))  # fun: -16.5; 最优值
##################################################################
## 2. 手写 Dual Simplex 程序
## 由于下面的算法是对标准型带松弛变量的, 所以对目标函数记行了高斯行变换
# target + 2*a1 + 6*a2 将 x3 和 x5 消去, 但会引入 -18 的常量
c = np.array([11, 11, 0, 1, 0, 0], dtype=float)  # 结果还需要 -18
## 本来的 c 都不满足对偶单纯形算法的要求, 但是经过等价变换以后就满足了
## Initial Tableau; 和 Prmal 用同一个 Tableau
tableau = np.vstack((np.pad(c, (1, 0), 'constant'), np.hstack((b.reshape(3, -1), A))))
print(tableau)
# print([x[0] < 0 for x in tableau[1:]])
while any([x[0] < 0 for x in tableau[1:]]):  # 判断 b_i' 是否还有负值
    row = [i+1 for i, x in enumerate(tableau[1:][0]) if x < 0][0]  # b_i' 第一个负值; 因为第一行是 c, 所以 +1
    if all([item >= 0 for item in tableau[row]]):  # 如果第一个 b_i' 负值的对应的行全非负, 则没有最优值
        raise Exception('Linear program is unbounded.')
    columns = [(i, tableau[0][i] / -tableau[row][i]) for i in range(1, len(tableau[0])) if tableau[row][i] < 0]  # 找到很多满足的列, 不会为空, 因为已经保证有负值
    # print(columns)  # 4
    if len(columns) >=2 and len(set(sorted([x[1] for x in  columns])[:2])) == 1:  # 判断是否前两个最小值相同
        raise Exception('Linear program is degenerate.')
    column = min(columns, key=lambda x: x[1])[0];
    # print(column)
    # 上面已经找到对应的行和列了
    # print(row, column)
    pivotDenom = tableau[row][column];
    # print(pivotDenom)  # -2.0; 找到主元
    tableau[row] = [x / pivotDenom for x in tableau[row]]  # 让 pivotDenom 变为 1, 当前行所有值除以 pivotDenom
    for k in range(len(tableau)):  # 将 pivotDenom 所在的列其他元素变为 0, 并进行高斯行变换
        if k != row:
            pivotRowMultiple = [x * tableau[k][column] for x in tableau[row]]
            tableau[k] = [x - y for x, y in zip(tableau[k], pivotRowMultiple)]
    print(tableau)
print(tableau)
print([i for i, col in enumerate(tableau.T) if sum(col) == 1 and len([c for c in col if c == 0]) == len(col) - 1])  # 找到单位矩阵对应的位置
print(list(zip([i for i, col in enumerate(tableau.T) if sum(col) == 1 and len([c for c in col if c == 0]) == len(col) - 1], tableau.T[0])))
print(-tableau[0][0] - 18)  # -16.5; 最优值
##################################################################
## 3. 手写程序
## 参考: https://jeremykun.com/2014/12/01/linear-programming-and-the-simplex-algorithm/
# Return a rectangular identity matrix with the specified diagonal entiries, possibly starting in the middle.
import heapq
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def column(A, j): return [row[j] for row in A]
def transpose(A): return [column(A, j) for j in range(len(A[0]))]
def isPivotCol(col): return (len([c for c in col if c == 0]) == len(col) - 1) and sum(col) == 1
# assume the last m columns of A are the slack variables; the initial basis is the set of slack variables
def initialTableau(c, A, b):
    tableau = [row[:] + [x] for row, x in zip(A, b)]
    tableau.append([ci for ci in c] + [0])
    return tableau
def primalSolution(tableau):
    # the pivot columns denote which variables are used
    columns = transpose(tableau)
    indices = [j for j, col in enumerate(columns[:-1]) if isPivotCol(col)]  # 找到只有一个值, 且为 1 的
    return list(zip(indices, columns[-1]))
def objectiveValue(tableau): return -(tableau[-1][-1])
def canImprove(tableau):
    lastRow = tableau[-1]
    return any(x > 0 for x in lastRow[:-1])
# this can be slightly faster
def moreThanOneMin(L):
    if len(L) <= 1:
        return False
    x, y = heapq.nsmallest(2, L, key=lambda x: x[1])
    return x == y
def findPivotIndex(tableau):
    # pick first nonzero index of the last row
    column = [i for i,x in enumerate(tableau[-1][:-1]) if x > 0][0]
    # check if unbounded
    if all(row[column] <= 0 for row in tableau):
        raise Exception('Linear program is unbounded.')
    # check for degeneracy: more than one minimizer of the quotient
    quotients = [(i, r[-1] / r[column]) for i,r in enumerate(tableau[:-1]) if r[column] > 0]
    if moreThanOneMin(quotients):
        raise Exception('Linear program is degenerate.')
    # pick row index minimizing the quotient
    row = min(quotients, key=lambda x: x[1])[0]
    return row, column
def pivotAbout(tableau, pivot):
    i, j = pivot
    pivotDenom = tableau[i][j]
    tableau[i] = [x / pivotDenom for x in tableau[i]]
    for k, row in enumerate(tableau):
        if k != i:
            pivotRowMultiple = [y * tableau[k][j] for y in tableau[i]]
            tableau[k] = [x - y for x,y in zip(tableau[k], pivotRowMultiple)]
def simplex(c, A, b):
    tableau = initialTableau(c, A, b)
    while canImprove(tableau):
        pivot = findPivotIndex(tableau)
        pivotAbout(tableau, pivot)
    return tableau, primalSolution(tableau), objectiveValue(tableau)
if __name__ == "__main__":
    c = [3, 2]
    A = [[1, 2],
         [1, -1]]
    b = [4, 1]
    # add slack variables by hand
    A[0] += [1, 0]
    A[1] += [0, 1]
    c += [0, 0]
    t, s, v = simplex(c, A, b)
    print(t, s, v)
# [[0.0, 1.0, 0.3333333333333333, -0.3333333333333333, 1.0], [1.0, 0.0, 0.3333333333333333, 0.6666666666666667, 2.0], [0.0, 0.0, -1.6666666666666665, -1.3333333333333335, -8.0]]
# [(0, 1.0), (1, 2.0)] 8.0
