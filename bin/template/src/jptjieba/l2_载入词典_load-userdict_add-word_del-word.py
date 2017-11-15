#!/usr/bin/python3
# coding: utf-8
# 词典一个词占一行; 每一行分三部分: 词语、词频(可省略)、词性(可省略); 词频省略时使用自动计算的能保证分出该词的词频; 如下所示
# 云计算 5
# 李小福 2 nr
# 创新办 3 i
# easy_install 3 eng
# 好用 300
# 韩玉赏鉴 3 nz
# 八一双鹿 3 nz
# 台中
# 凱特琳 nz
# Edu Trust认证 2000
import jieba
jieba.load_userdict("userdict.txt")  # file_name 为文件类对象或自定义词典的路径
##################################################################
## add_word(word, freq=None, tag=None) 和 del_word(word)
jieba.add_word('石墨烯')  # 和上面字典中的格式一样
# jieba.add_word(['我们', '你们'])  # AttributeError: 'list' object has no attribute 'decode'; 不能添加 list
jieba.del_word('自定义词')
##################################################################
## 测试
test_sent = (
    "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
    "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
    "「台中」正確應該不會被切開。mac上可分出「石墨烯」; 此時又可以分出來凱特琳了。"
)
print('/'.join(jieba.cut(test_sent)))
