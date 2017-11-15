#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import numpy as np  # 一般搭配两个在一起练习
##################################################################
## Pandas 两个数据结构: Series 和 DataFrame
# Series 会自动添加 序号 和 dtype
s = pd.Series([1, 3, 7, np.nan, 44, 1]); print(s)  # 序列; 类似于 numpy 中的一维
print(type(s))  # <class 'pandas.core.series.Series'>
data = pd.Series(np.random.randn(10), index=np.arange(10)); print(data)
# Series 很少用到, 可以忽略了...
##################################################################
## DateFrame; index 行标签; columns 列标签
dates = pd.date_range('20160101', periods=6); print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('abcd')); print(df)
print(type(df))  # <class 'pandas.core.frame.DataFrame'>
df1 = pd.DataFrame(np.arange(12).reshape((3, 4))); print(df1)  # 会有默认的标签, 行标, 列标都是 0, 1, 2, 3
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D' : np.array([3] * 4, dtype='int32'),
                    'E' : pd.Categorical(["test", "train", "test", "train"]),
                    'F' : 'foo'}); print(df2)  # index: 0123; columns: ABCDEF; 这种方式很少用
##################################################################
## DateFrame 一般预览数据顺序
print(df.shape)  # (6, 4); 重写了 numpy 的 ndarray
print(df.dtypes, '\n', df.index.values, '\n', df.columns.values)  # 每列都有自己的数据类型, 列序号, 数据名称
print(df.info())  # 按 列(属性) 进行分析, 可以查看那个数据有缺失值, 是否有空置, 类型
# DatetimeIndex: 6 entries, 2016-01-01 to 2016-01-06
# Freq: D
# Data columns (total 4 columns):
# a    6 non-null float64         # 顺序依次为 column, 当前属性属性值的个数, 是否有空值, 数值类型
# b    6 non-null float64
# c    6 non-null float64
# d    6 non-null float64
# dtypes: float64(4)
# memory usage: 240.0 bytes
# None
print(df2.describe())  # 数据总结; 按 列/属性 来进行分析
#          A    C    D  # 将非数字的列省去了
# count  4.0  4.0  4.0
# mean   1.0  1.0  3.0  # 平均值
# std    0.0  0.0  0.0  # 方差
# min    1.0  1.0  3.0
# 25%    1.0  1.0  3.0
# 50%    1.0  1.0  3.0
# 75%    1.0  1.0  3.0
# max    1.0  1.0  3.0
print(df.describe().mean())  # 可以输出统计的各项值
print(df.head().values)  # 输出 n=5 个, 类似于 shell 的 head
print(df[:1].values)  # 要用 slice, 否则就是第一个 column
##################################################################
## 修改属性
df2.columns = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff']; print(df2.head())  # 将 Column 进行修改

## 简单操作
print(df2.T)  # transpose 数据翻转
print(df2.sort_index(axis=1, ascending=False))  # axis=1 表示对列的名称排序; ascending=False 表示降序
print(df2.sort_values(by='E'))  # 对数据 值 排序输出

## 将 DataFrame 数据转为 list, 方便单独列保存
print(type(df2.A.values))  # <class 'numpy.ndarray'>
print(list(df2.A.values))  # [1.0, 1.0, 1.0, 1.0]
print(type(list(df2.A.values)))  # <class 'list'>
print(df2.A.values.tolist())  # 也可以用内置的函数
