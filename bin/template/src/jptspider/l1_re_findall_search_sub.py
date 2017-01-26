#!/usr/bin/python
# coding: utf-8
import re
# findall &&  (.*?)
test = 'hewerxxixxsdfefwefxxlovexxsdweexxyouxx'
print re.findall('xx.*xx', test)     # ['xxixxsdfefwefxxlovexxsdweexxyouxx'], 贪心算法
print re.findall('xx.*?xx', test)    # ['xxixx', 'xxlovexx', 'xxyouxx'], 非贪心算法
print re.findall('xx(.*?)xx', test)  # ['i', 'love', 'you']
# 测试 \n
test = 'hewerxx\nixxsdfefwefxxlovexxsdweexxyouxx'
print re.findall('xx(.*?)xx', test)        # ['sdfefwef', 'sdwee']
print re.findall('xx(.*?)xx', test, re.S)  # ['\ni', 'love', 'you'], re.S: make dot match newline
# 数字, search 返回找到的第一次匹配到的, group 是因为 pattern 中可能有很多处 ()
test = 'hello12345world'
print re.search('(\d+)', test).group(1)  # 12345, search 返回值是正则表达式类型, 用 group 返回其值, type: str

# sub && 各种正则表达式
phone = "2004-959-559 # 'jrp', This is Phone Number"
print re.sub(r'#.*$', "", phone), re.sub(r'\D', "", phone)  # 2004-959-559, 2004959559
print re.sub('\'', '\"', phone)  # 2004-959-559 # "jrp", 因为 dict 从文件中读取时必须是 "
text = '@bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1'  # from 12306
print re.findall(r'([A-Z]+)\|([a-z]+)', text)  # [('VAP', 'beijingbei'), ('BOP', 'beijingdong')
# r 表示不进行转义
