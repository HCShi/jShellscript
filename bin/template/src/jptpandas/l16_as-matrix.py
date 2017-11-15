#!/usr/bin/python3
# coding: utf-8
import pandas as pd
tmp_df = pd.read_csv('./student.csv'); print(tmp_df.head())
print(tmp_df.head().as_matrix())
# [[1100 'Kelly' 22 'Female']
#  [1101 'Clo' 21 'Female']
#  [1102 'Tilly' 22 'Female']
#  [1103 'Tony' 24 'Male']
#  [1104 'David' 20 'Male']]
print(type(tmp_df.head().as_matrix()))  # <class 'numpy.ndarray'>
print(tmp_df.head().as_matrix().shape)  # (5, 4)
