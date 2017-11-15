#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import numpy as np
# 建立 6x4 矩阵
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'])
##################################################################
## 修改数据
# 利用索引或者标签确定需要修改值的位置
df.iloc[2, 2] = 1111
df.loc['2013-01-03', 'D'] = 2222
df['2013-01-03', 'D'] = 3333  # 这样的效果是额外添加了一列...
df.B[df.A > 4] = 0  # 更改 B 中的数, 而更改的位置是取决于 A 的. 对于 A 大于 4 的位置. 更改 B 在相应位置上的数为 0
df['F'] = np.nan  # 添加新的一列
df['G']  = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130101', periods=6))  # 可以加上 Series 序列 (但是长度必须对齐)
print(df)
##################################################################
## 需要小范围数据进行测试时, 截取一小部分
tmp_df = df.head(); print(tmp_df)
print(tmp_df.shape)  # (5, 7)
