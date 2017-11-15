#!/usr/bin/python3
# coding: utf-8
import random
##################################################################
## 打乱 list
lis = [20, 16, 10, 5]
random.shuffle(lis); print(lis)
##################################################################
## 绑定两个数组, shuffle, 解绑; zip(*A) 的魅力
a, b = [str(i) + 'a' for i in range(100)], [str(i) + 'b' for i in range(100)]; c = list(zip(a, b))  # 绑定数组
import random; random.shuffle(c)  # 乱序
a, b = zip(*c); a, b = list(a), list(b); print(a, '\n', b)  # zip() 返回的是两个 tuple
##################################################################
## 通过确定 shuffle(x, random) 第二个参数
a, b = [str(i) + 'a' for i in range(100)], [str(i) + 'b' for i in range(100)];
r = random.random()           # randomly generating a real in [0,1)
random.shuffle(a, lambda :r)  # lambda :r is an unary function which returns r
random.shuffle(b, lambda :r)  # using the same function as used in prev line so that shuffling order is same
print(a, '\n', b)
##################################################################
## sklearn 实现上面的...; NumPy (>= 1.6.1), SciPy (>= 0.9)
a, b = [str(i) + 'a' for i in range(100)], [str(i) + 'b' for i in range(100)];
from sklearn.utils import shuffle; a, b = shuffle(a, b); print(a, '\n', b)
##################################################################
## 打乱 iris
from sklearn import datasets
import numpy as np
# 第一步: 将 data 和 target 绑定到一起, shuffle 一下
iris = datasets.load_iris()
iris = list(zip(iris.data, iris.target))
random.shuffle(iris); print(iris[0])  # (array([ 6.3,  3.3,  6. ,  2.5]), 2); 这样不好的地方是 tuple 格式
# 第二步: 将 data 和 target 再分开
x, y = zip(*iris[:30]); x, y = np.mat(list(x)), np.mat(list(y))  # (*c) 是去掉外面一层, 需要转型
print(x, y)  # 这样就可以扔到 dot(), .T, .I 中运算了
##################################################################
## 总结:
# 1. 不用赋值回去 y = random.shuffle(y)
# 2. 因为 iris 是按 0, 1, 2, 3 顺序排的, 有时候想用部分做测试, 前面都是 0 类...
