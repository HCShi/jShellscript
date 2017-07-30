#!/usr/bin/python3
# coding: utf-8
from sklearn import svm
from sklearn import datasets
##################################################################
## 准备数据, 测试模型
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf = svm.SVC()
clf.fit(X, y)
##################################################################
## method 1: pickle
import pickle
# save
with open('tmp/clf.pickle', 'wb') as f:
    pickle.dump(clf, f)
# restore
with open('tmp/clf.pickle', 'rb') as f:
   clf2 = pickle.load(f)
   print(clf2.predict(X[0:1]))  # [0]
##################################################################
## method 2: joblib; 据说比较快, 因为使用了多进程
from sklearn.externals import joblib
# Save
joblib.dump(clf, 'tmp/clf.pkl')
# restore
clf3 = joblib.load('tmp/clf.pkl')
print(clf3.predict(X[0:1]))  # [0]
