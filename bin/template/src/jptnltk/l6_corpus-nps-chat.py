#!/usr/bin/python3
# coding: utf-8
from nltk.corpus import nps_chat
##################################################################
## 简单查看
print(type(nps_chat))  # <class 'nltk.corpus.reader.nps_chat.NPSChatCorpusReader'>
print(len(nps_chat.fileids()))  # 15
print(nps_chat.fileids())  # ['10-19-20s_706posts.xml', '10-19-30s_705posts.xml', '10-19-40s_686posts.xml', '10-19-adults_706posts.xml', '10-24-40s_706posts.xml', '10-26-teens_706posts.xml', '11-06-adults_706posts.xml', '11-08-20s_705posts.xml', '11-08-40s_706posts.xml', '11-08-adults_705posts.xml', '11-08-teens_706posts.xml', '11-09-20s_706posts.xml', '11-09-40s_706posts.xml', '11-09-adults_706posts.xml', '11-09-teens_706posts.xml']
print(len(nps_chat.words('10-19-20s_706posts.xml')))  # 2829
print(nps_chat.words('10-19-20s_706posts.xml')[:10])  # ['now', 'im', 'left', 'with', 'this', 'gay', 'name', ':P', 'PART', 'hey']
##################################################################
## posts()
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print(chatroom[123])  # ['i', 'do', "n't", 'want', 'hot', 'pics', 'of', 'a', 'female', ',', 'I', 'can', 'look', 'in', 'a', 'mirror', '.']
