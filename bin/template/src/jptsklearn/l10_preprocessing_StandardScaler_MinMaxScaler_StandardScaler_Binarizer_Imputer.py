#!/usr/bin/python3
# coding: utf-8
# 参考 [Official](http://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)
# 对照 scikit-learn.preprocessing 章节结合代码简单的回顾下预处理技术的几种方法, 主要包括标准化、数据最大最小缩放处理、正则化、特征二值化和数据缺失值处理
from sklearn import preprocessing
import numpy as np
##################################################################
## ** 0. 下面的方法都是对列进行操作, 因为把列当做一个特征的所有值  **
a = np.array([23, 29, 27])  # 1D 数据按列排放, 但是还是说不清...
# print(preprocessing.MinMaxScaler().fit_transform(a))  # Expected 2D array, got 1D array instead:
# print(preprocessing.MinMaxScaler().fit_transform(a.T))  # Expected 2D array, got 1D array instead:
print(a.shape, a.T.shape)  # (3,) (3,)
print(a.reshape(-1, 1).shape)  # (3, 1)
print(preprocessing.MinMaxScaler().fit_transform(a.reshape(-1, 1)).reshape(1, -1))  # [[ 0.          1.          0.66666667]]

# 对下面的方法用自己的方式实现一遍
print((a - a.min()) / (a.max() - a.min()))  # [ 0.          1.          0.66666667]
##################################################################
# 1. StandardScaler() 标准化 Standardization
# 数据标准化: 当单个特征的样本取值相差甚大或明显不遵从高斯正态分布时, 标准化表现的效果较差;
# 实际操作中, 经常忽略特征数据的分布形状, 移除每个特征均值, 划分离散特征的标准差, 从而等级化, 进而实现数据中心化
# 公式为: (X-X_mean)/X_std 计算时对每个属性/每列分别进行; 最后得到的结果是, 对每个属性/每列来说所有数据都聚集在 0 附近, 方差值为 1
# sklearn.preprocessing.scale(X, axis=0, with_mean=True, with_std=True, copy=True)
# X: 数组或者矩阵
# axis: int 类型, 初始值为 0, axis 用来计算均值 means 和标准方差 standard deviations. 如果是 0, 则单独的标准化每个特征(列), 如果是 1, 则标准化每个观测样本(行)
# with_mean: boolean 类型, 默认为 True, 表示将数据均值规范到 0
# with_std: boolean 类型, 默认为 True, 表示将数据方差规范到 1
X = np.array([[1., -1.,  2.], [2.,  0.,  0.], [0.,  1., -1.]]); print(X)
X_mean = X.mean(axis=0); print(X_mean)  # [ 1.          0.          0.33333333]; 用来计算数据 X 每个特征的均值
X_std = X.std(axis=0)  # calculate variance; 用来计算数据 X 每个特征的方差
X1 = (X - X_mean) / X_std; print(X1)  # standardize X; 这三行是手动计算标准化 X
# 方法 1: 使用 sklearn.preprocessing.scale() 函数
X_scale = preprocessing.scale(X); print(X_scale)  # 直接标准化数据 X; X_scale 和上面的 X1 一样
# 方法 2: sklearn.preprocessing.StandardScaler 类
scaler = preprocessing.StandardScaler()
X_scaled = scaler.fit_transform(X); print(X_scaled)  # X_scaled 和 X1 也一样
# 只能处理 2-D 数据
# print(preprocessing.StandardScaler().fit_transform([2, 1, 2]))  # ValueError: Expected 2D array, got 1D array instead
print(preprocessing.StandardScaler().fit_transform(np.array([2, 1, 2]).reshape(-1, 1)))  # 将 (1, ) 转化为 (-1, 1)
print(preprocessing.StandardScaler().fit_transform([[2, 1, 2]]))  # [[ 0.  0.  0.]]; 伪装成 2-D, 但没意义
print(preprocessing.StandardScaler().fit_transform([[2, 1], [1, 2]]))  # [[ 1. -1.] [-1.  1.]]
##################################################################
## 2. MinMaxScaler() 将特征的取值缩小到一个范围, 如 0 到 1
# 1. 对于方差非常小的属性可以增强其稳定性
# 2. 维持稀疏矩阵中为 0 的条目
# 注意: 这些变换都是对列进行处理...
# 当然, 在构造类对象的时候也可以直接指定最大最小值的范围: feature_range=(min, max), 此时应用的公式变为:
# X_std=(X-X.min(axis=0)) / (X.max(axis=0)-X.min(axis=0))
# X_minmax=X_std/(X.max(axis=0)-X.min(axis=0))+X.min(axis=0))
X = np.array([[1., -1.,  2.], [2.,  0.,  0.], [0.,  1., -1.]])
min_max_scaler = preprocessing.MinMaxScaler()
X_minMax = min_max_scaler.fit_transform(X); print(X_minMax)  # [[0.5, 0., 1.], [1., 0.5, 0.333], [0., 1., 0.]]
X_test = np.array([[-3., -1., 4.]])  # 下面分别是 训练 和 转换
# X_test_minmax = min_max_scaler.fit_transform(X_test); print(X_test_minmax)  # [[ 0.  0.  0.]]
X_test_minmax = min_max_scaler.transform(X_test); print(X_test_minmax)  # [[-1.5, 0., 1.66666667]]; fit_transform 和 transform 见下面
##################################################################
## 3. StandardScaler() 正则化 Normalization, 也叫归一化
# 正则化的过程是将每个样本缩放到单位范数 (每个样本的范数为 1),
# 如果要使用如二次型 (点积) 或者其它核方法计算两个样本之间的相似性这个方法会很有用
# 该方法是文本分类和聚类分析中经常使用的向量空间模型 (Vector Space Model) 的基础
# Normalization 主要思想是对每个样本计算其 p- 范数, 然后对该样本中每个元素除以该范数,
# 这样处理的结果是使得每个处理后样本的 p- 范数 (l1-norm, l2-norm) 等于 1
# 方法 1: 使用 sklearn.preprocessing.normalize() 函数
X = np.array([[1., -1.,  2.], [2.,  0.,  0.], [0.,  1., -1.]])
X_normalized = preprocessing.normalize(X, norm='l2'); print(X_normalized)
# 方法 2: sklearn.preprocessing.StandardScaler 类
normalizer = preprocessing.Normalizer().fit(X); print(normalizer)  # Normalizer(copy=True, norm='l2'); fit does nothing
print(normalizer.transform(X))  # 然后使用正则化实例来转换样本向量
print(normalizer.transform([[-1.,  1., 0.]]))
##################################################################
## 4. Binarizer() 二值化 Binarization
# 特征的二值化主要是为了将数据特征转变成 boolean 变量
X = np.array([[1., -1.,  2.], [2.,  0.,  0.], [0.,  1., -1.]])
binarizer = preprocessing.Binarizer().fit(X); print(binarizer)  # fit does nothing
print(binarizer.transform(X))
# Binarizer 函数也可以设定一个阈值, 结果数据值大于阈值的为 1, 小于阈值的为 0, 实例代码如下：
binarizer = preprocessing.Binarizer(threshold=1.1); print(binarizer.transform(X))  # 二值化设定 threshold 后可以不用 fit()
##################################################################
## 5. Imputer() 缺失值处理
# 许多现实中的数据集都包含有缺失值, 要么是空白的, 要么使用 NaNs 或者其它的符号替代
# 这些数据无法直接使用 scikit-learn 分类器直接训练, 所以需要进行处理
# 幸运地是, sklearn 中的 Imputer 类提供了一些基本的方法来处理缺失值,
# 如使用均值、中位值或者缺失值所在列中频繁出现的值来替换
imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
print(imp.fit([[1, 2], [np.nan, 3], [7, 6]]))  # Imputer(axis=0, copy=True, missing_values='NaN', strategy='mean', verbose=0)
X = [[np.nan, 2], [6, np.nan], [7, 6]]; print(imp.transform(X))
# Imputer 类同样支持稀疏矩阵
import scipy.sparse as sp
X = sp.csc_matrix([[1, 2], [0, 3], [7, 6]]); print(X)
imp = preprocessing.Imputer(missing_values=0, strategy='mean', axis=0)
print(imp.fit(X))  # Imputer(axis=0, copy=True, missing_values=0, strategy='mean', verbose=0)
X_test = sp.csc_matrix([[0, 2], [6, 0], [7, 6]])
print(imp.transform(X_test))  # [[ 4. 2.] [ 6. 3.666 [ 7. 6.]]
##################################################################
## 总结:
# 1. fit_transform() 和 transform() 区别是, 前者是训练, 后者是用训练好的训练器对其他的进行转换
# 2. fit() 返回的是训练器, 并没有返回数据, fit_transform() = fit() + transform()
