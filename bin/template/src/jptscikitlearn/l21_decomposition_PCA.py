#!/usr/bin/python3
# coding: utf-8
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np
##################################################################
## PCA(n_components=None, copy=True, whiten=False): PCA(Principal component analysis)
# PCA 通过寻找高维空间中数据变化最快(方差最大)的方向, 对空间的基进行变换, 选取重要的空间基来对数据降维, 尽可能保持数据特征的情况下对数据进行降维
# 线性降维(Linear dimensionality reduction)使用 SVD(奇异值分解)对数据进行处理, 保留最重要的前 n 个奇异值向量(singular vectors, 似乎和特征向量不一样)
#     在较低的纬度对原数据集进行映射. PCA 类的实现使用可 scipy.linalg 来实现 SVD , 它只作用于密集矩阵(非稀疏的), 并且不能扩展到高维数据下.

# PCA 是一种数据降维技术, 用于数据预处理; 一般我们获取的原始数据维度都很高, 比如 1000 个特征, 在这 1000 个特征中可能包含了很多无用的信息或者噪声,
#     真正有用的特征才 100 个, 那么我们可以运用 PCA 算法将 1000 个特征降到 100 个特征; 这样不仅可以去除无用的噪声, 还能减少很大的计算量
# 简单来说, 就是将数据从原始的空间中转换到新的特征空间中, 例如原始的空间是三维的 (x,y,z), xyz 分别是原始空间的三个基, 我们可以通过某种方法,
#     用新的坐标系 (a,b,c) 来表示原始的数据, 那么 abc 就是新的基, 它们组成新的特征空间; 在新的特征空间中, 可能所有的数据在 c 上的投影都接近于 0,
#     即可以忽略, 那么我们就可以直接用 (a,b) 来表示数据, 这样数据就从三维的 (x,y,z) 降到了二维的 (a,b)
# 问题是如何求新的基 (a,b,c)
# 一般步骤是这样的: 先对原始数据零均值化, 然后求协方差矩阵, 接着对协方差矩阵求特征向量和特征值, 这些特征向量组成了新的特征空间
#     具体的细节, 推荐 Andrew Ng 的网页教程: Ufldl 主成分分析, 写得很详细

# 参数:
# n_components: int 或者 string, 缺省时默认为 None, 所有成分被保留; PCA 算法中所要保留的主成分个数 n, 也即保留下来的特征个数 n;
#     赋值为 string, 比如 n_components='mle', 将自动选取特征个数 n, 使得满足所要求的方差百分比
# copy: 缺省时默认为 True. 表示是否在运行算法时, 将原始训练数据复制一份. True 将保持原始数据不变, False 则直接在原始数据上进行计算
# whiten: 缺省时默认为 False. 白化, 是否使得每个特征具有相同的方差.
##################################################################
## 一: 手动实现 PCA
## 零均值化
def zeroMean(dataMat):  # 零均值化就是求每一列的平均值, 然后该列上的所有数都减去这个均值, 每个特征的均值变成 0
    meanVal = np.mean(dataMat, axis=0)  # 按列求均值, 即求各个特征的均值
    newData = dataMat - meanVal
    return newData, meanVal  # newData 是零均值化后的数据, meanVal 是每个特征的均值, 是给后面重构数据用的.
def pca(dataMat, n):
    newData, meanVal= zeroMean(dataMat)
    covMat = np.cov(newData, rowvar=0)  # 求协方差矩阵; rowvar=0, 说明传入的数据一行代表一个样本, 这个真变态
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))  # eigVals 存放特征值, 行向量; eigVects 存放特征向量, 每一列带别一个特征向量
    # 保留主要的成分, 即保留值比较大的前 n 个特征, eigVals 里面有 m 个特征值, 排序后排在前面的 n 个特征值所对应的特征向量就是我们要保留的,
    #     它们组成了新的特征空间的一组基 n_eigVect. 将零均值化后的数据乘以 n_eigVect 就可以得到降维后的数据
    eigValIndice = np.argsort(eigVals)                # 对特征值从小到大排序
    n_eigValIndice = eigValIndice[-1:-(n+1):-1]       # 最大的 n 个特征值的下标
    n_eigVect = eigVects[:, n_eigValIndice]           # 最大的 n 个特征值对应的特征向量
    lowDDataMat = newData * n_eigVect                 # 低维特征空间的数据
    reconMat = (lowDDataMat * n_eigVect.T) + meanVal  # 重构数据
    return lowDDataMat, reconMat
