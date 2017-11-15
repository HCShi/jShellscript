#!/usr/bin/python3
# coding: utf-8
import seaborn as sns
##################################################################
## tips, 吸烟与消费相关
tips = sns.load_dataset("tips")
print(type(tips))  # <class 'pandas.core.frame.DataFrame'>
print(tips.shape)  # (244, 7)
print(tips.columns.values)  # ['total_bill' 'tip' 'sex' 'smoker' 'day' 'time' 'size']
print(tips.info())
# total_bill    244 non-null float64
# tip           244 non-null float64
# sex           244 non-null category
# smoker        244 non-null category
# day           244 non-null category
# time          244 non-null category
# size          244 non-null int64
print(tips.values)  # [[16.99 1.01 'Female' ..., 'Sun' 'Dinner' 2], ...]
print(tips.describe())  # 只统计数值型的
#        total_bill         tip        size
# count  244.000000  244.000000  244.000000
# mean    19.785943    2.998279    2.569672
# std      8.902412    1.383638    0.951100
# min      3.070000    1.000000    1.000000
# 25%     13.347500    2.000000    2.000000
# 50%     17.795000    2.900000    2.000000
# 75%     24.127500    3.562500    3.000000
# max     50.810000   10.000000    6.000000
##################################################################
## jointplot(x, y, data=None, color=None, size=6): Draw a plot of two variables with bivariate and univariate graphs.
# kind : { "scatter" | "reg" | "resid" | "kde" | "hex" }
# 'reg': Add regression and kernel density fits
color = sns.color_palette()[2]  # palette=None
g = sns.jointplot("total_bill", "tip", data=tips, kind="reg", color=color, size=7)
g.ax_joint.set(xlim=(0, 70), ylim=(0, 12))  # x, y 范围
plt.show()
