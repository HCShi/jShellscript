#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import numpy as np
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=list('ABCD'))
print(df)
##################################################################
## 处理数据会产生空的或者是 NaN 数据, 如何删除或者是填补这些 NaN
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan  # 把两个位置置为空
print(df)  # 显示有两个 NaN
##################################################################
## dropna(), fillna(), isnull() 都不会影响原始数据
# 直接去掉有 NaN 的行或列, 可以使用 dropna; 并没有在原数据上进行修改
print(df.dropna(axis=0, how='any'))   # how={'any', 'all'}
print(df)  # 原始数据没有变
# 将 NaN 的值用其他值代替, 比如代替成 0
print(df.fillna(value=0))
print(df.fillna(value='NULL'))
# 判断是否有缺失数据 NaN, 为 True 表示缺失数据
print(pd.isnull(df))
