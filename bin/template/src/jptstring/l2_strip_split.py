#!/usr/bin/python3
# coding: utf-8
##################################################################
## strip() && split()
str = "  hello world "
print(str.strip())  # hello world
print(str.strip().lstrip('h').rstrip('d'))  # ello worl
print(str.split())  # ['hello', 'world']
