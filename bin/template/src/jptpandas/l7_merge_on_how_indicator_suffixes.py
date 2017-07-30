#!/usr/bin/python3
# coding: utf-8
import pandas as pd
##################################################################
## merging two df by key/keys. (may be used in database); concat 只是用于合并 或者 index 相同
## 定义资料集并打印
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']}); print(left)
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']}); print(right)
res = pd.merge(left, right, on='key'); print(res)  # 依据 key 合并 column
##################################################################
## 依据两组 key; consider two keys
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']}); print(left)
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']}); print(right)
# how = ['left', 'right', 'outer', 'inner']; 默认值为 'inner'
res = pd.merge(left, right, on=['key1', 'key2'], how='inner'); print(res)  # default for how='inner'
res = pd.merge(left, right, on=['key1', 'key2'], how='left'); print(res)
##################################################################
## indicator 会将合并的记录放到新的一列
df1 = pd.DataFrame({'col1':[0, 1], 'col_left':['a', 'b']}); print(df1)
df2 = pd.DataFrame({'col1':[1, 2, 2], 'col_right':[2, 2, 2]}); print(df2)
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True); print(res)
# give the indicator a custom name
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column'); print(res)
##################################################################
## merged by index
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2']); print(left)
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']}, index=['K0', 'K2', 'K3']); print(right)
# left_index and right_index
res = pd.merge(left, right, left_index=True, right_index=True, how='outer'); print(res)
res = pd.merge(left, right, left_index=True, right_index=True, how='inner'); print(res)
##################################################################
## handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]}); print(boys)
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]}); print(girls)
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner'); print(res)
# join function in pandas is similar with merge. If know merge, you will understand join
