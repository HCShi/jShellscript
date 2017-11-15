#!/usr/bin/python3
# coding: utf-8
# 任务: 用 NLTK 的 corpus 模块读取包含在古登堡语料库的 austen-persuasion.txt, 回答以下问题:
# 1. 这个语料库一共有多少字？
# 2. 这个语料库有多少个唯一单词(unique words)
# 3. 前 10 个频率最高的词出现了几次 (见 l21_Freqdist)
import nltk
from nltk.corpus import gutenberg  # 导入 gutenberg 集
##################################################################
## words(), fileids()
print(gutenberg.fileids())  # 都有些什么语料在这个集合里; 共 14 个
# ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']
print(len(gutenberg.words('austen-persuasion.txt')))  # 98171
print(gutenberg.words('austen-persuasion.txt'))  # return: the given file(s) as a list of words
print(len(gutenberg.words(gutenberg.fileids())))  # 2621613; 所有的 gutenberg 单词
print(len(gutenberg.words()))  # 2621613; 和上面的一样, 默认就是取所有的文档
print(gutenberg.words()[:5])  # ['[', 'Emma', 'by', 'Jane', 'Austen']
##################################################################
## sents()
macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
print(len(macbeth_sentences))  # 1907 句话
print(macbeth_sentences[0])  # ['[', 'The', 'Tragedie', 'of', 'Macbeth', 'by', 'William', 'Shakespeare', '1603', ']']
print(''.join(macbeth_sentences[0]))  # [TheTragedieofMacbethbyWilliamShakespeare1603]
longest_len = max(len(s) for s in macbeth_sentences)
print([s for s in macbeth_sentences if len(s) == longest_len])  # 找出最长的一句话
##################################################################
## 类型
print(type(gutenberg))  # <class 'nltk.corpus.reader.plaintext.PlaintextCorpusReader'>
print(type(gutenberg.words('austen-persuasion.txt')))  # <class 'nltk.corpus.reader.util.StreamBackedCorpusView'>
print(type(gutenberg.words()))  # <class 'nltk.corpus.reader.util.ConcatenatedCorpusView'>
# print(gutenberg.concordance('surprize'))  # 'PlaintextCorpusReader' object has no attribute 'concordance'
persuasion = nltk.Text(gutenberg.words('austen-persuasion.txt'))  # 转型
print(persuasion.concordance('persuasion'))  # 这样就能用 book.text1 中的方法了...
##################################################################
## 类型变换原理
raw = gutenberg.raw('austen-persuasion.txt'); print(len(raw))  # 466292; 字符数
tokens = nltk.word_tokenize(raw); print(len(tokens))  # 97888; 跟 gutenberg.words() 统计的还是不一样...
##################################################################
## 路径
print(gutenberg.abspath('austen-persuasion.txt'))  # /home/coder352/nltk_data/corpora/gutenberg/austen-persuasion.txt
print(gutenberg.abspaths())  # 返回所有的文件路径
##################################################################
## average word length, average sentence length, and the number of times each vocabulary item appears in the text on average
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)
# 5 25 26 austen-emma.txt
# 5 26 17 austen-persuasion.txt
