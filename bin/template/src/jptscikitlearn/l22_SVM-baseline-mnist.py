#!/usr/bin/python3
# coding: utf-8
from keras.datasets import mnist
from sklearn import svm
from keras.utils import np_utils
##################################################################
## SVM baseline
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  # (60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
print(set(y_train))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
X_train = X_train.reshape(X_train.shape[0], -1) / 255.
X_test = X_test.reshape(X_test.shape[0], -1) / 255.  # 这里也必须进行归一化, 否则结果很惨...
print(X_train.shape, X_test.shape)  # (60000, 784) (10000, 784)
# SVM 不用将 y_train 弄成 one-hot 的形式, 会报错, ValueError: bad input shape (1000, 10)

clf = svm.SVC()
clf.fit(X_train[:1000], y_train[:1000])  # 使用所有的数据会很慢...
predications = clf.predict(X_test[:10]); print(predications)  # [7 5 1 0 4 1 4 9 2 9]
print(y_test[:10])                                            # [7 2 1 0 4 1 4 9 5 9]
##################################################################
## clf 参数
print(clf.coef_)  # AttributeError: coef_ is only available when using a linear kernel
##################################################################
## 不同参数对比
clf_lin = svm.SVC(kernel='linear', decision_function_shape='ovo')
clf_poly = svm.SVC(kernel='poly', decision_function_shape='ovo')
clf_rbf = svm.SVC(kernel='rbf', decision_function_shape='ovo')
clf_lin.fit(X_train[:1000], y_train[:1000])  # 这三个都是近 20s, 还可以忍
clf_rbf.fit(X_train[:1000], y_train[:1000])
clf_poly.fit(X_train[:1000], y_train[:1000])
print(y_test[:10])                    # [7 2 1 0 4 1 4 9 5 9]
print(clf_lin.predict(X_test[:10]))   # [7 2 1 0 4 1 4 9 2 9]
print(clf_rbf.predict(X_test[:10]))   # [7 5 1 0 4 1 4 9 2 9]
print(clf_poly.predict(X_test[:10]))  # [7 7 7 7 7 7 7 7 7 7]
