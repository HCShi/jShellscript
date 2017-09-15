#!/usr/bin/python3
# coding: utf-8
import random
##################################################################
## 打乱 list
list = [20, 16, 10, 5]
random.shuffle(list); print(list)
##################################################################
## 打乱 iris
from sklearn import datasets
import numpy as np
# 第一种
iris = datasets.load_iris()
iris = list(zip(iris.data, iris.target))
random.shuffle(iris); print(iris[0])  # (array([ 6.3,  3.3,  6. ,  2.5]), 2); 这样不好的地方是 tuple 格式
# 第二种, 接着上面
x, y = zip(*iris[:30]); x, y = np.mat(list(x)), np.mat(list(y))  # zip(*c) 默认是 tuple, 需要转型
print(x, y)  # 这样就可以扔到 dot(), .T, .I 中运算了
##################################################################
## 总结:
# 1. 不用赋值回去 y = random.shuffle(y)
# 2. 因为 iris 是按 0, 1, 2, 3 顺序排的, 有时候想用部分做测试, 前面都是 0 类...
