#!/usr/bin/python3
# coding: utf-8
# 处理到这里了 https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-6-pd-concat/
import pandas as pd
import numpy as np
##################################################################
## axis 默认为 0, 表示纵向合并; ignore_index 默认为 False, True 表示忽略原来的 index
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=list('abcd')); print(df1)
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=list('abcd')); print(df2)
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=list('abcd')); print(df3)
res = pd.concat([df1, df2, df3], ignore_index=True); print(res)
res = pd.concat([df1, df2, df3], ignore_index=False); print(res)
res = pd.concat([df1, df2, df3], axis=1); print(res)  # 横向连接
##################################################################
## join 默认为 'outer', 按照 columns 来合并, 有相同 index 的 column 合并到一起, 其他的独自成列
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3]); print(df1)
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4]); print(df2)
res = pd.concat([df1, df2], axis=1, join='outer'); print(res)  # 空位置用 Nan 填充
res = pd.concat([df1, df2], axis=1, join='inner'); print(res)  # 只有相同的 index 合并到一起, 其他的被抛弃
##################################################################
## join_axes 指定合并的方式
res = pd.concat([df1, df2], axis=1, join_axes=[df1.index]); print(res)  # 按照 df1.index 合并
##################################################################
## append 只有纵向合并, 没有横向合并
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd']); print(df1)
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd']); print(df2)
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4]); print(df2)
res = df1.append(df2, ignore_index=True); print(res)
res = df1.append([df2, df3]); print(res)
# 合并 series
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']); print(s1)
res = df1.append(s1, ignore_index=True); print(res)
