#!/usr/bin/python3
# coding: utf-8
import jieba
import jieba.posseg as pseg
##################################################################
result = pseg.cut("我爱中国, 我爱家乡, 我爱亲人")
for w in result: print(w.word, "/", w.flag, ", ", end=' ')  # 带标签
