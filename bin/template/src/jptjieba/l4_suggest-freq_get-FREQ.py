#!/usr/bin/python3
# coding: utf-8
import jieba
##################################################################
## suggest_freq(segment, tune=True) 可调节单个词语的词频, 使其能(或不能)被分出来
# suggest_freq() 每执行一次, 频率会增加 1
print(jieba.get_FREQ(('中', '将')))  # None
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))  # 如果/放到/post/中将/出错/。
print(jieba.suggest_freq(('中', '将'), True))  # 494; 意思是 中将 两个字要分开
print(jieba.get_FREQ('中'), jieba.get_FREQ('将'))  # 243191 122305
print(jieba.get_FREQ('中', '将'))  # 243191; 输出的是 中 的词频
print(jieba.get_FREQ(('中', '将')))  # None, 没有意义
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))  # 如果/放到/post/中/将/出错/。

print(jieba.get_FREQ('台中'))
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))  # 「/台/中/」/正确/应该/不会/被/切开
print(jieba.suggest_freq('台中', True))  # 69; 执行几次以后会增加...,
print(jieba.get_FREQ('台中'))
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))  # 「/台中/」/正确/应该/不会/被/切开
##################################################################
## "台中"总是被切成"台 中"; P(台中) < P(台) x P(中), "台中"词频不够导致其成词概率较低
# 解决方法: 强制调高词频
# jieba.add_word('台中') 或者 jieba.suggest_freq('台中', True)
##################################################################
## test frequency tune
testlist = [
    ('今天天气不错', ('今天', '天气')),
    ('如果放到post中将出错。', ('中', '将')),
    ('我们中出了一个叛徒', ('中', '出')),
]
for sent, seg in testlist:
    word = ''.join(seg)
    print('%s Before: %s, After: %s' % (word, jieba.get_FREQ(word), jieba.suggest_freq(seg, True)))
    print('/'.join(jieba.cut(sent, HMM=False)))
    print("-"*40)
##################################################################
## 总结:
# 1. jieba.suggest_freq('台中', True)  # 表示将两个字看做一个词, 执行几次以后会增加...,
# 2. jieba.suggest_freq(('台' '中'), True)  # 表示将两个字不能看做一个词, 执行几次会不会增加
