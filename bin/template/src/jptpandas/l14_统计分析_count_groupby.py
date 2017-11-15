#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
tmp_df = pd.read_csv('student.csv')
tmp_df['young'] = tmp_df.age.apply(lambda x: x < 25)
print(tmp_df.head())
tmp_df.plot(kind='bar'); plt.show()  # 横坐标是 index, 纵坐标是 Number/Bool 的属性的属性值; 所以属性值最好归一化, 或者单一属性分析
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
tmp_df.gender.value_counts().plot('bar')
plt.show()
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
## groupby
# 按 gender 来分类, 其他属性的个数
tmp = tmp_df.groupby('gender'); print(tmp)
print(tmp.count())
# 按 ['name', 'gender'] 两个属性来联合分类, 其他属性的个数
tmp = tmp_df.groupby(['name', 'gender']); print(tmp)
print(tmp.count())
print(tmp.count().age)  # 还可以查看单一的属性, 但所有的 其他属性的分布是一样的, 所以这里只是相当于取其中一列
