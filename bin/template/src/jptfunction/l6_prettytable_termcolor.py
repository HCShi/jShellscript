#!/usr/bin/python
# coding: utf-8
from prettytable import *
from termcolor import colored

# 通过行添加
row = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
row.sortby = "Population"
row.reversesort = True          # 和上面那行一起用来排序
row.int_format["Area"] = "04d"  # 这样可以针对指定行
row.float_format = "6.1f"       # 针对全局, 但必须是 float
row.align["City name"] = "l"    # Left align city names
row.add_row(["Adelaide", 1295, 1158259, 600.5])
row.add_row(["Brisbane", 5905, 1857594, 1146.4])
row.add_row(["Melbourne", 1566, 3806092, 646.9])
row.add_row([colored("Perth", 'red'), 5386, 1554769, 869.4])  # 这样改变颜色
row.del_row(2)  # 没有排序时可以按插入的顺序删除
print row

# 通过列添加
col = PrettyTable()
col.add_column("City name", ["Adelaide", "Brisbane", "Darwin", "Hobart", "Sydney"], align="l", valign="t")
col.add_column("Area", [1295, 5905, 112, 1357, 2058])
col.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374])
col.add_column("Annual Rainfall", [600.5, 1146.4, 1714.7, 619.5, 1214.8])
col.del_row(4)  # 没有 del_column
print col
# 还可以行列混淆输入, 但不常用

# 清空, row 和 col 相同
print row.clear()       # output: None
print row.clear_rows()  # output: None
