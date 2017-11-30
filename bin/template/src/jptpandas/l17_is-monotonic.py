#!/usr/bin/python3
# coding: utf-8
import pandas as pd
tmp_df = pd.read_csv('./student.csv')
##################################################################
## is_monotonic: Return boolean if values in the object are
print(type(tmp_df.age))  # <class 'pandas.core.series.Series'>
print(tmp_df.age.is_monotonic)  # False
