#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt  # 只用 plt.show() 才会用到 matplotlib
import numpy as np
tmp_df = pd.read_csv('student.csv')
tmp_df['young'] = tmp_df.age.apply(lambda x: x < 25)
print(tmp_df.head())
##################################################################
## plot 包括两种 FramePlotMethods(BasePlotMethods) 和 SeriesPlotMethods(BasePlotMethods), 参数不同
# stacked : boolean, default False in line and bar plots, and True in area plot. If True, create stacked plot.
# .size() 中有 labels 等参数, 是 pie() 或 plot(kind='pie') 中的
tmp_df.plot(kind='bar'); plt.show()  # 横坐标是 index, 纵坐标是 Number/Bool 的属性的属性值; 所以属性值最好归一化, 或者单一属性分析

## Series: s.plot(kind='line', stacked=False); ** Series 可以直接 plot('kde'), DataFrame 就不行 **
## 随机生成 1000 个数据, Series 默认的 index 就是从 0 开始的整数, 这里显式赋值看的更清楚
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()  # 为了方便观看效果, 我们累加这个数据; 功能就是将前面的数据进行累加并且替换
data.plot(); plt.show()  # 我们可以使用 plt.plot(x=, y=), 把 x, y 的数据作为参数存进去, 但是 data 本来就是一个数据

## DataFrame: df.plot(x, y, kind='line', stacked=False)
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))  # header 就是 ABCD
data = data.cumsum(); print(data)
data.plot(); plt.show()  # 有 4 组数据, 所以 4 组数据会分别 plot 出来

## plot methods: 'bar', 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie'
## df.plot.hist(by=None, bins=10, **kwds) method of pandas.plotting._core.FramePlotMethods instance
# bins: integer, default 10; Number of histogram bins to be used; 画多少个 hist 柱子
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
data.plot(bins=50, kind='hist'); plt.show()  # 所有挤在一块
data['A'].plot(bins=50, kind='hist'); plt.show()  # plot() 不支持 column 参数
data['A'].plot.hist(bins=50); plt.show()  # plot() 都可以把 kind 提出来, 但还是不支持 column 参数
# df.hist() 支持更多参数, ** 不是 plot.hist() 或 plot(kind='hist') **
# hist_frame(column=None, by=None, grid=True, xlabelsize=None, xrot=None, ylabelsize=None, yrot=None,
#    ax=None, sharex=False, sharey=False, figsize=None, layout=None, bins=10, **kwds)
data.hist(column='A', bins=50, figsize=(10, 4)); plt.show()
data.hist(column=['A', 'B'], bins=50, figsize=(10, 4)); plt.show()  # 分成两个图
data = pd.DataFrame(np.random.randn(10, 4), index=np.arange(10), columns=list("ABCD")); print(data)
data.hist(column='A', by='B', bins=50, figsize=(10, 4)); plt.show()  # 按照 B 来分类, 每一类在按 A 来画图

## df.plot.scatter(x, y, s=None, c=None, **kwds); 没有 df.scatter(), 还是 hist() 厉害...
# scatter 只有 x, y 两个属性, 我们我们就可以分别给 x, y 指定数据
# 然后我们在可以再画一个在同一个 ax 上面, 选择不一样的数据列, 不同的 color 和 label
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label="Class 1")
data.plot.scatter(x='A', y='C', color='LightGreen', label='Class 2', ax=ax); plt.show()

## pie(lables=None, autopct=None, title=None, legend=False)
# autopct='%.2f' 可以控制小数精度
data = pd.DataFrame(np.random.randn(10, 4), index=np.arange(10), columns=list("ABCD")); print(data)
print(data.groupby('A').size(), type(data.groupby('A').size()))  # <class 'pandas.core.series.Series'>
data.groupby('A').size().plot.pie(); plt.show()

