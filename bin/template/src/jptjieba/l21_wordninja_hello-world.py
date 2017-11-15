#!/usr/bin/python3
# coding: utf-8
import wordninja
print(wordninja.split('derekanderson'))  # ['derek', 'anderson']
print(wordninja.split('imateapot'))  # ['im', 'a', 'teapot']
print(wordninja.split('heshotwhointhewhatnow'))  # ['he', 'shot', 'who', 'in', 'the', 'what', 'now']
print(wordninja.split('thequickbrownfoxjumpsoverthelazydog'))  # ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print(wordninja.split('wethepeopleoftheunitedstatesinordertoformamoreperfectunionestablishjusticeinsuredomestictranquilityprovideforthecommondefencepromotethegeneralwelfareandsecuretheblessingsoflibertytoourselvesandourposteritydoordainandestablishthisconstitutionfortheunitedstatesofamerica'))
# ['we', 'the', 'people', 'of', 'the', 'united', 'states', 'in', 'order', 'to', 'form', 'a', 'more', 'perfect', 'union', 'establish', 'justice', 'in', 'sure', 'domestic', 'tranquility', 'provide', 'for', 'the', 'common', 'defence', 'promote', 'the', 'general', 'welfare', 'and', 'secure', 'the', 'blessings', 'of', 'liberty', 'to', 'ourselves', 'and', 'our', 'posterity', 'do', 'ordain', 'and', 'establish', 'this', 'constitution', 'for', 'the', 'united', 'states', 'of', 'america']

print(wordninja.__version__)  # 0.1.3; 还有待改进
print(wordninja.split('HelloWorld'))  # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']; 大写不支持
print(wordninja.split('Hello World'))  # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']; 大写不支持
print(wordninja.split('hello world'))  # ['hello', 'world']
print(wordninja.split('helloworld'))  # ['helloworld']; 居然没分开
print(wordninja.split('hello123world'))  # ['hello', '1', '2', '3', 'w', 'o', 'r', 'l', 'd']
print(wordninja.split('123hello123'))  # ['1', '2', '3', 'h', 'e', 'l', 'l', 'o', '1', '2', '3']
# 所以要先把数字用 正则表达式 去掉
import re
print(wordninja.split(re.sub('[^a-zA-Z]', '', 'hello123world')))  # ['hello', '1', '2', '3', 'w', 'o', 'r', 'l', 'd']
##################################################################
## How fast it is!
import timeit
def f(): wordninja.split('imateapot')
print(timeit.timeit(f, number=10000))  # 0.40885152100236155
##################################################################
## 总结:
# 1. 其实内部运行的原理就是 ./l41_separate_en.py
