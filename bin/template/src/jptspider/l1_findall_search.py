#!/usr/bin/python
# coding: utf-8
import re
# 测试 .*?
test = 'hewerxxixxsdfefwefxxlovexxsdweexxyouxx'
print re.findall('xx.*xx', test)     # ['xxixxsdfefwefxxlovexxsdweexxyouxx'], 贪心算法
print re.findall('xx.*?xx', test)    # ['xxixx', 'xxlovexx', 'xxyouxx'], 非贪心算法
print re.findall('xx(.*?)xx', test)  # ['i', 'love', 'you']

# 测试 \n
test = 'hewerxx\nixxsdfefwefxxlovexxsdweexxyouxx'
print re.findall('xx(.*?)xx', test)        # ['sdfefwef', 'sdwee']
print re.findall('xx(.*?)xx', test, re.S)  # ['\ni', 'love', 'you'], re.S: make dot match newline

# 测试数字
test = 'hello12345world'
print re.search('(\d+)', test).group(1)  # 12345, search 返回值是正则表达式类型, 用 group 返回其值, type: str
