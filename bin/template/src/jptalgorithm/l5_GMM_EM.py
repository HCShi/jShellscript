#!/usr/bin/python3
# coding: utf-8
# 高斯混合模型的实践(高斯一元分布)
# 对于由参数未知的 K 个高斯混合模型生成的数据集, 利用 EM 算法可以对这 K 个高斯分布进行参数估计, 并且可以知道两个模型的各自比重
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
def Normal(x, mu, sigma): return np.exp(-(x - mu)**2 / (2 * sigma**2)) / (np.sqrt(2 * np.pi) * sigma)  # 一元正态分布概率密度函数; Normalize
print(Normal(np.array([1, 2]), 0, 1))  # [ 0.24197072  0.05399097]
# 下面给出 K = 2, 即由两个高斯分布组成的混合模型, 分别是男女生身高分布
# 已经给出了各自分布的比重, 参数; 用来检验算法生成的参数估计是否准确
N_boys, N_girls = 77230, 22770  # 比重 77.23%, 22.77%
N = N_boys + N_girls; print(N)  # 100000; 观测集大小
K = 2  # 高斯分布模型的数量

## 生成回归拟合数据...
## normal(loc=0.0, scale=1.0, size=None): Draw random samples from a normal (Gaussian) distribution. (均值, 标准差, shape)
# 男生身高数据
mu1, sig1 = 1.74, 0.0865; BoyHeights = np.random.normal(mu1, sig1, N_boys).reshape(-1, 1);  # 均值, 方差
print(BoyHeights.shape, BoyHeights[0])  # (77230, 1) [ 1.88050587];
# 女生身高数据
mu2, sig2 = 1.63, 0.0642; GirlHeights = np.random.normal(mu2, sig2, N_girls).reshape(-1, 1)
print(GirlHeights.shape, GirlHeights[0])  # (22770, 1) [ 1.69702944]
# 男女生数据合并
data = np.concatenate((BoyHeights, GirlHeights)); print(data.shape)  # (100000, 1); vstack

## 具体算法步骤含义见 Gaussion-Mixture-Model.org
## 也就是李航老师 第一版, 算法 9.2 的实现

## 1. 随机初始化模型参数 θ, 包括 \mu \sigma \alpha; 分别带表: 平均数, 方差, 每个模型的比例
Mu = np.random.random((1, 2)); print(Mu)  # [[ 0.53333823  0.37603887]]; 两个高斯分布的 平均值 参数
SigmaSquare = np.random.random((1, 2)); print(SigmaSquare)  # [[ 0.7139585   0.03358096]]; 两个高斯分布的 方差 参数
# 随机初始化各模型比重系数(大于等于 0, 且和为 1)
a = np.random.random(); print(a)  # 0.5918464503222021; 生成一个数
Alpha = np.array([[a, 1-a]]); print(Alpha)  # [[ 0.59184645  0.40815355]]; 两个模型的比重和为 1
## 训练的结果就是将 Alpha 模拟出来上面数据的比重 0.772 和 0.227, Mu 是上面的 mu1, mu2, SigmaSquare 是 sig1 和 sig2

for i in range(10000): # 用 EM 算法迭代求参数估计, 还是比较慢的...
    # Expectation
    gauss1 = Normal(data, Mu[0][0], np.sqrt(SigmaSquare[0][0]))  # 第一个模型
    # print(gauss1.shape, gauss1.mean(), gauss1.std())  # (100000, 1), 0.178517155216, 0.0273401382427
    gauss2 = Normal(data, Mu[0][1], np.sqrt(SigmaSquare[0][1]))  # 第二个模型
    # print(gauss2.shape, gauss2.mean(), gauss2.std())  # (100000, 1) 6.33216682479e-10 7.6559825701e-09
    Gamma1 = Alpha[0][0] * gauss1;  # (100000, 1)
    Gamma2 = Alpha[0][1] * gauss2;  # (100000, 1)
    M = Gamma1 + Gamma2  # 将两个模型混合
    # Gamma = np.concatenate((Gamma1/m, Gamma2/m), axis=1)  # 元素 (j, k) 为第 j 个样本来自第 k 个模型的概率, 聚类时用来判别样本分类
    ## 上面这几步非常重要, 和公式结合起来看...

    # Maximization
    # 更新 SigmaSquare
    SigmaSquare[0][0] = np.dot((Gamma1/M).T, (data-Mu[0][0])**2)/np.sum(Gamma1/M)
    SigmaSquare[0][1] = np.dot((Gamma2/M).T, (data-Mu[0][1])**2)/np.sum(Gamma2/M)
    # 更新 Mu
    Mu[0][0]          = np.dot((Gamma1/M).T, data)/np.sum(Gamma1/M)
    Mu[0][1]          = np.dot((Gamma2/M).T, data)/np.sum(Gamma2/M)
    # 更新 Alpha
    Alpha[0][0]       = np.sum(Gamma1/M)/N
    Alpha[0][1]       = np.sum(Gamma2/M)/N
    if(i % 100 == 0):
        print("第", i, "次迭代:")
        print("Mu:", Mu)
        print("Sigma:", np.sqrt(SigmaSquare))
        print("Alpha", Alpha)
    # 训练到 10000 轮的时候效果显示很好
