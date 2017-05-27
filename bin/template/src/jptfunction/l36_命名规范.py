#!/usr/bin/python3
# coding: utf-8
# 这里的命名主要针对那些基础类型的变量, list, dict; 类的对象以后考虑
class Person(object):  # 类名首字母大写
    def __init__(self, name):
        self.name = name  # 所有成员变量要在 __init__ 中声明
persons = [];  # 需要一个基本类型的变量来盛放 类的对象
for name in ['jrp', 'dr']: persons.append(Person(name))  # 成员变量的 list 用复数形式
for person in persons: print(person.name)  # 直接遍历成员变量的 list
person_dic = {}
for name in ['jrp', 'dr']: person_dic[name] = Person(name)  # 成员变量的 dict, 相当于带索引的 list.
for person in person_dic: print(person)  # 直接遍历的话输出的只是 key
# persons 通常用于不需要索引的地方
# person_dic 用于后期需要索引

