#!/usr/bin/python3
# coding: utf-8
##################################################################
## any: list 中只要有非零就为 True
print(any([x for x in range(5)]))  # True
print(any([0, 1]))  # True
##################################################################
## all: list 中只要有非零就为 False
print(all([0, 1]))  # False
