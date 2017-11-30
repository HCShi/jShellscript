#!/usr/bin/python3
# coding: utf-8
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
##################################################################
## make_regression(n_samples=100, n_features=100, n_informative=10, n_targets=1, bias=0.0, effective_rank=None, tail_strength=0.5, noise=0.0,
##     shuffle=True, coef=False, random_state=None)
# Generate a random regression problem.
# noise : float, optional (default=0.0) The standard deviation of the gaussian noise applied to the output.
X_train, y_train = datasets.make_regression(5, 1, n_targets=1, noise=10); print(X_train.shape, y_train.shape)  # (5, 1), (5,)
print(X_train)  # [[-0.86958646] [-1.71682126] [-0.6265871 ] [ 0.82419042] [-0.08056284]]
print(y_train)  # [-36.53755489 -59.18291396 -34.0576309   23.62646674  -0.25897597]
X_train, y_train = datasets.make_regression(3, 2, n_targets=1, noise=10); print(X_train.shape, y_train.shape)  # (3, 2), (3,)
print(X_train)  # [[ 0.69076872 -1.51310813] [-0.49550397 -0.38044674] [-1.78348976  1.38575244]]
print(y_train)  # [-39.96334922 -58.77593593 -35.87022518]
X_train, y_train = datasets.make_regression(3, 1, n_targets=2, noise=10); print(X_train.shape, y_train.shape)  # (3, 1), (3, 2)
print(X_train)  # [[-0.39471974] [ 0.81290018] [-2.06060568]]
print(y_train)  # [[ -16.04815958  -23.6711522 ] [  12.7321429    50.2537519 ] [   0.87336622 -132.63712312]]
## 使用 plt 进行绘制
X_train, y_train = datasets.make_regression(100, 1, n_targets=1, noise=10)
plt.scatter(X_train, y_train); plt.show()
##################################################################
## make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=2, n_repeated=0, n_classes=2, n_clusters_per_class=2,
##     weights=None, flip_y=0.01, class_sep=1.0, hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=None)
# Generate a random n-class classification problem. 这里没有 target, 所以使用 informative 代替了
# n_informative: The number of informative features. Each class is composed of a number of gaussian clusters each located around the vertices of
#     a hypercube in a subspace of dimension `n_informative`. For each cluster, informative features are drawn independently from  N(0, 1) and
#     then randomly linearly combined within each cluster in order to add covariance. The clusters are then placed on the vertices of the hypercube.
X_train, y_train = datasets.make_classification(100, 2, 1, 0, n_clusters_per_class=1); print(X_train.shape, y_train.shape)  # (100, 2) (100,)
print(X_train[0], set(y_train))  # [ 0.18914444 -1.12202319] {0, 1}
X_train, y_train = datasets.make_classification(100, 2, 2, 0, n_clusters_per_class=1); print(X_train.shape, y_train.shape)  # (100, 2) (100,)
print(X_train[0], set(y_train))  # [ 1.08757586 -0.5062478 ] {0, 1}
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.3, random_state=56)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  # (49, 2) (49,) (21, 2) (21,)
plt.scatter(X_train[:, 0], X_train[:, 1], marker='o', c=y_train); plt.show()  # 二分类画图
