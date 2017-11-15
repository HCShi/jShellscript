#!/usr/bin/python3
# coding: utf-8
import seaborn as sns
import matplotlib.pyplot as plt
##################################################################
## load_dataset() 有内置数据集
## iris
# 内置的 DataFrame, 所以说 Seaborn 是和 DataFrame 紧密结合的
iris = sns.load_dataset("iris")  # Load iris data
print(type(iris))  # <class 'pandas.core.frame.DataFrame'>; 居然用了 DataFrame
print(iris.columns.values)  # ['sepal_length' 'sepal_width' 'petal_length' 'petal_width' 'species']; 和 pandas 好像啊
print(iris.shape)  # (150, 5)
print(iris.info())
# Data columns (total 5 columns):
# sepal_length    150 non-null float64
# sepal_width     150 non-null float64
# petal_length    150 non-null float64
# petal_width     150 non-null float64
# species         150 non-null object
print(type(iris.values))  # <class 'numpy.ndarray'>
print(iris.values)
print(iris.describe())  # 为什么没 species 那列...
#        sepal_length  sepal_width  petal_length  petal_width
# count    150.000000   150.000000    150.000000   150.000000
# mean       5.843333     3.057333      3.758000     1.199333
# std        0.828066     0.435866      1.765298     0.762238
# min        4.300000     2.000000      1.000000     0.100000
# 25%        5.100000     2.800000      1.600000     0.300000
# 50%        5.800000     3.000000      4.350000     1.300000
# 75%        6.400000     3.300000      5.100000     1.800000
# max        7.900000     4.400000      6.900000     2.500000
##################################################################
## swarmplot(x=None, y=None, data=None): 点图, 类似于 scatter; 没有 kind 属性
# beeswarm-style: 5 个属性, 选出两个, 其他不考虑
sns.swarmplot(x="species", y="petal_length", data=iris)  # Construct iris plot
plt.show()  # Show plot
