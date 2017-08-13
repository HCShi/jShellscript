#!/usr/bin/python3
# coding: utf-8
import pandas as pd
# pandas 可以读取与存取的资料格式有很多种, csv、excel、json、html 与 pickle 等
data = pd.read_csv('student.csv')  # read from csv
print(data, '\n', data['name'])  # 第一次 .csv 中 name 后面跟着个空格, 结果老是出错
data = pd.read_csv('student.csv', header=0)  # 读取 csv 文件, 并将第一行设为表头
print(data, '\n', data['name'])  # 可以发现 header='infer' 是默认值, 好像就是 0

data.to_pickle('tmp.pickle')  # save to pickle
