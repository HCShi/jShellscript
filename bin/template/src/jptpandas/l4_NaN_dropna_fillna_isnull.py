#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import numpy as np
dates = pd.date_range('20130101', periods=6)
tmp_df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=list('ABCD')); print(tmp_df)
tmp_df.iloc[0,1] = np.nan; tmp_df.iloc[1,2] = np.nan; print(tmp_df)  # 显示有两个 NaN
##################################################################
## dropna(axis=0, how='any', thresh=None, subset=None, inplace=False) method of pandas.core.frame.DataFrame instance
# how : {'any', 'all'} any NA values are present, drop that label; all values are NA, drop that label
print(df.dropna())
## fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs) method of pandas.core.frame.DataFrame instance
print(df.fillna(0))  # 代替成 0
print(df.fillna('NULL'))
## pd.isnull(obj)
print(pd.isnull(df))  # 判断是否有缺失数据 NaN, 为 True 表示缺失数据
## ffill(axis=None, inplace=False, limit=None, downcast=None) method of pandas.core.frame.DataFrame instance
print(df.ffill())  # 用上面的值填充
## bfill(axis=None, inplace=False, limit=None, downcast=None) method of pandas.core.frame.DataFrame instance
print(df.bfill())  # 用下面的值填充
##################################################################
## 高级应用
## 判断是否含有空值
print(tmp_df.isnull())  # 每个值都检查
print(tmp_df.isnull().any())  # 上面输出二维的, 这里输出一维的, 以 feature 为单位
print(tmp_df.isnull().any().any())  # True; 这里输出一个值, False 表示没有空值, True 表示有空值; 常用这个, 意思是只要有一个为空, 就返回 True
print(tmp_df.isnull().sum())  # 还是按 feature 来统计
print(tmp_df.isnull().any().sum())  # 2; 总的个数
print(tmp_df.isnull().B.sum())  # 1; 对单独属性来统计

## 找出存在 Nan 的行, isnull() 会将每一个元素是否为空标记出, 这里是要找出该行
print(tmp_df.isnull())
print(tmp_df.isnull().any())  # 是按 feature 来统计, axis = 0
print(tmp_df.isnull().T.any())  # 这样就是按 index 来统计了
print(tmp_df.isnull().T.any().T)  # 这里就不用转置了..., 没用
print(tmp_df[tmp_df.isnull().T.any()])  # 很完美
