#!/usr/bin/python3
# coding: utf-8
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt
##################################################################
## 先测试一下 scale() 函数
a = np.array([[10, 2.7, 3.6],
              [-100, 5, -2],
              [120, 20, 40]], dtype=np.float64)
print(a)
print(preprocessing.scale(a))  # 正态分布化; 好像只是每个纵列之间的伸缩...
# [[ 0.         -0.85170713 -0.55138018]
#  [-1.22474487 -0.55187146 -0.852133  ]
#  [ 1.22474487  1.40357859  1.40351318]]
##################################################################
## 生成数据 并 plot
X, y = make_classification(n_samples=300, n_features=2 , n_redundant=0, n_informative=2,
                           random_state=22, n_clusters_per_class=1, scale=100)
# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.show()
##################################################################
## 范围变窄, 这里可以 注释掉来重复执行, 测试 clf.score()
X = preprocessing.scale(X)    # normalization step
##################################################################
## 生成模型, 并学习 测试数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
clf = SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
