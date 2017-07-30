#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import numpy as np
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A', 'B', 'C', 'D'])
##################################################################
## 处理数据会产生空的或者是 NaN 数据, 如何删除或者是填补这些 NaN
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan  # 把两个位置置为空
# 直接去掉有 NaN 的行或列, 可以使用 dropna; 并没有在原数据上进行修改
print(df.dropna(axis=0, how='any'))   # how={'any', 'all'}
# 将 NaN 的值用其他值代替, 比如代替成 0
print(df.fillna(value=0))
# 判断是否有缺失数据 NaN, 为 True 表示缺失数据
print(pd.isnull(df))
