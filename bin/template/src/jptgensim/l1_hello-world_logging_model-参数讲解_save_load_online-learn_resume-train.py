#!/usr/bin/python3
# coding: utf-8
from gensim.models import word2vec # 引入 word2vec
import logging  # 引入日志配置
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)  # 官方推荐格式
##################################################################
## 准备数据, list 嵌套 list
raw_sentences = ["the quick brown fox jumps over the lazy dogs", "yoyoyo you go home now to sleep"]  # 引入数据集
sentences = [s.split() for s in raw_sentences]  # 切分词汇
print(sentences)  # [['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dogs'], ['yoyoyo', 'you', 'go', 'home', 'now', 'to', 'sleep']]
##################################################################
## 构建模型
# model = Word2Vec(sentences, size=100, min_count=5, worker=1, iter=5)
# min_count 参数可以对字典做截断. 少于 min_count 次数的单词会被丢弃掉
# size 是神经网络的隐藏层的单元数; 大的 size 需要更多的训练数据, 但是效果会更好. 推荐值为几十到几百.
# worker 参数控制训练的并行; default = 1 worker = no parallelization; worker 参数只有在安装了 Cython 后才有效. 没有 Cython 的话, 只能使用单核.
# Word2Vec(sentences, iter=1) 会调用句子迭代器运行两次(一般来说, 会运行 iter+1 次, 默认情况下 iter=5 ).
#     第一次运行负责收集单词和它们的出现频率, 从而构造一个内部字典树. 第二次以及以后的运行负责训练神经模型.
model = word2vec.Word2Vec(sentences, min_count=1)
print(type(model))  # <class 'gensim.models.word2vec.Word2Vec'>
##################################################################
## 内存
# word2vec 的参数被存储为矩阵 (Numpy array). array 的大小为 #vocabulary 乘以 #size 大小的浮点数(4 byte)矩阵.
# 内存中有三个这样的矩阵, 如果你的输入包含 100,000 个单词, 隐层单元数为 200, 则需要的内存大小为 100,000 * 200 * 4 * 3 bytes, 约为 229MB.
# 另外还需要一些内存来存储字典树, 但是除非你的单词是特别长的字符串, 大部分内存占用都来自前面说的三个矩阵.
##################################################################
## 使用模型, 这里训练的少, 可以到 ./l2_Text8Corpus-official-corpus.py 官方语料库训练结果里面测试, 这里只是测试 model 结构
print(model.similarity('dogs', 'you'))  # 0.200907723602; 进行相关性比较
print(model.similarity('dogs', 'dogs'))  # 1.0; 最相关
print(model.similarity('go', 'home'))  # 0.0670198771294;
print(model.similarity('brown', 'sleep'))  # 0.0228728534468;

print(model['dogs'])  # 查看某一个 word 对应的 word2vec 向量, 可以将这个 word 作为索引传递给训练好的模型对象
# print(model['hello'])  # KeyError: "word 'hello' not in vocabulary"
print(type(model['dogs']))  # <class 'numpy.ndarray'>
print(model['dogs'].shape)  # (100,); 和隐藏层单元数 size参数 对应

##################################################################
## save() && load()
model.save('tmp.model')
model1 = word2vec.Word2Vec.load('tmp.model')
# binary; 可以直接加载由 C 生成的模型
model.wv.save_word2vec_format('tmp.model.bin', binary=True)
model1 = gensim.models.KeyedVectors.load_word2vec_format('tmp.model.bin', binary=True)
# model1 = gensim.models.KeyedVectors.load_word2vec_format('tmp_text.model.bin.gz', binary=True)  # 可以直接加载用 gzipped/bz2 压缩的模型

##################################################################
## Online learning / Resuming training; 可以在加载模型之后使用另外的句子来进一步训练模型
# train(sentences, total_examples=None, epochs=None); 这两个参数代表句子的数量, 和迭代次数, 必须指定
model1 = word2vec.Word2Vec.load('tmp.model')
print(sentences)
model1.train(sentences, total_examples=2, epochs=3)  # 这两个参数必须指定
model1.train(sentences, total_examples=3, epochs=3)  # 设置为 3, 好像也没问题
# 但是不能对 Cython 生成的模型进行再训练.
