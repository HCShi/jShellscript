##################################################################
## 参考: https://github.com/EliasCai/sentiment
# 任务: 根据 contents-评论内容 找到 theme-主题 和 sentiment_words-情感关键词, 并对 情感关键词标注 sentiment_anls-情感正负面(-1, 0, 1)
# Finish:
# 使用 jieba 进行分词, 并用 LSTM 对第一个情感关键词进行预测, 10 轮 epochs 后验证样本的准确率为 0.70
# Todo:
# 1、将情感关键词添加到 jieba 的字典里
# 2、将第 2、3 个关键词添加到样本, 将预测的概率大于阈值的位置作为情感关键词输出
# 3、完成主题和情感正负面的分析
import pandas as pd
from nltk import ConditionalFreqDist  # 找同一个次有不同词性标注 时会用到
import jieba
import numpy as np
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from functools import reduce
from keras.utils import to_categorical
from keras import optimizers
from keras.models import Sequential, load_model
from keras.layers import Dense, Embedding
from keras.layers import LSTM
##################################################################
## 一: 数据预览
xlsx = pd.ExcelFile('./tmp_dataset/BDCI2017-taiyi/泰一指尚训练集.xlsx')
print(xlsx.sheet_names)  # ['Sheet1']
df = xlsx.parse("Sheet1")
print(df.shape)  # (20000, 5)
print(df.columns.values)  # ['row_id' 'content-评论内容' 'theme-主题' 'sentiment_word-情感关键词' 'sentiment_anls-情感正负面']
df = df.fillna('NULL')  # 将 NaN 变为 NULL, 因为 .xlsx 中用的是 NULL; 主要是针对用到 split(';') 时, NaN 是 float 类型的...
print(df[df.columns[1]])  # 一个情感关键词对应一个 情感正负面评分
print(df[df.columns[2]])  # 主题
print(df[df.columns[3]])  # 情感词
print(df[df.columns[4]])  # 情感值
print(df[df.columns[3:5]])  # 一个情感关键词对应一个 情感正负面评分
print(df.head())
## 简单计算情感值: 直接相加, 为正, 则为积极评价; 为负, 消极评价
df['result'] = df['sentiment_anls-情感正负面'].replace('NULL', '0').apply(lambda x: sum([int(num) for num in x.split(';') if len(num)]))
print(len([x for x in df[df.columns[5]] if x < 0]))  # 6350; 20000 中有 6350 个消极评论
print(len([x for x in df[df.columns[5]] if x > 0]))  # 9174; 20000 中有 9174 个积极评论
## 将 主题, 情感关键词 和 情感正负面 分隔
# 主题
print(set([type(word) for word in df[df.columns[2]]]))  # {<class 'float'>, <class 'str'>}; 竟然有 float..., 是 NaN
themes = [word for words in df[df.columns[2]] for word in words.split(';') if len(word)]
print(len(themes))  # 45648; 可以发现大部分只有 2 个主题
print(set([len(word) for word in themes]))  # {1, 2, 3, 4, 5, 6}; 所有主题长度最长为 6
print([word for word in themes if len(word) == 6])  # ['iphone', 'iphone', 'iphone', 'iphone']; 居然是英文的...
# 情感关键词
sen_words = [word for words in df[df.columns[3]] for word in words.split(';') if len(word)]
print(len(sen_words))  # 45648
print(set([len(word) for word in sen_words]))  # {1, 2, 3, 4, 5, 6}; 所有主题长度最长为 6
print([word for word in sen_words if len(word) == 6])  # ['没有物美价廉', '不会心平气和', '不是别出心裁', '不是结实耐用, ...]...; 这样玩没朋友啊...
# 情感值, 正负面
anls = [word for words in df[df.columns[4]] for word in words.split(';') if len(word)]
print(len(anls))  # 45648
## combine sen_words and anls; 联合情感词和情感值, 找同一个次有不同词性标注的
print(sen_words[:10])  # ['实惠', '快', '也好', '太长', '太贵', '不方便', '差', '无语', '满意', '好']
print(anls[:10])  # ['1', '1', '1', '-1', '-1', '-1', '-1', '-1', '1', '1']
con = ConditionalFreqDist(zip(sen_words, anls))
print(con)  # <ConditionalFreqDist with 3032 conditions>; 将相同的 key 合并了
print([condition for condition in con.conditions() if len(con[condition].keys()) > 1])  # ['不容易', '不高']; Shit, 只有两个词有不同的情感值(-1, 0, 1)
## 将 theme, sentiment_word, anls 存
with open('./tmp_dataset/BDCI2017-taiyi/theme.txt', 'w') as f: f.write('\n'.join(themes))
with open('./tmp_dataset/BDCI2017-taiyi/word.txt', 'w') as f: f.write('\n'.join(sen_words))
with open('./tmp_dataset/BDCI2017-taiyi/word_score.txt', 'w') as f: f.write('\n'.join(word + ' ' + anls for word, anls in zip(sen_words, anls)))
##################################################################
## 二: 数据预处理; 将 DataFrame 分为 四个 list 分别保存
# df = xlsx.parse("Sheet1")  # 因为上面把 NaN 换成了 NUll, 这里重新导入; 后来发现不用了, 使用的时候将 NULL 去掉就行了
contents = [str(word) for word in list(df[df.columns[1]].values)]; print(contents[:10])
themes = [str(word) for word in list(df[df.columns[2]].values)]; print(themes[:10])
words = [str(word) for word in list(df[df.columns[3]].values)]; print(words[:10])
anls = [str(word) for word in list(df[df.columns[4]].values)]; print(anls[:10])
print('len of contents:', len(contents))  # len of contents: 20000
print('len of words:', len(words))  # len of words: 20000
## jieba 分词添加 themes, words
dict_themes = [word for line in themes for word in line.strip().split(';') if len(word) and word != 'NULL']
print(len(dict_themes), len(set(dict_themes)))  # 22017 1959
dict_words = [word for line in words for word in line.strip().split(';') if len(word) and word != 'NULL']
print(len(dict_words), len(set(dict_words)))  # 43300 3031
for word in dict_themes: jieba.add_word(word)
for word in dict_words: jieba.add_word(word)
## 从 list 嵌套 str 变为 list 嵌套 list, contents 又变回 list 嵌套 str(但是有空格了), 也就是每句话分词存储, 每句的情感词也分词存储
contents = [' '.join(jieba.lcut(line.strip())) for line in contents]; print(len(contents), contents[0])  # 20000 收到 了 ， 太 实惠 了 ， 买 了...
words = [list(set([item for item in line.strip().split(';') if len(item) and item != 'NULL'])) for line in words]; print(len(words), words[0])  # 20000 ['快', '实惠', '也好']
themes = [list(set([item for item in line.strip().split(';') if len(item) and item != 'NULL'])) for line in themes]; print(len(themes), themes[0])  # 20000 ['送货速度', '服务']
## 计算覆盖率; 关键词 / 被覆盖的关键词
print(reduce(lambda x, y: x + len(y), words, 0))  # 42182; 上面计算的是 45648, 居然少了...
print(reduce(lambda x, y: x + len(y), [set(tags.split()) & set(keys) for tags, keys in zip(contents, words)], 0))  # 38000
print(38000 / 42182)  # 0.900858185956095
## 计算覆盖率; 主题词 / 被覆盖的主题词
print(reduce(lambda x, y: x + len(y), themes, 0))  # 21532; 上面计算的是 45648, 居然少了...
print(reduce(lambda x, y: x + len(y), [set(tags.split()) & set(keys) for tags, keys in zip(contents, themes)], 0))  # 20939
print(20939 / 21532)  # 0.9724595950213636
## 输出 contents 前5个所有分词中 和 words/themes 前5个能匹配上的
print('\n'.join([str((set(keys), set(keys) & set(tags.split()))) for tags, keys in list(zip(contents, themes))[:5]]))
print('\n'.join([str((set(keys), set(keys) & set(tags.split()))) for tags, keys in list(zip(contents, words))[:5]]))
## 平均 情感关键词/主题 的数量
dfWords = pd.DataFrame(words); print(dfWords.shape)  # (20000, 16)
print(dfWords.count(axis=1).mean())  # 2.1091; 平均情感关键词的数量
dfThemes = pd.DataFrame(themes); print(dfThemes.shape)  # (20000, 12); 因为把 NULL 去掉了, 所以比 dfWords 短了
print(dfThemes.count(axis=1).mean())  # 1.0766
dfContents = pd.DataFrame(contents); print(dfContents.shape)  # (20000, 1)
## 剔除没有情感关键词的句子, 因为没有情感词肯定没有 主题, 反之不行, 所以剔除没有情感关键词的句子
print(words[:2])  # [['快', '也好', '实惠'], ['不方便', '太长', '太贵']]; list 嵌套 list
print(len([line for line in words if len(line)]))  # 17652; 原长为 20000
indexWord = dfWords.index[~pd.isnull(dfWords.iloc[:, 0])]; print(len(indexWord))  # 17652; 第一个关键词非空的 index
contents = dfContents.iloc[indexWord]; print(contents.shape)  # (17652, 1); 第一个关键词非空对应的评论内容
words = dfWords.iloc[indexWord]; print(words.shape)  # (17652, 16); 第一个关键词非空的列表
themes = dfThemes.iloc[indexWord]; print(themes.shape)  # (17652, 12)
print(words[:1])  # 也好  实惠  快  None  None  None  None  None  None  None  None  None  None
print(themes[:1])  # 送货速度  服务  None  None  None  None  None  None  None  None  None  None
## 将 contents, themes, words 转换为 list 嵌套 str
contents = contents[0].values; print(contents[0])  # 收到 了 ， 太 实惠 了 ， 买 了 一大 箱 ， 以后 继续 购买 ， 送货速度 快 服务 也好
themes = [' '.join([word for word in line if word]) for line in themes.values]; print(themes[0])  # 送货速度 服务
words = [' '.join([word for word in line if word]) for line in words.values]; print(words[0])  # 也好 实惠 快
print((contents + ' ' + words)[0])  # 收到 了 ， 太 实惠 了 ， 买 了 一大 箱 ， 以后 继续 购买 ， 送货速度 快 服务 也好 也好 实惠 快
print((contents + ' ' + words + ' ' + themes)[0])  # 收到 了 ， 太 实惠 了 ， 买 了 一大 箱 ， 以后 继续 购买 ， 送货速度 快 服务 也好 也好 实惠 快 送货速度 服务
##################################################################
## 将 contents / words/ themes 进行词向量, 有些词可能 Word2Vec 的现有模型中可能都没有..., 所以还是用 Tokenizer()
# 这里的 train 集太奇葩了...
tokenizer = Tokenizer(num_words=500000)
tokenizer.fit_on_texts(contents + ' ' + words + ' ' + themes)
print(len(tokenizer.word_index))  # 24651; 词典长度
sequences_contents = tokenizer.texts_to_sequences(contents); print(len(sequences_contents))  # 17652
print(len(sequences_contents[0]), len(contents[0].split()))  # 20 20; 将 contents 标记为词索引
sequences_words = tokenizer.texts_to_sequences(words); print(len(sequences_words))  # 17652
print(sequences_words[0], sequences_words[0][0])  # [380, 135, 47] 380
sequences_themes = tokenizer.texts_to_sequences(themes); print(len(sequences_themes))  # 17652
print(sequences_themes[0], len(themes[0].split()))  # [445, 119] 2
##################################################################
## 获取 情感关键词/主题 在评论内容中的位置
print(max([len(line) for line in sequences_contents]))  # 188; contents 一行最多 188 个词
print([line for line in sequences_contents if len(line) == 188])  # [[32, 12, 239, 12, 257, 24, 15246, 3, 427, 52, 9, 14, 141, 154, 1, 52, 1211, 15, 14, 1, 2044, 15, 1, 51, 15247, 154, 13, 272, 313, 1, 3971, 1932, 15248, 6336, 3, 172, 28, 209, 11, 1, 11, 4, 2221, 1, 137, 118, 272, 643, 453, 273, 6336, 1, 64, 700, 231, 1, 153, 89, 15249, 4, 40, 7, 52, 1, 12, 453, 18, 182, 1257, 1, 237, 1461, 6115, 13, 15250, 4, 3, 2065, 328, 2646, 514, 12, 508, 141, 721, 2, 1, 14, 2, 15, 1, 28, 2177, 522, 1697, 1, 110, 7, 52, 287, 435, 877, 913, 18, 387, 4, 274, 1, 2720, 2, 248, 14, 2, 16, 487, 1932, 273, 6336, 2, 1037, 1, 9712, 941, 13, 10, 4, 3, 9838, 1248, 108, 118, 28, 209, 62, 11, 4, 64, 1564, 1, 161, 2221, 118, 272, 487, 6336, 1, 88, 483, 643, 2, 9839, 3, 12, 4464, 740, 1, 5466, 7, 154, 1, 155, 200, 101, 11, 3, 40, 350, 2, 1, 28, 209, 522, 351, 781, 1, 19, 16, 255, 1, 198, 155, 100, 5997, 102, 209, 2, 3543, 3]]
data_contents = pad_sequences(sequences_contents, maxlen=200, padding='post')  # 平均长度是 20, 最长是 200, 设置为 50; 感觉不太合适...
print(len(data_contents), len(data_contents[0]), data_contents[0])  # 17652 200
# 因为上面的覆盖率为 90%+, 不是 100%, 所以可能有不能 index() 的
data_themes = [[list(data_contents[i]).index(word) if word in list(data_contents[i]) else -1 for word in sequences_themes[i]] for i in range(len(sequences_contents))]
print(data_contents[0][data_themes[0]], sequences_themes[0])  # [445 119] [445, 119]
print(max([len(line) for line in data_themes]))  # 12; 最长 12 个
print(len([word for line in data_themes for word in line if word == -1]))  # 568; 没有匹配到的数量
print(len([line for line in data_themes if -1 not in line]))  # 17096; 没有 -1 的行数
# index_themes = [True if -1 not in line else False for line in data_themes]; print(len(index_themes))  # 17652
# print(len(data_themes[index_themes]))  # 本来想把没有主题的行删掉...
data_words = [[list(data_contents[i]).index(word) if word in list(data_contents[i]) else -1 for word in sequences_words[i]] for i in range(len(sequences_contents))]
print(data_contents[0][data_words[0]], sequences_words[0])  # [380 135  47] [380, 135, 47]
print(max([len(line) for line in data_words]))  # 16; 最长 16 个
## data_themes, data_words 转换为 onehot 位置信息
onehot_themes = [[1 if index in data_themes[i] else 0 for index in range(200)] for i in range(len(data_themes))]
print(data_themes[0])  # [18, 16]
print(set(onehot_themes[0]), onehot_themes[0])  # {0, 1}
onehot_words = [[1 if index in data_words[i] else 0 for index in range(200)] for i in range(len(data_words))]
print(data_words[0])  # [19, 4, 17]
print(set(onehot_words[0]), onehot_words[0])  # {0, 1}
# data_contents 就是 特征值, padding_themes/padding_words 分别是 label, 训练两次
##################################################################
## 构造训练集, 开始训练
def trainModel(train_x, test_x, train_y, test_y):  # 训练模型
    model = Sequential()
    model.add(Embedding(len(tokenizer.word_index) + 1, 128))  # 输出 128 维词向量
    model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(200, activation='softmax'))  # 这里的 20 就是 padding_themes 中的 maxlen
    sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)  # lr 小一点, 以为 0 太多了
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    model.fit(train_x, train_y, batch_size=32, epochs=3, validation_data=(test_x, test_y))  # 这里原来是 20
    return model