## 1. DataFrame 对象很乱, df.hist(), df.plot.hist() 参数不同; 没有 df.scatter(), 只能用 df.plot.scatter() 或 df.plot(kind='scatter')
## 2. df.plot(kind='pie') 和 plot.pie() 参数相同
##################################################################
## count mean
print(tmp_df.count())  # 行数
print(tmp_df.count(axis=1))  # 每行多少列
print(tmp_df.count(axis=1).mean())  # 每行平均多少列
## 画图看 性别和年龄, 因为要用两个属性, 所以不能通过属性来调用了
plt.scatter(np.where(tmp_df.gender == 'Female', 1, 0), tmp_df.age)  # x, y 都必须是 数值化
plt.show()
## 各性别的年龄分布; Kernel Density Estimation (KDE), 根据已有的插值填充
tmp_df.age[tmp_df.gender == 'Female'].plot('kde')
tmp_df.age[tmp_df.gender == 'Male'].plot('kde')
plt.show()
## 画图统计性别            # 单个属性的 value_counts() 画图
print(tmp_df.gender.value_counts())  # Male      7, Female    7; 属性按属性值分类, 并统计个数
tmp_df.gender.value_counts().plot('bar'); plt.show()
## 是否青春期的男女分布    # 两个属性之间的条件 plot()
male = tmp_df.young[tmp_df.gender == 'Male'].value_counts(); print(male)  # True     5; False    2
female = tmp_df.young[tmp_df.gender == 'Female'].value_counts(); print(female)  # True    7; 这个没有大于 25 的
tmp = pd.DataFrame({'male': male, 'female': female}); print(tmp)
tmp.plot(kind='bar', stacked=True)  # 所以是按 index 为横坐标来画的; 自动带 legand
plt.xlabel('young'); plt.ylabel('number of male or female'); plt.show()  # 看到男性才有 >25 岁的
tmp.plot(kind='bar'); plt.show()  # 不用 stacked 也很好看
# 可以想象, plot 横坐标是个体的编号并按属性来依次排开, 纵坐标是每个个体的属性的属性值
##################################################################
## DataFrame 神级别应用
tmp_words = [['hello', 'word'], ['i', 'love', 'you'], ['1', '2', '3', '4']]
tmp_df = pd.DataFrame(tmp_words)
print(tmp_df.count(axis=1).mean())  # 3; 每句话平均词数
print(tmp_df.count(axis=1).max())  # 4;
# 其实用普通方法也可以
print(min([len(line) for line in tmp_words]))  # 2
##################################################################
## groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, **kwargs) method of pandas.core.frame.DataFrame instance
tmp_df = pd.read_csv('student.csv'); print(tmp_df)
## 单个属性分类
# 属性和方法
tmp = tmp_df.groupby('gender'); print(tmp)  # <pandas.core.groupby.DataFrameGroupBy object at 0x7ffb5991a518>
print(type(tmp))  # <class 'pandas.core.groupby.DataFrameGroupBy'>
print(type(tmp.age))  # <class 'pandas.core.groupby.SeriesGroupBy'>
print(tmp.all())  # 查看所有的, 会显示 True, False
print(tmp.groups)  # {'Female': Int64Index([0, 1, 2, 5, 6, 11, 13], dtype='int64'), 'Male': Int64Index([3, 4, 7, 8, 9, 10, 12], dtype='int64')}
print(tmp.get_group('Male'))  # 把上面的 'Male': Index 中的都列出来了
print(tmp.ngroup())  # 用 0, 1, 3, ... 来表示每个 Index 对应的组别
print(tmp.ngroups)  # 2
print(tmp.count().shape, tmp.count())  # (2, 3); 按 gender 来分类, 其他属性的个数
print(tmp.age.count().shape, tmp.age.count(), tmp.count().age)  # (2,); count().age 和 age.count() 结果一样
print(tmp.age.value_counts())  # 不同数值的统计
# 画图
tmp.plot(); plt.show()  # 只能将数值属性画出来,  两幅图, 一副表示 Male, 另一幅表示 Female; 按照 groups() 的字典画的
tmp.age.plot(); plt.show()  # 这里画到了一幅图里;  两个自变量, 一个因变量; 上面是 两个自变量, 两个因变量; 好神奇
# plot() 的横坐标一直都是 index, 但是对于不同维度的数据可能有不同的显示方式, 一副图里只能展示 ** 二维的数据 **
# 不管怎么去属性, 都会有两条线, 代表两类, 分别是 Male 和 Female

## 多属性分类
# 按 ['name', 'gender'] 两个属性来联合分类, 其他属性的个数
tmp = tmp_df.groupby(['name', 'gender']); print(tmp)
print(type(tmp))  # <class 'pandas.core.groupby.DataFrameGroupBy'>
print(type(tmp.age))  # <class 'pandas.core.groupby.SeriesGroupBy'>
print(tmp.all())
print(tmp.groups)  # {('A', 'Male'): Int64Index([8], dtype='int64'), ('Catty', 'Female'): Int64Index([5], dtype='int64'), ('Clo', 'Female'): Int64Index([1], dtype='int64'), ('David', 'Male'): Int64Index([4, 10], dtype='int64'), ('Dw', 'Female'): Int64Index([11], dtype='int64'), ('Kelly', 'Female'): Int64Index([0], dtype='int64'), ('M', 'Female'): Int64Index([6], dtype='int64'), ('N', 'Male'): Int64Index([7], dtype='int64'), ('Q', 'Male'): Int64Index([12], dtype='int64'), ('S', 'Male'): Int64Index([9], dtype='int64'), ('Tilly', 'Female'): Int64Index([2], dtype='int64'), ('Tony', 'Male'): Int64Index([3], dtype='int64'), ('W', 'Female'): Int64Index([13], dtype='int64')}
print(tmp.ngroup())
print(tmp.age.all())
print(tmp.count().shape, tmp.count())  # (13, 2)
print(tmp.age.count(), tmp.count().age)  # 还可以查看单一的属性, 但所有的 其他属性的分布是一样的, 所以这里只是相当于取其中一列
# 画图
tmp.plot(); plt.show()  # 13 幅图, 因为 tmp.count() 中有 13 个 index
tmp.age.plot(); plt.show()  # 一幅图, 本来应该有 13 条不同颜色的线, 但因为只有一个分类有 2 个, 所以只连出来一条线

