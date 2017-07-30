#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import numpy as np
# 建立 6x4 的矩阵数据
dates = pd.date_range('20130101', periods=6); print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D']); print(df)
##################################################################
## 选择数据的方法有很多种, 一般我们会用到这几种
## 1.简单的筛选 2.根据标签: loc 3.根据序列: iloc 4.根据混合的这两种: ix 5.通过判断的筛选
# 1. 简单筛选
print(df['A'], '\n', df.A)  # 两种方法相同
print(df[0:3], '\n', df['20130102':'20130104'])  # 前者是左闭右开, 后者是两边都闭合
# 2. select by label: loc
print(df.loc['20130102'])  # 一个参数: 选择一行或几行; 也可以用下面的两个参数
print(df.loc[:, ['A','B']])  # : 表示所有行, 然后选择其中的一列或几列
print(df.loc['20130102', ['A','B']])
# 3. select by position: iloc
print(df.iloc[3])  # 行
print(df.iloc[3, 1])  # 行 + 列
print(df.iloc[3:5, 0:2])  # 连续行 + 连续列
print(df.iloc[[1, 2, 4], [0, 2]])  # 跨行 + 跨列
# 4. mixed selection: ix
print(df.ix[:3, ['A', 'C']])
# 5. Boolean indexing
print(df[df.A > 0])
