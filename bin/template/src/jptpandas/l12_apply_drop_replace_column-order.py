#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import numpy as np
data = pd.read_csv('student.csv'); print(data)  # # <class 'pandas.core.frame.DataFrame'>; 会根据读入的格式来确定数据类型
##################################################################
## apply(func) Additional keyword arguments will be passed as keywords to the function
data['name_length'] = data['name'].apply(len); print(data.head())  # 添加长度属性
tmp = lambda x: len(x)
data['name_length2'] = data['name'].apply(tmp); print(data.head())  # 还可以这样玩
data['name_age'] = np.where(data['name'] == data['age'], 1, 0)  # 两列影响一列, 但还是对矩阵操作, 没有针对单个元素
print(data)

# 查看 apply 内部运行原理
data['name2'] = data[data.columns[1:3]].apply(lambda x: print(x))
data['name2'] = data[data.columns[1:3]].apply(lambda x: print(x[0]))  # 按行输出...
data['name2'] = data[data.columns[1:3]].apply(lambda x: print([word for word in x]))  # 输出下面两行
# ['Kelly', 'Clo', 'Tilly', 'Tony', 'David', 'Catty', 'M', 'N', 'A', 'S', 'David', 'Dw', 'Q', 'W']
# [22, 21, 22, 24, 20, 22, 3, 43, 13, 12, 33, 3, 23, 21]
# apply 实际应用的是 对一列列的分开运算
# 所以 apply() 是和数学计算, 并不适合事务处理

# REPL 会提示使用 loc 来操作, 不要对整列进行操作事务
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead
# See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy

# 想同时操作两列的单个元素:
data['name2'] = list(zip(data['name'], data['age']))
print(data)
##################################################################
## drop(labels, axis=0, inplace=False); 默认是按行, 不替换原来的
print(data.drop([0]).head())                                           # 默认按行索引删除, 但是原始数据没变
print(data.drop(['name_length2'], axis=1).head()); print(data.head())  # 按列索引删除, 按行或者按列 都需要用 ['name', 'name'] 的 list 格式
data.drop(['name_length2'], axis=1, inplace=True); print(data.head())  # 原来的被替换了
##################################################################
## replace()
print(data.replace('1104', 'jrp'))  # 并没有影响源数据
print(data)
data['tmp'] = data['name'].replace('Catty', 'jrp').apply(lambda x: 1 if x == 'jrp' else 0)  # 这里的 replace 也没有影响原始值, 但是可以形成新的数据
print(data['tmp'])
##################################################################
## 调整 columns order
import pandas as pd
data = pd.read_csv('student.csv'); print(data)  # # <class 'pandas.core.frame.DataFrame'>; 会根据读入的格式来确定数据类型
print(data.columns.values)  # ['Student ID' 'name' 'age' 'gender']
data = data[['Student ID', 'name', 'gender', 'age']]; print(data.columns.values)  # ['Student ID' 'name' 'gender' 'age']

# 使用 slice 来交换
cols = data.columns.tolist(); print(cols)  # ['Student ID', 'name', 'gender', 'age']
data = data[cols[-1:] + cols[:-1]]; print(data.columns.values)  # ['age' 'Student ID' 'name' 'gender']
data = data[-1:] + data[:-1]; print(data.columns.values)  # ['age' 'Student ID' 'name' 'gender']; 直接操作 data[-1:] 没用, 要用 cols
