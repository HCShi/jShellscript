#!/usr/bin/python3
# coding: utf-8
##################################################################
## startswith(), endswith()
s = "hello_world"
print(s.startswith("hello"))  # True
print(s.endswith(("world", "he")))  # True; 可以从列表中选取

##################################################################
## re.match()
import re
if re.match(r'^hello', s): print('start with hello')  # start with hello
if re.match(r'world$', s): print('end with world')  # 这个不好用
##################################################################
## in
print('ab' in 'sabc')  # True
