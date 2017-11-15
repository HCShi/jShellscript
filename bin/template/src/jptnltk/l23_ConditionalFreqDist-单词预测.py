#!/usr/bin/python3
# coding: utf-8
import nltk
from nltk import ConditionalFreqDist
from nltk.corpus import brown
from nltk.corpus import names
from nltk.corpus import inaugural
from nltk.corpus import toolbox
from nltk.corpus import udhr
##################################################################
## ConditionalFreqDist 简单应用: 文本情感分析
word = ['实惠', '快', '也好', '快', '也好']
anls = ['1', '1', '1', '-1', '1']
tmp_Con = ConditionalFreqDist(zip(word, anls))
print(tmp_Con)  # <ConditionalFreqDist with 3 conditions>; 将相同的 'tmp' 合并了
print(tmp_Con.tabulate())
print(tmp_Con.conditions())  # ['实惠', '快', '也好']
print(tmp_Con['快'].most_common())  # [('1', 1), ('-1', 1)]
print(tmp_Con['快'].keys())  # dict_keys(['1', '-1'])
print(len(tmp_Con['快'].keys()))  # 2; 可以看到每个词语的词性有多少个...
print(len(tmp_Con['也好'].keys()))  # 1; 重复的已经 set() 化了
print([condition for condition in tmp_Con.conditions() if len(tmp_Con[condition].keys()) > 1])  # ['快']
tmp_Con.plot()
tmp_Con_1 = ConditionalFreqDist(zip(anls, word))
print(tmp_Con_1.conditions())  # ['实惠', '快', '也好']
##################################################################
## Brown 语料库 word 归类分析
print(brown.categories())  # ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre))  # 这里的 categories=genre 不能去掉
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']  # 从 brown.categories() 中找的
modals = ['can', 'could', 'may', 'might', 'must', 'will']  # 随机找的几个单词
print(cfd.tabulate(conditions=genres, samples=modals))  # Observe that the most frequent modal in the news genre is will, while the most frequent modal in the romance genre is could
#                  can could  may might must will  # 每个类别种各个单词的数量
#            news   93   86   66   38   50  389
#        religion   82   59   78   12   54   71
#         hobbies  268   58  131   22   83  264
# science_fiction   16   49    4   12    8   16
#         romance   74  193   11   51   45   43
#           humor   16   30    8    8    9   13
##################################################################
## 将上面的例子分开写; conditions()
genre_word = [(genre, word) for genre in ['news', 'romance'] for word in brown.words(categories=genre)]
print(len(genre_word))  # 170576 个词类
print(genre_word[:4])  # [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ('news', 'Grand')] # [_start-genre]
print(genre_word[-4:])  # [('romance', 'afraid'), ('romance', 'not'), ('romance', "''"), ('romance', '.')] # [_end-genre]
cfd = ConditionalFreqDist(genre_word)
print(cfd)  # <ConditionalFreqDist with 2 conditions>
print(cfd.conditions())  # ['news', 'romance'] # [_conditions-cfd]
print(cfd['news'])  # <FreqDist with 14394 samples and 100554 outcomes>
print(cfd['romance'])  # <FreqDist with 8452 samples and 70022 outcomes>
print(cfd['romance'].most_common(2))  # [(',', 3899), ('.', 3736)]
print(cfd['romance']['could'])  # 193
print(cfd['romance'].max())  # 找到 romance 中最大的
print(cfd['romance'][','])  # 3899
##################################################################
## plot() how the words America and citizen are used over time; 美国总统就职演讲, 使用 America 和 citizen 情况
cfd = ConditionalFreqDist((target, fileid[:4]) for fileid in inaugural.fileids() for word in inaugural.words(fileid) for target in ['america', 'citizen'] if word.lower().startswith(target))
cfd.plot()  # 绘制演讲中出现 America 和 citizen 次数
##################################################################
## tabulate(); 提取词对
# Next, let's combine regular expressions with conditional frequency distributions.
# Here we will extract all consonant-vowel sequences from the words of Rotokas, such as ka and si. Since each of these is a pair,
# it can be used to initialize a conditional frequency distribution. We then tabulate the frequency of each pair:
rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
print(cvs[:10])  # ['ka', 'ka', 'ka', 'ka', 'ka', 'ro', 'ka', 'ka', 'vi', 'ko']
cfd = ConditionalFreqDist(cvs)
cfd.tabulate()
#     a    e    i    o    u
# k  418  148   94  420  173
# p   83   31  105   34   51
# r  187   63   84   89   79
# s    0    0  100    2    1
# t   47    8    0  148   37
# v   93   27  105   48   49
##################################################################
## 处理 udhr; 单词长度在不同语言的分布
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = ConditionalFreqDist((lang, len(word)) for lang in languages for word in udhr.words(lang + '-Latin1'))
cfd.plot(cumulative=True)
##################################################################
## 画 男女名字结尾字母 区分图; It is well known that names ending in the letter a are almost always female.
cfd = nltk.ConditionalFreqDist((fileid, name[-1]) for fileid in names.fileids() for name in names.words(fileid))
cfd.plot()
##################################################################
## 利用 NLTK 预测单词
# 任务: 训练和创建一个单词预测器, 例如: 给定一个训练过语料库, 写一个能够预测给定单词的一下个单词的程序.
#       使用这个预测器随机生成一个 20 个词的句子.