## 高级用法
print(tmp_df.groupby('gender').age)  # <pandas.core.groupby.SeriesGroupBy object at 0x7ffb60f28a90>
print(tmp_df.groupby('gender').age.count())  # 并没有将重复的合并...
print(tmp_df.groupby('gender').age.value_counts())  # 并没有将重复的合并...
print(tmp_df.groupby('gender').age.unique())
# gender
# Female                     [22, 21, 3]
# Male      [24, 20, 43, 13, 12, 33, 23]
print(tmp_df.groupby('gender').age.unique().count())  # 2; 只是统计了分类的个数...
print(tmp_df.groupby('gender').age.unique().shape)  # (2,)
print(tmp_df.groupby('age').gender.count())
print(tmp_df.groupby('age').count())

## apply()
print(tmp_df.groupby('gender').all())
def feature_count(group):
    dct_cnt = {}
    dct_cnt['age_c'] = group['age'].unique().shape[0]
    dct_cnt['age_mean'] = np.mean(group['age'].value_counts())
    dct_cnt['gender_c'] = group.shape[0]
    dct_cnt = pd.Series(dct_cnt)
    return dct_cnt
cnt_gender = tmp_df.groupby('gender').apply(feature_count); print(cnt_gender)
print(cnt_gender.describe())
##################################################################
## size()
tmp_df = pd.read_csv('student.csv')
print(tmp_df.groupby('gender').size())
# gender
# Female    7
# Male      7
tmp_df.groupby('gender').size().plot(labels=['Female', 'Male'], kind='pie', autopct='%.2f', title='JRP', legend=True); plt.show()
##################################################################
## 筛选 和 排序: Excel 中经常用到的...
## 排序
tmp_df = pd.read_csv('student.csv'); print(tmp_df)
print(tmp_df.sort(['age']))  # 按年龄排序, 默认是增序
print(tmp_df.sort(['age'], ascending=False))  # 降序
# 两个属性排序
print(tmp_df.sort(['age', 'Student ID']))  # 第一排序字段, 第二排序字段
print(tmp_df.sort(['Student ID', 'age']))
# 年龄最小前 5 项
print(tmp_df.sort(['age']).head(5))
## 筛选
# 单列数据筛选
print(tmp_df.loc[tmp_df['age'] > 20].head())  # 找到年龄大于 20 的人
print(tmp_df.loc[tmp_df['name'] != 'Clo'].head())  # 不是 Clo 的人
print(tmp_df.loc[tmp_df['name'] != 'Clo', ['name', 'age']].head())  # 筛选, 并抽出重要的显示
# 多个筛选条件
print(tmp_df.loc[(tmp_df['name'] != 'Clo') & (tmp_df['name'] != 'Kelly')].head())  # 不是 Clo 和 Kelly 的人
# 多列筛选并排序
print(tmp_df.loc[(tmp_df['name'] == 'Clo') | (tmp_df['age'] > 20)].head())  # 不是 Clo 和 Kelly 的人
##################################################################
## sort()
# sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, by=None)
#    Sort object by labels (along an axis)
tmp_df = pd.read_csv('./student.csv'); print(tmp_df)
print(tmp_df.sort_index())  # 完全没有变化
print(tmp_df.sort_index(ascending=False))  # 按 index/行 反序
print(tmp_df.sort_index(axis=1, ascending=False))  # axis=1 表示对列的名称排序; ascending=False 表示降序
# sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last') method of pandas.core.frame.DataFrame instance
#    Sort by the values along either axis
print(tmp_df.sort_values('age'))  # 对数据 值 排序输出
print(tmp_df.sort_values(['age', 'Student ID']))  # 先按 name, 再按 id
print(tmp_df.sort_values(['age', 'Student ID']).groupby('gender'))  # <pandas.core.groupby.DataFrameGroupBy object at 0x7ffb5991a518>
print(tmp_df.sort_values(['age', 'Student ID']).groupby('gender')['age'])  # <pandas.core.groupby.SeriesGroupBy object at 0x7ffb59911400>
print(tmp_df.sort_values(['age', 'Student ID']).groupby('gender')['age'].count())
print(tmp_df.sort_values(['age', 'Student ID']).groupby('gender')['age'].all())
