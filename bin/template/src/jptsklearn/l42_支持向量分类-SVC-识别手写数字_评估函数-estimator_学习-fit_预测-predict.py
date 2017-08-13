#!/usr/bin/python3
# coding: utf-8
##################################################################
## 评估函数 (estimator) 是一个 Python 对象, 它实现了 fit(X, y) 与 predict(T) 方法
# 类 sklearn.svm.SVC 就是一个实现了支持向量分类的评估函数, 这里仅是做一个简单的例子, 不深究算法的细节与参数的选择, 我们仅把它当作一个黑盒
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)  # 这里我们手动地设置了 gamma 的值, 使用格点搜索与交叉验证的方法可以自动帮我们找到较好的参数
# 评估函数实例的变量名取作 clf, 说明它是一个分类器 (classifier)
##################################################################
## fit(X, y) 学习过程
# 将训练集传递给 fit 方法进行数据拟合之后就可以做预测了; 这里我们取数据集的最后一张图为预测图, 前面的数据都作为训练数据
from sklearn import datasets
digits = datasets.load_digits()
clf.fit(digits.data[:-1], digits.target[:-1])
print(clf)
# SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
#   gamma=0.001, kernel='rbf', max_iter=-1, probability=False,
#   random_state=None, shrinking=True, tol=0.001, verbose=False)
##################################################################
## predict(X) 预测
print(clf.predict(digits.data[-1]))  # [8]
# 将最后一张图片画出来
print(digits.images.shape)
import matplotlib.pyplot as plt
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