train_x, test_x, train_y, test_y = train_test_split(data_contents, onehot_themes)
themes_model = trainModel(train_x, test_x, train_y, test_y)
themes_model.save('./tmp_dataset/BDCI2017-taiyi/0.007_onehot_themes.model')
themes_model = load_model('./tmp_dataset/BDCI2017-taiyi/0.007_onehot_themes.model')
model = load_model('./tmp_dataset/BDCI2017-taiyi/themes.model')
# 第一次训练/ themes.model
# 13239/13239 [==============================] - 260s - loss: 22.4353 - acc: 0.7941 - val_loss: 25.6015 - val_acc: 0.8006
# 13239/13239 [==============================] - 266s - loss: 21.7376 - acc: 0.8069 - val_loss: 25.4970 - val_acc: 0.8006
# 13239/13239 [==============================] - 277s - loss: 21.7602 - acc: 0.8069 - val_loss: 25.4768 - val_acc: 0.8006
# 13239/13239 [==============================] - 268s - loss: 21.7586 - acc: 0.8071 - val_loss: 25.5909 - val_acc: 0.8006
# 13239/13239 [==============================] - 269s - loss: 21.7086 - acc: 0.8070 - val_loss: 25.5866 - val_acc: 0.8006
# 比没有多少提升
# 第二次 0.007 0.007 model
# 13239/13239 [==============================] - 202s - loss: 4.5586 - acc: 0.5046 - val_loss: 4.2107 - val_acc: 0.5037
# 13239/13239 [==============================] - 206s - loss: 4.1831 - acc: 0.5086 - val_loss: 4.1935 - val_acc: 0.5037
# 13239/13239 [==============================] - 220s - loss: 4.1752 - acc: 0.5086 - val_loss: 4.1884 - val_acc: 0.5037
# 13239/13239 [==============================] - 211s - loss: 4.1692 - acc: 0.5086 - val_loss: 4.1994 - val_acc: 0.5037
# 13239/13239 [==============================] - 224s - loss: 4.1665 - acc: 0.5086 - val_loss: 4.1892 - val_acc: 0.5037
# ##################################################################
## 使用预测值模型
predict_classes = themes_model.predict_classes(train_x)
print(len(predict_classes), predict_classes[1])  # 13239 0
predict = themes_model.predict(train_x)
print(len(predict), predict[1])  # 4413
print(max(predict[1]), min(predict[1]))  # 0.205561 7.92129e-05
print(train_y[0])
print(max(predict))
pos_pred = themes_model.predict_classes(test_x)  # 获取评论内容的预测关键词
print(len(pos_pred), set(pos_pred))  # 4413
pos_y = np.argmax(test_y, axis=1)  # 最大值的位置, 也就是还原到 data_y 的形式
# x[[i for i in range(pos_pred.shape[0])], pos_pred]  # 通过预测的位置获取关键词
index2word = pd.DataFrame.from_dict(tokenizer.word_index, 'index').reset_index().set_index(0)  # 将 word2index 转化为 index2word

print('模型预测的关键词')
print(index2word.loc[test_x[[i for i in range(pos_pred.shape[0])], pos_pred]].head(5))
print('实际样本的关键词')
print(index2word.loc[test_x[[i for i in range(pos_y.shape[0])], pos_y]].head(5))

#     index
# 0
# 56     垃圾
# 644    开心
# 174    不行
# 73     很快
# 144    容易


#     index
# 0
# 3519    冒牌
# 644     开心
# 174     不行
# 73      很快
# 144     容易
# 因为只训练了 epoch 5, 所以比较低
