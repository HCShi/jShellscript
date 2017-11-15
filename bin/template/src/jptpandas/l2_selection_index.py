#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import numpy as np
# 建立 6x4 的矩阵数据
dates = pd.date_range('20130101', periods=6); print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D']); print(df)
##################################################################
## 单独 list 索引在列上, slice 索引作用在行上
print(df[df.columns]); print(df)  # 两个效果相同
print(df['A']); print(df[df.columns[0]])  # 返回值一样
# 上面说明 单独的一个索引 是以列来进行索引, 但是可以用 list 来筛选列的索引
print(df[df.columns[-2:]])  # 后两列
print(df[['A', 'C']])  # 也可以手动指定, 注意这里是两层 [[]]

# print(df[1])  # 报错, 不能单独使用数字索引
print(df[0:3])  # 按行索引

print(df['A'][0])  # -0.097288860711; 可以这样来索引
# print(df[0]['A'])  # KeyError: 0; 说明 Pandas 是 先列后行

print(df.A)  # 直接用 列的 label 来访问

print(df.iloc[:, 1:3])  # 这里和 Numpy 中访问顺序一样, 先行后列, 所以一般优先使用这中方式
print(df.loc[:, ['A', 'B']])  # 如果是想用 label, 也可以这样
# print(df.loc[0, ['A', 'B']])  # 报错, 不能用 数字index, 但可以用 :; 换下面的 ix

# 下面是最常用的 ix
print(df.ix[:, 1:3])
print(df.ix[0, ['A', 'B']])
print(df.ix[:, ['A', 'B']])
##################################################################
## 系统介绍几种索引方法
## 1.简单的筛选 2.根据标签: loc 3.根据序列: iloc 4.根据混合的这两种: ix 5.通过判断的筛选
# 总有你想要的索引方式
# 1. 简单筛选
print(df['A'], '\n', df.A)                       # 两种方法相同
print(df[0:3], '\n', df['20130102':'20130104'])  # 两边都闭合, 但默认是对列进行索引, 第二个用了日期, 所以对行索引; **header 也输出来了**
# print(df[0])  # KeyError: 0; 能 [0:3], 居然不能 [0], 好奇葩

# 2. select by label: loc
print(df.loc['20130102'])    # 一个参数: 选择一行或几行; 也可以用下面的两个参数
print(df.loc[:, ['A','B']])  # : 表示所有行, 然后选择其中的一列或几列
print(df.loc['20130102', ['A','B']])
print(df.loc[:])
# print(df.loc[0])  # 不能用整数索引(见 iloc[]), 也不能用列标索引
# print(df.loc['A'])  # KeyError: 'the label [A] is not in the [index]'

# 3. select by position: iloc
print(df.iloc[3])                  # 行
print(df.iloc[3, 1])               # 行 + 列
print(df.iloc[3:5, 0:2])           # 连续行 + 连续列
print(df.iloc[[1, 2, 4], [0, 2]])  # 跨行 + 跨列

# 4. mixed selection: ix
print(df.ix[:3, ['A', 'C']])

# 5. Boolean indexing
print(df[df.A > 0])
##################################################################
## index[]
# 一行
print(df.A[df.B != 0])  # 原理就是下边那行
print(np.array([1, 2, 3]) != 2)  # [ True False  True]

## 第一个关键词非空的列表
df = pd.DataFrame([['abc', 'def'], ['', 'hello'], ['diffu']]); print(df)
print(df.iloc[:, 0])  # 0      abc 1 2    diffu
print(df.index)  # RangeIndex(start=0, stop=3, step=1); 这就是默认支持的 index
print(pd.isnull(['a', 'b']))  # [False False]; 支持 list
print(~pd.isnull(df.iloc[:, 0]))  # 0    True 1    True 2    True
index = df.index[~pd.isnull(df.iloc[:, 0])]; print(index)  # Int64Index([0, 1, 2], dtype='int64')
print(df.iloc[index, 0].tolist());  # ['abc', '', 'diffu'];

## 自己的 index, 要用 ix()
df.index = list('abc'); print(df.index.values)  # ['a' 'b' 'c']
print(df.iloc[:, 0])  # a      abc b c    diffu; 还是第一列, 不是 index
index = df.index[~pd.isnull(df.iloc[:, 0])]; print(index)  # Index(['a', 'b', 'c'], dtype='object'); 这里是 abc, 不能再用索引了
# print(df.iloc[index, 0].tolist());  # TypeError: '>=' not supported between instances of 'str' and 'int'; 因为是 abc, 不是 123
print(df.ix[index, 0].tolist());  # ['abc', '', 'diffu']
##################################################################
## regex
tmp_df = pd.read_csv('./student.csv'); print(tmp_df.head())
print(tmp_df.filter(regex='Studen*|nam*').head())  # 将 columns 筛选出来; regex= 必须写上去
