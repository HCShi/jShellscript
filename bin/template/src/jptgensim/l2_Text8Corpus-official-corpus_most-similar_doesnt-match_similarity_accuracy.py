#!/usr/bin/python3
# coding: utf-8
# from gensim.models import Word2Vec
from gensim.models import word2vec  # 也可以想上面那样引入, 都对...
from gensim.models import KeyedVectors  # 这里只是 load model 时会用到
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)  # 官方推荐格式
##################################################################
## Text8Corpus() 处理数据; Text8Corpus() 的源代码还是能看懂的
# http://mattmahoney.net/dc/text8.zip 百度云已存盘, 压缩前 30M, 解压后 96M; wc text8 && head text8; 发现就一行, vim 打开也会崩
# wc text8  # 0  17005207 100000000 text8; 1 行, 17005207 个 word, 100000000 字节
sentences = word2vec.Text8Corpus('./tmp_dataset/text8')
print(type(sentences))  # <class 'gensim.models.word2vec.Text8Corpus'>
print(sentences.max_sentence_length)  # 10000
print(sentences.fname)  # ./tmp_dataset/text8
print(len(list(sentences)))  # 1701; 分成了 1701 句话
print(len(list(sentences)[0]))  # 10000; 每句话 10000 个 word
##################################################################
## 开始训练
model = word2vec.Word2Vec(sentences, size=200)  # 大约 3min
##################################################################
## 模型预测; Word2Vec 最著名的效果即是以语义化的方式推断出相似词汇
# 测试 model 结构 见 ./l1_hello-world_logging_model-参数讲解.py, 那个运行比较快, 好调试
print(model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1))  # [('queen', 0.6476820111274719)]; ..., 新世界的大门
print(model.doesnt_match("breakfast cereal dinner lunch".split()))  # cereal
print(model.similarity('woman', 'man'))  # 0.696215908841
print(model.most_similar(['man'])) # [('woman', 0.6962158679962158), ('girl', 0.6134898662567139), ...]; ...
print(model['computer'])  # 如果我们希望直接获取某个单词的向量表示, 直接以下标方式访问即可
##################################################################
## 模型评估
# Word2Vec 的训练属于无监督模型, 并没有太多的类似于监督学习里面的客观评判方式, 更多的依赖于端应用
# 训练集上表现的好也不意味着 Word2Vec 在真实应用中就会表现的很好, 还是需要因地制宜
# Google 之前公开了 20000 条左右的语法与语义化训练样本 questions-words.txt, 每一条遵循 A is to B as C is to D 这个格式
# 这里为了放到百度云上好辨认, 修改了名字
model.accuracy('./tmp_dataset/questions-words_Word2Vec-accuracy-test.txt')  # 运行 1min 左右; questions-words.txt 是分类别的, 每个类别的识别率如下:
# 2017-10-22 08:49:26,921 : INFO : capital-common-countries: 35.2% (178/506)
# 2017-10-22 08:49:33,961 : INFO : capital-world: 21.1% (306/1452)
# 2017-10-22 08:49:35,220 : INFO : currency: 10.4% (28/268)
# 2017-10-22 08:49:42,795 : INFO : city-in-state: 12.7% (199/1571)
# 2017-10-22 08:49:44,230 : INFO : family: 74.5% (228/306)  # 就这个还高一点
# 2017-10-22 08:49:47,887 : INFO : gram1-adjective-to-adverb: 14.0% (106/756)
# 2017-10-22 08:49:49,382 : INFO : gram2-opposite: 14.4% (44/306)
# 2017-10-22 08:49:55,751 : INFO : gram3-comparative: 59.0% (744/1260)
# 2017-10-22 08:49:58,330 : INFO : gram4-superlative: 36.8% (186/506)
# 2017-10-22 08:50:03,195 : INFO : gram5-present-participle: 28.5% (283/992)
# 2017-10-22 08:50:09,733 : INFO : gram6-nationality-adjective: 54.2% (743/1371)
# 2017-10-22 08:50:16,115 : INFO : gram7-past-tense: 26.7% (356/1332)
# 2017-10-22 08:50:20,842 : INFO : gram8-plural: 42.8% (425/992)
# 2017-10-22 08:50:23,956 : INFO : gram9-plural-verbs: 32.6% (212/650)
# 2017-10-22 08:50:23,957 : INFO : total: 32.9% (4038/12268)  # 哈, 才 32.9%
