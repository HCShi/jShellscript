#!/usr/bin/python3
# coding: utf-8
import pandas as pd
# pandas 可以读取与存取的资料格式有很多种, csv、excel、json、html 与 pickle 等
# read_csv('file.csv') 读取时间和 行数 关系比较大; csdn 密码分析, 600w 行, 250M, 读取了 2min; ai-challenger 27w 行, 500M, 5s 载入
##################################################################
## 简单导入 csv; 默认都是 str 类型的, 需要转型
data = pd.read_csv('student.csv')  # read from csv; 自动把第一行作为 head/columns
print(data, '\n', data['name'])  # 第一次 .csv 中 name 后面跟着个空格, 结果老是出错
print(type(data))  # <class 'pandas.core.frame.DataFrame'>; 会根据读入的格式来确定数据类型
##################################################################
## read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, quoting=0, engine=None) 测试各种参数
# seq 等价于 delimiter...
data = pd.read_csv('./student.csv', sep='\s+|\t+|\s+\t+|\t+\s+', engine='python')  # 使用 regex 表示 delimiter 时要指定 engine
data = pd.read_csv('student.csv', header=0)  # 读取 csv 文件, 并将第一行设为表头; 可以发现 header='infer' 表示没有设置 name 的话就是 0
data = pd.read_csv('student.csv', names=['id', 'name', 'age', 'grade'])  # 设置了 name, header='infer' 就不起作用了
data = pd.read_csv('student.csv', quoting=3)  # quoting=3 tells Python to ignore double quotes.
# QUOTE_MINIMAL (0), QUOTE_ALL (1), QUOTE_NONNUMERIC (2) or QUOTE_NONE (3).
print(data, '\n')
# data = pd.read_csv('student.csv', sep=' # ', engine='python', names=['uname', 'passwd', 'mail'])  # csdn 泄露密码分隔符是 ' # ', 要设置 engine
##################################################################
## Add ability to process bad lines for read_csv
## 编码问题
df = pd.read_csv('./file.csv', sep=':', encoding='utf-8', error_bad_lines=False)  # 对于那些含有奇怪字符的, 可以用 encoding 来解决...

## 分隔符问题
# 参考: [read_csv() & extra trailing comma(s) cause parsing issues](https://github.com/pandas-dev/pandas/issues/2886)
data = pd.read_csv('./student.csv', sep='\s+|\t+|\s+\t+|\t+\s+', engine='python')  # 处理长度不同的分隔符
# NAME,PAT
# Peter,cat
# really bad line
# Fedor,cat
data = pd.read_csv('./student.csv', error_bad_lines=False)  # to skip really bad lines exist error_bad_lines=False parameter.
# 82,52,29,11,2,2013-08-02 00:00:00,,,gen,,FDP, employee,0,1,gen,,,0
# 55,69,36,19,2,2013-10-28 00:00:00,,,gen,,FDP employee,0,1,gen,,,0
# There are difference for FDP employee and FDP, employee. So it will be grate to have ability process this bad lines with own handler.
def bad_line_handler(items):  # probably ugly example, but lets imagine that `FDP, employee` is half of our data
    fdp_index = items.index('FDP')
    return items[:fdp_index] + ['FDP, employee'] + items[fdp_index + 2:]
pd.read_csv('./student.csv', process_bad_lines=bad_line_handler)
##################################################################
## write back
data.to_pickle('tmp.pickle')  # 只有 path 参数; save to pickle
data.to_csv('tmp.csv')  # 还带着 header 和 index
data.to_csv('tmp.csv', index=False, header=False, float_format='%.6f')  # 保留指定的小数长度
data.to_csv('tmp.csv', index=False)  # 这个用的最多
