#!/usr/bin/python3
# coding: utf-8
import pandas as pd
from gensim.models import word2vec
import time
sta = time.time()
model = word2vec.Word2Vec.load('/home/coder352/github/jData/Word2Vec/Word2Vec_Chinese_Model/word2vec_wx')
end = time.time()
print(end - sta)  # 机械硬盘: 12s; 固态硬盘: 6s; 模型 1.1G
# model.save('./tmp_dataset/Word2Vec_Model/1_word2vec_from_weixin/my.model')  # 尝试自己保存, 结果还是 4 个文件, 结果更大了...

print(pd.Series(model.most_similar('微信')))
# 0        (QQ, 0.7525061964988708)
# 1       (订阅号, 0.7143402099609375)
# 2       (QQ号, 0.6955775618553162)
# 3       (扫一扫, 0.6954882144927979)
# 4     (微信公众号, 0.6946920156478882)
# 5        (私聊, 0.6816550493240356)
# 6    (微信公众平台, 0.6741705536842346)
# 7        (私信, 0.6538211703300476)
# 8      (微信平台, 0.6517565250396729)
# 9        (官方, 0.6436207294464111)
print(model.most_similar('微信'))
