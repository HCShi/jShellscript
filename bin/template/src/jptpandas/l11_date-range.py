#!/usr/bin/python3
# coding: utf-8
import pandas as pd
import numpy as np
##################################################################
## date_range()
dates = pd.date_range('20160101', periods=6); print(dates)  # 会生成 '2016-01-01' 到 '2016-01-06' 六组数据
print(type(dates))  # <class 'pandas.tseries.index.DatetimeIndex'>
print(dates.year, dates.month, dates.day)  # [2016 2016 2016 2016 2016 2016] [1 1 1 1 1 1] [1 2 3 4 5 6]
print(dates.date)  # [datetime.date(2016, 1, 1) datetime.date(2016, 1, 2), ...]
# 还是不知道怎么找到类似于下面的 2016-01-01
##################################################################
## 与 DataFrame 结合
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D']); print(df)
#              A   B   C   D
# 2016-01-01   0   1   2   3
# 2016-01-02   4   5   6   7
# 2016-01-03   8   9  10  11
# 2016-01-04  12  13  14  15
# 2016-01-05  16  17  18  19
# 2016-01-06  20  21  22  23
