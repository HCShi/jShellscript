#!/usr/bin/python3
# coding: utf-8
from nltk.corpus import PlaintextCorpusReader
##################################################################
## Loading your own Corpus
corpus_root = '/home/coder352/nltk_data/corpora/gutenberg'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
print(len(wordlists.fileids()))  # 19; 该目录下有 19 个文件
print(wordlists.fileids())  # ['README', 'austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']
print(len(wordlists.raw('README')))  # 9351 个字符
