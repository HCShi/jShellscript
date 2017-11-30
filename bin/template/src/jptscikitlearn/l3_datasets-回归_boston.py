#!/usr/bin/python3
# coding: utf-8
from sklearn import datasets
##################################################################
## boston
# 该数据集有 506 条数据, 每条数据包含 13 个特征变量和对应的房屋价格; 其中, 特征变量包含房屋所在位置的人口比例、交通方便程度、空气质量等
boston = datasets.load_boston()
print(dir(boston))  # ['DESCR', 'data', 'feature_names', 'target']
print(boston.feature_names)  # ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']
print(boston.data.shape, boston.data[0])  # (506, 13) [  6.32000000e-03   1.80000000e+01   2.31000000e+00   0.00000000e+00 ... 4.98000000e+00]
print(boston.target.shape, boston.target[:5])  # (506,) [ 24.   21.6  34.7  33.4  36.2]
