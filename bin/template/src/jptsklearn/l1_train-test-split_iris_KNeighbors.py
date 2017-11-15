import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier  # 临近几个点作为邻居, 并综合模拟出此处的值
##################################################################
## 准备数据
iris = datasets.load_iris()  # 鸢尾花数据
iris_X = iris.data  # iris 的属性, 一维数组, columns 就是 iris 的属性数量
iris_y = iris.target  # iris 分类
print(iris_X[:2, :])  # 第二个 : 表示纵向的取值范围, 这里是全部; 这是 numpy 对象的属性, 普通 list 不能
print(len(iris_y), '\n', iris_y)  # 150 个数据; 0 1 2 三个分类;
##################################################################
## 使用 train_test_split 将数据分为 train 和 test 两类, test 占 30% 的比例
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)
print(len(X_train), '\n', len(X_test))  # 105, 45; 这些是将 iris_X 的数据进行切割; 同时会打乱数据...
##################################################################
## 生成 Model, 并使用 Model
knn = KNeighborsClassifier()  # 生成 Model
knn.fit(X_train, y_train)  # Model 进行数据训练
##################################################################
## 将 Model 应用到 test data 上, 并和 y_test 进行对比
print(knn.predict(X_test))
print(y_test)