# 从高维的数据 dataMat 得到低维的数据 lowDDataMat, 另外, 程序也返回了重构数据 reconMat, 有些时候 reconMat 课便于数据分析.
##################################################################
## 二: 以一组二维的数据 data 为例, 一共 12 个样本(x,y), 其实就是分布在直线 y=x 上的点, 并且聚集在 x=[1,2,3,4]上, 各 3 个
# data 这组数据, 有两个特征, 因为两个特征是近似相等的, 所以用一个特征就能表示了, 即可以降到一维
data = np.array([[1, 1], [0.9, 0.95], [1.01, 1.03],
       [2, 2], [2.03, 2.06], [1.98, 1.89],
       [3, 3], [3.03, 3.05], [2.89, 3.1],
       [4, 4], [4.06, 4.02], [3.97, 4.01]])
newData = PCA(1).fit_transform(data); print(newData, data)  # 可以看到原始数据 data 并未改变, newData 是一维的, 并且明显地将原始数据分成了四类.
# [[ 2.12015916] [ 2.22617682] [ 2.09185561] [ 0.70594692] [ 0.64227841] [ 0.79795758]
#  [-0.70826533] [-0.76485312] [-0.70139695] [-2.12247757] [-2.17900746] [-2.10837406]]
# [[ 1.    1.  ] [ 0.9   0.95] [ 1.01  1.03] [ 2.    2.  ] [ 2.03  2.06] [ 1.98  1.89]
#  [ 3.    3.  ] [ 3.03  3.05] [ 2.89  3.1 ] [ 4.    4.  ] [ 4.06  4.02] [ 3.97  4.01]]
newData = PCA(1, False).fit_transform(data); print(newData, data)  # 将 copy 设置为 False, 原始数据 data 将发生改变, 并不是 1 维
# [[-1.48916667 -1.50916667] [-1.58916667 -1.55916667] [-1.47916667 -1.47916667] [-0.48916667 -0.50916667] [-0.45916667 -0.44916667] [-0.50916667 -0.61916667]
#  [ 0.51083333  0.49083333] [ 0.54083333  0.54083333] [ 0.40083333  0.59083333] [ 1.51083333  1.49083333] [ 1.57083333  1.51083333] [ 1.48083333  1.50083333]]
pca = PCA('mle'); newData = pca.fit_transform(data); print(newData)  # 'mle' 自动降到了 1 维.data 都变了, newData 训练结果还一样
# [[ 2.12015916] [ 2.22617682] [ 2.09185561] [ 0.70594692] [ 0.64227841] [ 0.79795758]
#  [-0.70826533] [-0.76485312] [-0.70139695] [-2.12247757] [-2.17900746] [-2.10837406]]
print(pca.components_)  # [[-0.70614096 -0.70807129]]  [n_components, n_features] 返回具有最大方差的成分
print(pca.n_components)  # mle                         返回所保留的成分个数 n. 当它被设为 'mle' 或者 0-1 的数字时, 表示选中方差百分比和的比重.
print(pca.explained_variance_ratio_)  # [ 0.99910873]  [n_components]返回 所保留的 n 个成分各自的方差百分比, 当 n 没有设定时, 各项的和应为 1.0
print(pca.explained_variance_)  # [ 2.7864764]
print(pca.get_params)  # <bound method PCA.get_params of PCA(copy=True, n_components=1, whiten=False)>
print(pca.noise_variance_)  # 0.00248572228227         没看懂... 似乎和一本书(或者一篇论文？)的上的内容有关.
# 我们所训练的 pca 对象的 n_components 值为 mle, 即保留 1 个特征, 该特征的方差为 2.7864764, 占所有特征的方差百分比为 0.99910873,
#     意味着几乎保留了所有的信息. get_params 返回各个参数的值.

##################################################################
## 三: iris 上测试
X_train, y_train = datasets.load_iris(True); print(X_train.shape, y_train.shape)  # (150, 4) (150,)
print(X_train[0], set(y_train))  # [ 5.1  3.5  1.4  0.2] {0, 1, 2}
pca = PCA(3); X_train = pca.fit_transform(X_train); print(X_train.shape)  # (150, 3)
print(pca.explained_variance_)  # [ 4.22484077  0.24224357  0.07852391]
print(pca.explained_variance_ratio_)  # [ 0.92461621  0.05301557  0.01718514]
print(pca.noise_variance_)  # 0.023683027126; 这个就没上面的噪声小, 说明这个没有上面那么适合 PCA
