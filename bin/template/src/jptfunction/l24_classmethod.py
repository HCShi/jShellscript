#!/usr/bin/python3
# coding: utf-8
string_date = '10-02-2017'
class Date(object):
    day, month, year = 0, 0, 0
    def __init__(self, day=0, month=0, year=0): self.day, self.month, self.year = day, month, year
    @classmethod
    def from_string(cls, date_as_string):  # classmethod must have a reference to a class object as the first parameter
        day, month, year = map(int, date_as_string.split('-'))
        date = cls(day, month, year)
        return date
day, month, year = map(int, string_date.split('-'));
data1 = Date(day, month, year)  # 这种方法不够好, 下面用 classmethod 实现
data2 = Date.from_string(string_date)  # 调用类的方法, 把当前对象 和 日期字符串传进去
print(data2.year, data2.month, data2.day)
