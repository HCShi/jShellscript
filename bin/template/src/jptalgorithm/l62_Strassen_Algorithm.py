#!/usr/bin/python3
# coding: utf-8
# 卜东波老师算法课 第一次作业编程
# 算法讲解: [Wiki](https://en.wikipedia.org/wiki/Strassen_algorithm)
import numpy as np
def straight(a, b):  # 传统方法, 两个矩阵相乘
    if len(a[0]) != len(b): return "Matrices are not m*n and n*p"  # A 矩阵的 columns 和 B 矩阵的 rows 不同
    p_matrix = np.zeros((len(a), len(b[0])))
    # for i in range(len(a)):
    #     for j in range(len(b[0])):
    #         for k in range(len(b)):
    #             p_matrix[i][j] += a[i][k] * b[k][j]  # 将 for 循环转换为下面几句
    p_matrix += [[np.sum([a[i][k] * b[k][j] for k in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))]
    return p_matrix
def split(matrix):  # split matrix into quarters
    row, col = matrix.shape
    return matrix[:row//2, :col//2], matrix[:row//2, col//2:], matrix[row//2:, :col//2], matrix[row//2:, col//2:]
def strassen(a, b):
    q = len(a)
    if q == 1:  # base case: 1x1 matrix
        # d = np.array([[0]])
        # d[0][0] = a[0][0] * b[0][0]
        # return d  # 将这 3 句简化为 1 句
        return a * b  # 1 x 1 就直接用 Numpy 计算了
    a11, a12, a21, a22 = split(a)
    b11, b12, b21, b22 = split(b)
    p1 = strassen(a11 + a22, b11 + b22)  # p1 = (a11 + a22) * (b11 + b22)
    p2 = strassen(a21 + a22, b11)        # p2 = (a21 + a22) * b11
    p3 = strassen(a11, b12 - b22)        # p3 = a11 * (b12 - b22)
    p4 = strassen(a22, b21 - b11)        # p4 = a22 * (b21 - b11)
    p5 = strassen(a11 + a12, b22)        # p5 = (a11 + a12) * b22
    p6 = strassen(a21 - a11, b11 + b12)  # p6 = (a21 - a11) * (b11 + b12)
    p7 = strassen(a12 - a22, b21 + b22)  # p7 = (a12 - a22) * (b21 + b22)
    c11 = p1 + p4 - p5 + p7  # c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5            # c12 = p3 + p5
    c21 = p2 + p4            # c21 = p2 + p4
    c22 = p1 + p3 - p2 + p6  # c22 = p1 + p3 - p2 + p6
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))  # 重新堆叠起来
    return c
def check():
    a = np.random.randint(0, 10, size=(16, 16))
    b = np.random.randint(0, 10, size=(16, 16))
    assert (strassen(a, b) == straight(a, b)).all()
    assert (np.array(strassen(a, b)) == np.dot(a, b)).all()
    print('Hooray!')
check()
def time():
    a = np.random.randint(0, 10, size=(1024, 1024))
    b = np.random.randint(0, 10, size=(1024, 1024))
    import time
    st = time.clock()
    strassen(a, b)
    print("Strassen Algorithm:", time.clock() - st);
    st = time.clock()
    straight(a, b)
    print("Classical Method:", time.clock() - st);
    st = time.clock()
    np.dot(a, b)
    print("Numpy Lib:", time.clock() - st);
time()
##################################################################
## 总结:
# 1. 这里默认使用的是 2^n 的方阵, 其他的需要先填充 0, 这里没有写
# 2. 128x128
#    Strassen Algorithm: 6.9863159999999995
#    Classical Method: 1.6585130000000001
#    Numpy Lib: 0.00234400000000079
# 3. 1024x1024
#    Strassen Algorithm: 2499.392781
#    Classical Method: 776.8647190000002
#    Numpy Lib: 7.796399999999721
