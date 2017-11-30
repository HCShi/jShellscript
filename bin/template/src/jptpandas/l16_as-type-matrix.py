#!/usr/bin/python3
# coding: utf-8
import pandas as pd
tmp_df = pd.read_csv('./student.csv'); print(tmp_df.head())
##################################################################
## as-matrix; 一般用不到, 因为内部实现了相关的方法来进行表达, 不用特意转化
print(tmp_df.head().as_matrix())
# [[1100 'Kelly' 22 'Female']
#  [1101 'Clo' 21 'Female']
#  [1102 'Tilly' 22 'Female']
#  [1103 'Tony' 24 'Male']
#  [1104 'David' 20 'Male']]
print(type(tmp_df.head().as_matrix()))  # <class 'numpy.ndarray'>
print(tmp_df.head().as_matrix().shape)  # (5, 4)
##################################################################
## as-type
tmp_df.age = tmp_df.age.astype(float)
print(tmp_df.head())
