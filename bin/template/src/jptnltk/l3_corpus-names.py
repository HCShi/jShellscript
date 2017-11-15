#!/usr/bin/python3
# coding: utf-8
import nltk
from nltk.corpus import names
##################################################################
## 窥探 names
print(names.root)  # ~/nltk_data/corpora/names; 根路径
print(names.abspaths())  # [FileSystemPathPointer('/home/coder352/nltk_data/corpora/names/female.txt'), FileSystemPathPointer('/home/coder352/nltk_data/corpora/names/male.txt')]
# This corpus contains 5001 female names and 2943 male names, sorted alphabetically, one per line.
print(len(names.raw()))  # 55869;
print(names.readme())  # ~/nltk_data/corpora/names/README; 打印了一遍
##################################################################
## 常见应用
male = names.words('male.txt'); print(len(male))  # 2943
all_name = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
print(type(male))  # <class 'list'>; 和 book.text1 不一样, 那个是 nltk.text.Text 类, 封装了 list 方法
##################################################################
## nltk.Text() 转型
name_text = nltk.Text(names.words('male.txt'))  # 从 list 转为 Text 很奇怪
print(name_text.concordance('bob'))
##################################################################
## 男女同名
male_names = names.words('male.txt')
female_names = names.words('female.txt')
print([w for w in male_names if w in female_names])  # ['Abbey', 'Abbie', 'Abby', 'Addie', 'Adrian', 'Adrien', 'Ajay', 'Alex', 'Alexis', ...]
