#!/usr/bin/python3
# coding: utf-8
##################################################################
## str.find(); str.rfind(); rfind() 是从右边开始数, 返回的还是第一个字符的索引
str = "this is string example....wow!!! this is really string";
l, r = str.find('string'), str.rfind('string'); print(l, r)
str = str[l:r]; print(str)  # 最后的 string 被去掉了
##################################################################
## upper(), lower()
a, b = "Hello", 'HELLO'
print(a.upper())  # HELLO
print(b.lower())  # hello
##################################################################
## strip() && split()
str = "  hello world "
print(str.strip())  # hello world
print(str.strip().lstrip('h').rstrip('d'))  # ello worl
print(str.split())  # ['hello', 'world']
##################################################################
# str.replace(old, new[, max])
# old: to be replaced; new: replace old substring; max: only the first count occurrences are replaced.
str = "this is string example....wow!!! this is really string";
print(str.replace("is", "was"))     # thwas was string example....wow!!! thwas was really string
print(str.replace("is", "was", 3))  # thwas was string example....wow!!! thwas is really string
##################################################################
## 总结:
# s.find(t)        # index of first instance of string t inside s (-1 if not found)
# s.rfind(t)       # index of last instance of string t inside s (-1 if not found)
# s.index(t)       # like s.find(t) except it raises ValueError if not found
# s.rindex(t)      # like s.rfind(t) except it raises ValueError if not found
# s.join(text)     # combine the words of the text into a string using s as the glue
# s.split(t)       # split s into a list wherever a t is found (whitespace by default)
# s.splitlines()   # split s into a list of strings, one per line
# s.lower()        # a lowercased version of the string s
# s.upper()        # an uppercased version of the string s
# s.title()        # a titlecased version of the string s
# s.strip()        # a copy of s without leading or trailing whitespace
# s.replace(t, u)  # replace instances of t with u inside s
