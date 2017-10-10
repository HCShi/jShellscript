#!/usr/bin/python3
# coding: utf-8
##################################################################
## startswith()
str = "hello_world"
print(str.startswith("hello"))
print(str.endswith(("world", "he")))  # 可以从列表中选取
##################################################################
## re.match()
import re
if re.match(r'^hello', str): print('start with hello')
if re.match(r'world$', str): print('end with world')  # 这个不好用