# 要创建单词预测器, 我们首先要在训练过的语料库中计算两个词的顺序分布, 例如, 我们需要累加给定单词接下来这个单词的出现次数.
# 一旦我们计算出了分布, 我们就可以通过输入一个单词, 得到它在语料库中所有可能出现的下一个单词列表, 并且可以从列表中随机输出一个单词.
# 为了随机生成一个 20 个单词的句子, 我只需要给定一个初始单词, 利用预测器来预测下一个单词, 然后重复操作指导直到句子满 20 个词.
# 清单 2 描述了怎么利用 NLTK 提供的模块来简单实现. 我们利用简奥斯丁的 Persuasion 作为训练语料库.
def generate_model(cfdist, word, num=20):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)  # 每一个次都是一个分类, 计算其后面出现最多的词
cfd = nltk.ConditionalFreqDist(bigrams)
print(cfd['living'])  # FreqDist({'creature': 7, 'thing': 4, 'substance': 2, ',': 1, '.': 1, 'soul': 1})
print(generate_model(cfd, 'living'))
# living creature that he said , and the land of the land of the land
# 解答: 输出的 20 个单词的句子当然不合语法. 但就词的角度两两来看, 是合语法的,
# 因为用以估计条件分布概率(conditional frequency distribution)的训练语料库是合乎语法的, 而我们正是使用了这个条件分布概率.
# 注意在本任务中, 我们使用前一个词作为预测器的上下文提示. 显然也可以使用前两个, 甚至前三个词.
##################################################################
## 总结:
# 1. ConditionalFreqDist() 专门为 Brown 这类带标签的准备的, gutenberg 用不上
# 2. 这里的每一个 #### 下面都是一个单独的功能
##################################################################
## API
# Example                               Description
# cfdist = ConditionalFreqDist(pairs)   create a conditional frequency distribution from a list of pairs
# cfdist.conditions()                   the conditions
# cfdist[condition]                     the frequency distribution for this condition
# cfdist[condition][sample]             frequency for the given sample for this condition
# cfdist.tabulate()                     tabulate the conditional frequency distribution
# cfdist.tabulate(samples, conditions)  tabulation limited to the specified samples and conditions
# cfdist.plot()                         graphical plot of the conditional frequency distribution
# cfdist.plot(samples, conditions)      graphical plot limited to the specified samples and conditions
# cfdist1 < cfdist2                     test if samples in cfdist1 occur less frequently than in cfdist2
