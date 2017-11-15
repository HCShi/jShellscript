#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import seaborn as sns
##################################################################
## titanic
titanic = sns.load_dataset("titanic")
print(titanic.shape)  # (891, 15)
print(titanic.columns.values)  # ['survived' 'pclass' 'sex' 'age' 'sibsp' 'parch' 'fare' 'embarked' 'class'
# 'who' 'adult_male' 'deck' 'embark_town' 'alive' 'alone']
print(titanic.info())  # 让我回想起了 Kaggle Titanic 的比赛
# survived       891 non-null int64
# pclass         891 non-null int64
# sex            891 non-null object
# age            714 non-null float64
# sibsp          891 non-null int64
# parch          891 non-null int64
# fare           891 non-null float64
# embarked       889 non-null object
# class          891 non-null category
# who            891 non-null object
# adult_male     891 non-null bool
# deck           203 non-null category
# embark_town    889 non-null object
# alive          891 non-null object
# alone          891 non-null bool
print(titanic.values)
print(titanic.describe())
#          survived      pclass         age       sibsp       parch        fare
# count  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
# mean     0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
# std      0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
# min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
# 25%      0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
# 50%      0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
# 75%      1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
# max      1.000000    3.000000   80.000000    8.000000    6.000000  512.329200
##################################################################
## factorplot(x=None, y=None, hue=None, data=None): hue 色相
# kind : {``point``, ``bar``, ``count``, ``box``, ``violin``, ``strip``}
# palette : {deep, muted, bright, pastel, dark, colorblind}
g = sns.factorplot("class", "survived", "sex", data=titanic, kind="bar", palette="muted", legend=False)
g = sns.factorplot("class", "survived", "sex", data=titanic, palette="muted", legend=False)
g = sns.factorplot("class", "survived", "sex", data=titanic, legend=False)
g = sns.factorplot("class", "survived", "sex", data=titanic)  # 有 legend 反而不好看
# x, y, hue : names of variables in ``data``: Inputs for plotting long-form data. See examples for interpretation.
plt.show()
