#!/usr/bin/python3
# coding: utf-8
import numpy as np
import scipy.sparse as sparse             # 稀疏矩阵的存储
import scipy.sparse.linalg as sparse_alg  # 一些针对稀疏矩阵的算法
from scipy.sparse import csgraph          # 一些拓扑图的理论, 算法里面包含一些图论的东西
# dia matrix: 做矩阵乘积较快的方式, 适合求特征值, svd 分解什么的.
#             但是如果矩阵的对角性不好, 矩阵大小就要比其他存储方式高到不知道哪里去了, 所以 random 矩阵最好不要用这个方式
# coo/csc/csr matrix: 存储方式相对的比较灵活, 也好理解. 操作重点在于读写矩阵的话用这个可能会比较好.
# bsr matrix: 分块存储
# dok matrix: 基于键值对的方式存储的矩阵, 有点像字典的存储方式
# lil matrix: 很有意思的增量式存储方式, 文档里面说这种方式对索引, 切片操作的资瓷是非常吼的.
# csr 这个最好用了...; 支持 nonzero(), [a, b] 索引
##################################################################
## 1. Coordinate Format (COO) 坐标形式的稀疏矩阵; 采用三个数组 row 、 col 和 data 保存非零元素的信息; 存储的主要优点是灵活、简单
##    COO 不支持元素的存取和增删, 一旦创建之后, 除了将之转换成其它格式的矩阵, 几乎无法对其做任何操作和矩阵运算
## coo_matrix(arg1, shape=None, dtype=None, copy=False):
a = sparse.coo_matrix([[1, 2], [3, 4]]); print(a)  # 简单的创建
print(a[0])  # TypeError: 'coo_matrix' object does not support indexing
# 使用参数创建
row  = np.array([0, 0, 0, 0, 1, 3, 1])
col  = np.array([0, 0, 0, 2, 1, 3, 1])
data = np.array([1, 1, 1, 8, 1, 1, 1])
A = sparse.coo_matrix((data, (row, col)), shape=(4, 4)); print(A); print(A.todense())
##################################################################
## 2. Diagonal Storage Format (DIA) 仅包含非 0 元素的对角线, 对有限元素或者有限差分离散化的矩阵尤其有效
##    DIA 通过两个数组确定: values, distance
# values: 对角线元素的值;
# distance: 第 i 个 distance 是当前第 i 个对角线和主对角线的距离
dia_matrix(arg1[, shape, dtype,copy]) Sparse matrix with DIAgonal storage
##################################################################
## 3. Compressed Sparse Row Format (CSR) 通过四个数组确定: values, columns, pointerB, pointerE.
# values: 包含矩阵 A 中的非 0 元, 以行优先的形式保存
# columns: 第 i 个整型元素代表矩阵 A 中第 i 列
# pointerB : 第 j 个整型元素给出矩阵 A 行 j 中第一个非 0 元的位置, 等价于 pointerB(j) -pointerB(1)+1
# pointerE: 第 j 个整型元素给出矩阵 A 第 j 行最后一个非 0 元的位置, 等价于 pointerE(j)-pointerB(1)
# csr_matrix(arg1[, shape, dtype,copy])
csr = sparse.csr_matrix([[1, 5], [4, 0], [1, 3]]); print(csr)
print(type(csr.todense()))  # todense() 之后是 <class 'numpy.matrixlib.defmatrix.matrix'>
print(type(csr[0]))  # <class 'scipy.sparse.csr.csr_matrix'>
print(csr[0, 0])  # 1; 很方便, 支持索引
for c in csr: print(c)
print(csr.todense())
print(csr.nonzero())  # 把横纵坐标分别打印出来
##################################################################
## 4. Compressed Sparse Column Format (CSC) 类似 CSR 格式, CSC 格式和转置的 CSR 一样
# csc_matrix(arg1[, shape, dtype,copy]) Compressed Sparse Column matrix
##################################################################
## 5. Skyline Storage Format
# The skyline storage format is important for the direct sparse solvers, and it is well suited for Cholesky or LU decomposition
#     when no pivoting is required.
##################################################################
## 6. Block Compressed Sparse Row Format (BSR) 分块压缩稀疏行格式通过四个数组确定: values,columns,pointerB, pointerE.
# values: 是一个实(复)数, 包含原始矩阵 A 中的非 0 元, 以行优先的形式保存
# columns: 第 i 个整型元素代表块压缩矩阵 E 中第 i 列
# pointerB: 第 j 个整型元素给出 columns 第 j 个非 0 块的起始位置
# pointerE: 第 j 个整型元素给出 columns 数组中第 j 个非 0 块的终止位置
# bsr_matrix(arg1[, shape, dtype,copy, blocksize]) Block Sparse Row matrix
##################################################################
## 7. ELLPACK (ELL) 由 ELL+COO 两种格式结合而成
# dok_matrix(arg1[, shape, dtype,copy]) Dictionary Of Keys based sparse matrix
# lil_matrix(arg1[, shape, dtype,copy]) Row-based linked list sparse matrix; 基于行链接列表的稀疏矩阵, 增量式创建稀疏矩阵的结构
##################################################################
## 稀疏矩阵常用属性
# dtype               # 矩阵数据类型
# shape               # (2-tuple)矩阵形状
# ndim                # (int)矩阵维数
# nnz                 # 非 0 元个数
# data                # 矩阵的数据数组
# row                 # COO 特有的, 矩阵行索引
# col                 # COO 特有的, 矩阵列索引
# has_sorted_indices  # BSR 有的, 是否有排序索引
# indices             # BSR 特有的, BSR 格式的索引数组
# indptr              # BSR 特有的, BSR 格式的索引指针数组
# blocksize           # BSR 特有的, 矩阵块大小
##################################################################
## 稀疏矩阵常用方法
# asformat(format)       # 返回给定格式的稀疏矩阵
# astype(t)              # 返回给定元素格式的稀疏矩阵
# diagonal()             # 返回矩阵主对角元素
# dot(other)             # 坐标点积
# getcol(j)              # 返回矩阵列 j 的一个拷贝, 作为一个 (mx 1) 稀疏矩阵 (列向量)
# getrow(i)              # 返回矩阵行 i 的一个拷贝, 作为一个 (1 x n)  稀疏矩阵 (行向量)
# max([axis])            # 给定轴的矩阵最大元素
# nonzero()              # 非 0 元索引
# todense([order, out])  # 返回当前稀疏矩阵的密集矩阵表示
##################################################################
## sparse 模块中用于创建稀疏矩阵的函数
# eye(m[, n, k, dtype, format])                      # Sparse matrix with ones on diagonal
# identity(n[, dtype, format])                       # Identity matrix in sparse format
# kron(A, B[, format])                               # kronecker product of sparse matrices A and B
# kronsum(A, B[, format])                            # kronecker sum of sparse matrices A and B
# diags(diagonals[, offsets, shape, format, dtype])  # Construct a sparse matrix from diagonals.
# spdiags(data, diags, m, n[, format])               # Return a sparse matrix from diagonals.
# block_diag(mats[, format, dtype])                  # Build a block diagonal sparse matrix from provided matrices.
# tril(A[, k, format])                               # Return the lower triangular portion of a matrix in sparse format
# triu(A[, k, format])                               # Return the upper triangular portion of a matrix in sparse format
# bmat(blocks[, format, dtype])                      # Build a sparse matrix from sparse sub-blocks
# hstack(blocks[, format, dtype])                    # Stack sparse matrices horizontally (column wise)
# vstack(blocks[, format, dtype])                    # Stack sparse matrices vertically (row wise)
# rand(m, n[, density, format, dtype, ...])          # Generate a sparse matrix of the given shape and density with uniformly distributed values.
# random(m, n[, density, format, dtype, ...])        # Generate a sparse matrix of the given shape and density  with randomly distributed values.
