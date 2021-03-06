#!/usr/bin/python3
# coding: utf-8
import jieba
##################################################################
## 三种分词模式
# 精确模式:     试图将句子最精确地切开, 适合文本分析;
# 全模式:       把句子中所有的可以成词的词语都扫描出来, 速度非常快, 但是不能解决歧义;
# 搜索引擎模式: 在精确模式的基础上, 对长词再次切分, 提高召回率, 适合用于搜索引擎分词
seg_list = jieba.cut("我来到北京清华大学", cut_all=True); print("/ ".join(seg_list))  # 全模式 / Full Mode
seg_list = jieba.cut("我来到北京清华大学", cut_all=False); print("/ ".join(seg_list))  # 精确模式 / Default Mode
seg_list = jieba.cut("他来到了网易杭研大厦"); print(", ".join(seg_list))  # 默认是精确模式
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所, 后在日本京都大学深造"); print(", ".join(seg_list))  # 搜索引擎模式
# 输出:
# 【全模式】: 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学
# 【精确模式】: 我/ 来到/ 北京/ 清华大学
# 【新词识别】: 他, 来到, 了, 网易, 杭研, 大厦 (此处, "杭研"并没有在词典中, 但是也被 Viterbi 算法识别出来了)
# 【搜索引擎模式】:  小明, 硕士, 毕业, 于, 中国, 科学, 学院, 科学院, 中国科学院, 计算, 计算所, 后, 在, 日本, 京都, 大学, 日本京都大学, 深造
##################################################################
## 常用方法
# cut(sentence, cut_all=False, HMM=True)  # 默认是精确模式
print(jieba.lcut('我来到北京清华大学'))  # ['我', '来到', '北京', '清华大学']; 返回列表
print(jieba.lcut('我来到 Beijing 清华大学'))  # ['我', '来到', ' ', 'Beijing', ' ', '清华大学']; 空格也提取了
##################################################################
## 总结
# API:
#   jieba.cut 方法接受三个输入参数: 需要分词的字符串; cut_all 参数用来控制是否采用全模式; HMM 参数用来控制是否使用 HMM 模型
#   jieba.cut_for_search 方法接受两个参数: 需要分词的字符串; 是否使用 HMM 模型. 该方法适合用于搜索引擎构建倒排索引的分词, 粒度比较细

#   待分词的字符串可以是 unicode 或 UTF-8 字符串、 GBK 字符串. 注意: 不建议直接输入 GBK 字符串, 可能无法预料地错误解码成 UTF-8
#   jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator, 可以使用 for 循环来获得分词后得到的每一个词语(unicode), 或者用
#   jieba.lcut 以及 jieba.lcut_for_search 直接返回 list
#   jieba.Tokenizer(dictionary=DEFAULT_DICT) 新建自定义分词器, 可用于同时使用不同词典. jieba.dt 为默认分词器, 所有全局分词相关函数都是该分词器的映射.
