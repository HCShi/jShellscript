#!/usr/bin/python3
# coding: utf-8
from pypinyin import pinyin, lazy_pinyin, Style
##################################################################
## 基本功能测试
print(pinyin('中心'))  # [['zhōng'], ['xīn']]
print(pinyin('中心', heteronym=True))  # [['zhōng', 'zhòng'], ['xīn']]; 启用多音字模式
print(pinyin('中心', style=Style.FIRST_LETTER))  # [['z'], ['x']]; 设置拼音风格
print(pinyin('中心', style=Style.TONE2, heteronym=True))  # [['zho1ng', 'zho4ng'], ['xi1n']]
print(pinyin('中心', style=Style.BOPOMOFO))  # [['ㄓㄨㄥ'], ['ㄒㄧㄣ']]; 注音风格
print(pinyin('中心', style=Style.CYRILLIC))  # [['чжун1'], ['синь1']]; 俄语字母风格
print(lazy_pinyin('中心'))  # ['zhong', 'xin']; 不考虑多音字的情况
##################################################################
## 鲁棒性测试
print(lazy_pinyin(['我', '是']))  # ['wo', 'shi']
print(lazy_pinyin('中心 一个'))  # ['zhong', 'xin', ' ', 'yi', 'ge']
print(lazy_pinyin('中心 5 #[hello] :'))  # ['zhong', 'xin', ' 5 #[hello] :']
##################################################################
## 还有命令行版的...
# $ pypinyin 音乐  # yīn yuè
# $ pypinyin -h
