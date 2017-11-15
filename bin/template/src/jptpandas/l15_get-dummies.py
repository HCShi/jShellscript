#!/usr/bin/python3
# coding: utf-8
import pandas as pd
##################################################################
## 处理 DataFrame()
tmp_df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'], 'C': [1, 2, 3]}); print(tmp_df)
#    A  B  C
# 0  a  b  1
# 1  b  a  2
# 2  a  c  3
print(pd.get_dummies(tmp_df))  # 可以看到会把非数值的转化为数值的, C 没有变化
#    C  A_a  A_b  B_a  B_b  B_c
# 0  1    1    0    0    1    0
# 1  2    0    1    1    0    0
# 2  3    1    0    0    0    1
print(pd.get_dummies(tmp_df, prefix=['col1', 'col2']))  # 自定义 columns
#    C  col1_a  col1_b  col2_a  col2_b  col2_c
# 0  1       1       0       0       1       0
# 1  2       0       1       1       0       0
# 2  3       1       0       0       0       1
print(pd.get_dummies(tmp_df.C))  # 单独使用 C, 就会把 C 分开
#    1  2  3
# 0  1  0  0
# 1  0  1  0
# 2  0  0  1
print(pd.get_dummies(tmp_df.C, prefix='C'))  # 单个属性, prefix 就很重要
#    C_1  C_2  C_3
# 0    1    0    0
# 1    0    1    0
# 2    0    0    1
##################################################################
## 处理 list
s1 = ['a', 'b', np.nan]
print(pd.get_dummies(s1))
#    a  b
# 0  1  0
# 1  0  1
# 2  0  0
print(pd.get_dummies(s1, dummy_na=True))
#    a  b  NaN
# 0  1  0    0
# 1  0  1    0
# 2  0  0    1
##################################################################
## 处理 Series()
tmp_s = pd.Series(list('abca')); print(tmp_s)
# 0    a
# 1    b
# 2    c
# 3    a
print(pd.get_dummies(tmp_s))
#    a  b  c
# 0  1  0  0
# 1  0  1  0
# 2  0  0  1
# 3  1  0  0
print(pd.get_dummies(pd.Series(list('abcaa')), drop_first=True))
#    b  c
# 0  0  0
# 1  1  0
# 2  0  1
# 3  0  0
# 4  0  0
