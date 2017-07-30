#!/usr/bin/python3
# coding: utf-8
import pandas as pd
# pandas 可以读取与存取的资料格式有很多种, csv、excel、json、html 与 pickle 等
data = pd.read_csv('student.csv')  # read from csv
print(data)
data.to_pickle('tmp.pickle')  # save to pickle
