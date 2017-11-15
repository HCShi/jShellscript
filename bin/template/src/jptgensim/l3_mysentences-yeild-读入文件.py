#!/usr/bin/python3
# coding: utf-8
from gensim.models import word2vec
import logging, os
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)  # 官方推荐格式
##################################################################
## MySentences
# 将输入视为 Python 的内置列表很简单, 但是在输入很大时会占用大量的内存.
# 所以 Gensim 只要求输入按顺序提供句子, 并不将这些句子存储在内存, 然后 Gensim 可以加载一个句子, 处理该句子, 然后加载下一个句子
# 例如, 如果输入分布在硬盘上的多个文件中, 文件的每一行是一个句子, 那么可以逐个文件, 逐行的处理输入:
class MySentences(object):
    def __init__(self, path): self.path = path  # 传进来的可能是 文件 或者 目录
    def __iter__(self):  # a memory-friendly iterator
        if os.path.isdir(self.path):  # 如果传进来的是目录
            for fname in os.listdir(self.path):
                for line in open(os.path.join(self.dirname, fname)):
                    yield line.split()
        else:  # 如果传进来的是文件
            for line in open(self.path):
                yield line.split()
# Google 之前公开了 20000 条左右的语法与语义化训练样本 questions-words.txt, 每一条遵循 A is to B as C is to D 这个格式
# wc questions-words.txt  # 19558  78204 603955 questions-words.txt; 19558 行, 78204 个单词, 603955 字节
sentences = MySentences('./tmp_dataset/questions-words_Word2Vec-accuracy-test.txt')
print(len(list(sentences)))  # 19558 行
print(list(sentences)[0])  # [':', 'capital-common-countries']
##################################################################
## 训练模型
sentences = MySentences('./tmp_dataset/questions-words_Word2Vec-accuracy-test.txt')  # 重新打开, 因为上面已经移动了指针
model = word2vec.Word2Vec(sentences)
# 如果需要对文件中的单词做其他处理, 比如转换为 unicode, 转换大小写, 删除数字, 抽取命名实体等, 所有这些都可以在 MySentence 迭代器中进行处理.
