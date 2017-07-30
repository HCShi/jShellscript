#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import numpy as np  # 一般搭配两个在一起练习
##################################################################
## Pandas 两个数据结构: Series 和 DataFrame
# Series 会自动添加 序号 和 dtype
s = pd.Series([1, 3, 7, np.nan, 44, 1]); print(s)  # 序列; 类似于 numpy 中的一维
# date_range 会生成 '2016-01-01' 到 '2016-01-06' 六组数据
dates = pd.date_range('20160101', periods=6); print(dates)  # 时间序列
##################################################################
## DateFrame; index 行标签; columns 列标签
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd']); print(df)
df1 = pd.DataFrame(np.arange(12).reshape((3, 4))); print(df1)  # 会有默认的标签
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D' : np.array([3] * 4, dtype='int32'),
                    'E' : pd.Categorical(["test", "train", "test", "train"]),
                    'F' : 'foo'}); print(df2)
##################################################################
## DateFrame 简单应用
print(df['b'])  # 查看列的数据
print(df2.dtypes, '\n', df2.index, '\n', df2.columns)  # 每列都有自己的数据类型, 列序号, 数据名称
print(df2.values)  # 查看数据
##################################################################
## 简单操作
print(df2.describe())  # 数据总结
#          A    C    D  # 将非数字的列省去了
# count  4.0  4.0  4.0
# mean   1.0  1.0  3.0  # 平均值
# std    0.0  0.0  0.0  # 方差
# min    1.0  1.0  3.0
# 25%    1.0  1.0  3.0
# 50%    1.0  1.0  3.0
# 75%    1.0  1.0  3.0
# max    1.0  1.0  3.0
print(df2.T)  # transpose 数据翻转
print(df2.sort_index(axis=1, ascending=False))  # axis=1 表示对列的名称排序; ascending=False 表示降序
print(df2.sort_values(by='E'))  # 对数据 值 排序输出
