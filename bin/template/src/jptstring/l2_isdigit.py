#!/usr/bin/python3
# coding: utf-8
##################################################################
## prepare data
_str = "helloworld"; print(_str)
_num = "123456"; print(_num)
_str_num = "helloworld1234"; print(_str_num)
_str_spa = "hello world"; print(_str_spa)
_num_spa = "123 456"; print(_num_spa)
_str_num_spa = "hello 1234"; print(_str_num_spa)
_spa = "   "; print(_spa)
# print(_str.isnumeric(), _num.isnumeric(), _str_num.isnumeric(), _str_spa.isnumeric(), _num_spa.isalpha())  # False True False False
##################################################################
## S.isalpha() Return True if all characters in S are alphabetic and there is at least one character in S, False otherwise.
print(_str.isalpha(), _str_num.isalpha(), _str_spa.isalpha())  # True False False
print('AAAaaa'.isalpha())  # True
##################################################################
## S.isnumeric() Return True if there are only numeric characters in S, False otherwise.
print(_num.isnumeric(), _str_num.isnumeric(),  _num_spa.isalpha())  # True False False
##################################################################
## S.isspace() Return True if all characters in S are whitespace and there is at least one character in S, False otherwise.
print(_str_spa.isspace(), _spa.isspace())  # False True
##################################################################
## S.islower() Return True if all cased characters in S are lowercase and there is at least one cased character in S, False otherwise.
print(_str_spa.islower(), _spa.islower())  # True False
print('heHa'.islower())  # False; 不能有大写
print('heHa'.isupper())  # False
print('HEHA'.isupper())  # True
##################################################################
## 总结:
# 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier',
# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
# 还是很专一的, 不能有其它符号
