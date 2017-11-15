#!/usr/bin/python3
# coding: utf-8
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
##################################################################
## 准备数据
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)  # test train split
##################################################################
## 准备模型 && 进行验证
knn = KNeighborsClassifier(n_neighbors=5)  # 考虑数据点周围的 5 个数值, 综合得出...
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(knn.score(X_test, y_test))  # 0.9736
##################################################################
## cross_val_score 交叉验证
from sklearn.model_selection import cross_val_score
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')  # 会自动将数据交叉检测, 5 次
print(scores)  # [ 0.96666667  1.          0.93333333  0.96666667  1.        ]
print(scores.mean())  # 0.973
##################################################################
## 下面进行验证 n_neighbors 的变化对测试的影响, 并进行 plot 显示
# this is how to use cross_val_score to choose model and configs
import matplotlib.pyplot as plt
k_range = range(1, 31)
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    # loss = -cross_val_score(knn, X, y, cv=10, scoring='mean_squared_error')  # for regression
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')  # for classification
    k_scores.append(scores.mean())
plt.plot(k_range, k_scores)  # 可以查看到采用那个 n_neighbors 参数是, 更加的合适
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()
