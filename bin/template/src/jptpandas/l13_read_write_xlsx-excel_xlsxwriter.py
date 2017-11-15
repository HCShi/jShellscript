#!/usr/bin/python3
# coding: utf-8
from pandas.io.excel import ExcelWriter
import pandas as pd
##################################################################
## write
csv_files = ['student.csv', 'student.csv']
with ExcelWriter('tmp.xlsx') as ew:
    for csv_file in csv_files:
        pd.read_csv(csv_file).to_excel(ew, sheet_name=csv_file)  # 这里重复写了, 所以只有一个 sheet
##################################################################
## read
xl = pd.ExcelFile("tmp.xlsx")
print(xl.sheet_names)  # ['student.csv']
df = xl.parse("student.csv")
print(df.head())
#    Student ID   name  age  gender
# 0        1100  Kelly   22  Female
# 1        1101    Clo   21  Female
# 2        1102  Tilly   22  Female
# 3        1103   Tony   24    Male
# 4        1104  David   20    Male
##################################################################
## xlsxwriter
csv_files = ['student.csv', 'student.csv']
with ExcelWriter('tmp.xlsx', engine='xlsxwriter') as ew:  # xlsxwriter 只是有更加丰富的 format, 这里还没有用到
    for csv_file in csv_files:
        pd.read_csv(csv_file).to_excel(ew, sheet_name=csv_file)  # 这里重复写了, 所以只有一个 sheet
