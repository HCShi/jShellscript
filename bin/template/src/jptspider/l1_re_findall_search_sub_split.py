#!/usr/bin/python3
# coding: utf-8
import re  # Python 里数量词默认是贪婪的 (在少数语言里也可能是默认非贪婪), 总是尝试匹配尽可能多的字符
##################################################################
## findall &&  (.*?), () 表示要分组
test = 'hewerxxixxsdfefwefxxlovexxsdweexxyouxx'
print(re.findall('xx.*xx', test))     # ['xxixxsdfefwefxxlovexxsdweexxyouxx'],                    # .* 贪心算法
print(re.findall('xx.*?xx', test))    # ['xxixx', 'xxlovexx', 'xxyouxx'],                         # .*? 非贪心算法
print(re.findall('xx(.*?)xx', test))  # ['i', 'love', 'you']                                      # (.*?) 取出要匹配的值
text = '@bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1'  # from 12306
print(re.findall(r'([A-Z]+)\|([a-z]+)', text))  # [('VAP', 'beijingbei'), ('BOP', 'beijingdong')  # r: 不进行转义, \, 不用写成 \\, 同理 \_ 表下划线
print(re.findall(r'[a-zA-Z\_][0-9a-zA-Z\_]{0,19}', '_abc'))  # Python 合法变量                    # {} 前一个变量重复次数
print(re.findall(r'\w+@\w+\.[a-z]{2,5}', 'email: 352111644@qq.com'))                              # \w = [a-zA-Z0-9_]
# [a-zA-Z\_\$][0-9a-zA-Z\_\$]* 由字母或下划线、$开头, 后接任意个由一个数字、字母或者下划线、$组成的字符串, JavaScript 变量名
# ^ 表示行的开头, ^\d 表示必须以数字开头; $ 表示行的结束, \d$ 表示必须以数字结束
# 测试 \n
test = 'hewerxx\nixxsdfefwefxxlovexxsdweexxyouxx'
print(re.findall('xx(.*?)xx', test))        # ['sdfefwef', 'sdwee']
print(re.findall('xx(.*?)xx', test, re.S))  # ['\ni', 'love', 'you'], re.S: make dot match newline
##################################################################
## 数字, search 返回找到的第一次匹配到的, group 是因为 pattern 中可能有很多处 ()
m = re.search(r'^(\d{3})-(\d{3,8})$', '010-12345'); print(m.group(0), m.group(1), m.group(2), m.groups())  # group(0) 永远是原始字符串
print(re.search(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    '19:05:30').groups())  # ('19', '05', '30'), 一个非常残暴的匹配时间的例子
## 先加上判断才能使用 groups()
datas, patten = ['12345', 'hello'], r'(\d+)'  # 这里一定要加上 ()
print([word for raw in datas if re.search(patten, raw) for word in re.search(patten, raw).groups()])  # groups() 方法一定要确定匹配到了, 否则报错
## [10-12] 的问题, 会匹配到 [102] [112]
print(re.search(r'(19\d{2}[10-12][10-31])', '1976112').groups())  # ('197611',)                   # [10-12] 并不是匹配 10, 11, 12...
print(re.search(r'(19\d{2}[10-12][10-31])', '197621').groups())  # ('197621',); 2 是第一个框, 1 是第二个框
print(re.search(r'(19\d{2}[10-12])', '197621').groups())  # ('19762',)
# print(re.search(r'(19\d{2}1[0-2]])', '197621').groups())  # 正确写法, 虽然会报错
## compile
regex = re.compile(r'(?P<month>[a-zA-Z]+)\s+(?P<year>\d{4})')
m = regex.search('may 2013')  # 这两行相当于下面一行
m = re.search(r'(?P<month>[a-zA-Z]+)\s+(?P<year>\d{4})', 'may 2013')
print(m.group('month'), m.group('year'), m.groups())  # may 2013 ('may', '2013')
## 匹配 yymmdd / yyyymmdd, () group 分组的好处
yymmdd = re.compile(r'((?P<year>\d{2})((0[13578]|1[02])(0[1-9]|[12][0-9]|3[01])|(0[469]|11)(0[1-9]|[12][0-9]|30)|(02(0[1-9]|1[0-9]|2[0-8]))))')
print(yymmdd.search('341204').groups())  # ('341204', '34', '1204', '12', '04', None, None, None, None); 第一个是原始字符串, 因为最外面有个括号
print(yymmdd.search('340228').groups())  # ('340228', '34', '0228', None, None, None, None, '0228', '28')
print(yymmdd.search('340430').groups())  # ('340430', '34', '0430', None, None, '04', '30', None, None)
print(yymmdd.search('340430').group('year'))  # 34
# 后面包含下面三个平行的匹配模式
# (0[13578]|1[02])(0[1-9]|[12][0-9]|3[01])  # 13578 12 月 和 日期
# (0[469]|11)(0[1-9]|[12][0-9]|30)  # 4689 11 月 和 日期
# (02(0[1-9]|1[0-9]|2[0-8]))  # 平月, 没有分析闰月, 这里有两层嵌套...
# 下面只是到了 2019 年
yyyymmdd = re.compile(r'(?P<year>19[0-9]{2}|20[0-1][0-9])((0[13578]|1[02])(0[1-9]|[12][0-9]|3[0-1])|(0[469]|11)(0[1-9]|[12][0-9]|30)|(02(0[1-9]|1[0-9]|2[0-8])))')
print(yyyymmdd.search('20130328').groups())  # ('2013', '0328', '03', '28', None, None, None, None); 这里就没有 最外面的括号了
print(yyyymmdd.search('20130430').groups())  # ('2013', '0430', None, None, '04', '30', None, None)
print(yyyymmdd.search('20130228').groups())  # ('2013', '0228', None, None, None, None, '0228', '28')
##################################################################
## sub(将第一个参数匹配到的替换为第二个参数, 第三个参数为字符串源) && split && 各种正则表达式
phone = "2004-959-559 # 'jrp', This is Phone Number"
print(re.sub(r'#.*$', "", phone), re.sub(r'\D', "", phone))  # 2004-959-559, 2004959559,          # \D 匹配非数字
print(re.sub('\'', '\"', phone))  # 2004-959-559 # "jrp", 因为 dict 从文件中读取时必须是
print(re.sub('[^a-zA-Z]', '', phone))  # jrpThisisPhoneNumber; 去掉所有非英文字母的               # [^a-zA-Z] 非英文字符
print(' '.join([word for word in re.sub('[^a-zA-Z]', ' ', phone).split()]))  # jrp This is Phone Number; 保留原来单词的顺序
cn = '你好，我是god。同一條'
print(re.sub('[^\u4e00-\u9fa5]', '', cn))  # 你好我是同一條                                       # [\u4e00-\u9fa5] 匹配所有汉字
##################################################################
## split
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))  # ['a', 'b', 'c', 'd']                               # \s 空白符
##################################################################
## Summary
# .         # Wildcard, matches any character
# ^abc      # Matches some pattern abc at the start of a string
# abc$      # Matches some pattern abc at the end of a string
# [abc]     # Matches one of a set of characters
# [A-Z0-9]  # Matches one of a range of characters
# ed|ing|s  # Matches one of the specified strings (disjunction)
# *         # Zero or more of previous item, e.g. a*, [a-z]* (also known as Kleene Closure)
# +         # One or more of previous item, e.g. a+, [a-z]+
# ?         # Zero or one of the previous item (i.e. optional), e.g. a?, [a-z]?
# {n}       # Exactly n repeats where n is a non-negative integer
# {n,}      # At least n repeats
# {,n}      # No more than n repeats
# {m,n}     # At least m and no more than n repeats
# a(b|c)+   # Parentheses that indicate the scope of the operators
