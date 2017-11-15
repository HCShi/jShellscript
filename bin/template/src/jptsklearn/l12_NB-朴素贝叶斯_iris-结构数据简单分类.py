#!/usr/bin/python3
# coding: utf-8
# scikit-learn 里面有 3 种不同类型的朴素贝叶斯:
# 1. 高斯分布型: 用于 classification 问题, 假定属性/特征是服从正态分布的
# 2. 多项式型: 用于离散值模型里。比如文本分类问题里面我们提到过, 我们不光看词语是否在文本中出现, 也得看出现的次数。如果总词数为 n, 出现词数为 m 的话, 说起来有点像掷骰子 n 次出现 m 次这个词的场景。
# 3. 伯努利型: 这种情况下, 就如之前博文里提到的 bag of words 处理方式一样, 最后得到的特征只有 0(没出现) 和 1(出现过)
from sklearn.naive_bayes import GaussianNB  # 高斯分布型
from sklearn import datasets
##################################################################
## 高斯分布型朴素贝叶斯建模; 取 iris 数据集
iris = datasets.load_iris()
print(iris.data[:1])  # [[ 5.1  3.5  1.4  0.2]]
# 我们假定 sepal length, sepal width, petal length, petal width 4 个量独立且服从高斯分布, 用贝叶斯分类器建模
##################################################################
## 简短的训练验证过程
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
right_num = (iris.target == y_pred).sum()
print("Total testing num :%d, naive bayes accuracy :%f" % (iris.data.shape[0], float(right_num)/iris.data.shape[0]))
# Total testing num :150 , naive bayes accuracy :0.960000
