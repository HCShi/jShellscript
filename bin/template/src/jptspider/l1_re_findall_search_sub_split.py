#!/usr/bin/python3
# coding: utf-8
import re
# findall &&  (.*?), () 表示要分组
test = 'hewerxxixxsdfefwefxxlovexxsdweexxyouxx'
print(re.findall('xx.*xx', test))     # ['xxixxsdfefwefxxlovexxsdweexxyouxx'], * 贪心算法
print(re.findall('xx.*?xx', test))    # ['xxixx', 'xxlovexx', 'xxyouxx'], ? 非贪心算法
print(re.findall('xx(.*?)xx', test))  # ['i', 'love', 'you']
# 测试 \n
test = 'hewerxx\nixxsdfefwefxxlovexxsdweexxyouxx'
print(re.findall('xx(.*?)xx', test))        # ['sdfefwef', 'sdwee']
print(re.findall('xx(.*?)xx', test, re.S))  # ['\ni', 'love', 'you'], re.S: make dot match newline
# 数字, search 返回找到的第一次匹配到的, group 是因为 pattern 中可能有很多处 ()
m = re.search(r'^(\d{3})-(\d{3,8})$', '010-12345'); print(m.group(0), m.group(1), m.group(2), m.groups())  # group(0) 永远是原始字符串

# sub(将第一个参数匹配到的替换为第二个参数, 第三个参数为字符串源) && split && 各种正则表达式
phone = "2004-959-559 # 'jrp', This is Phone Number"
print(re.sub(r'#.*$', "", phone), re.sub(r'\D', "", phone))  # 2004-959-559, 2004959559,          # \D 匹配非数字
print(re.sub('\'', '\"', phone))  # 2004-959-559 # "jrp", 因为 dict 从文件中读取时必须是
text = '@bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1'  # from 12306
print(re.findall(r'([A-Z]+)\|([a-z]+)', text))  # [('VAP', 'beijingbei'), ('BOP', 'beijingdong')  # r: 不进行转义, \, 不用写成 \\, 同理 \_ 表下划线
print(re.findall(r'[a-zA-Z\_][0-9a-zA-Z\_]{0,19}', '_abc'))  # Python 合法变量                    # {} 前一个变量重复次数
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))  # ['a', 'b', 'c', 'd']                               # \s 空白符
print(re.search(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    '19:05:30').groups())  # ('19', '05', '30'), 一个非常残暴的匹配时间的例子
print(re.findall(r'\w+@\w+\.[a-z]{2,5}', 'email: 352111644@qq.com'))                              # \w = [a-zA-Z0-9_]
# [a-zA-Z\_\$][0-9a-zA-Z\_\$]* 由字母或下划线、$开头, 后接任意个由一个数字、字母或者下划线、$组成的字符串, JavaScript 变量名
# ^ 表示行的开头, ^\d 表示必须以数字开头; $ 表示行的结束, \d$ 表示必须以数字结束
