#!/usr/bin/python3
# coding: utf-8
##################################################################
## 写 bson 文件
post1 = {"author": "Mike", "text": "Another post!", "tags": ["bulk", "insert"], "date": 14}
post2 = {"author": "Jenny", "text": "Another post!", "tags": ["bulk", "insert"], "date": 14}
f = open('tmp.bson', 'wb')
f.write(bson.BSON.encode(post1))
f.write(bson.BSON.encode(post2))
f.close()
##################################################################
## 直接使用 Python 读取 bson 文件, bson 文件是 json 的二进制格式
import bson  # pip install pymongo 这样安装的附带包, 不能直接 pip install bson (这样出来是第三方的, 好多函数都没有)
items = list(bson.decode_file_iter(open('./tmp.bson', 'rb'))); print(len(items))  # 2
item = items[0]; print(type(items), type(item))  # <class 'list'> <class 'dict'>
print(item.keys())  # dict_keys(['author', 'text', 'tags', 'date'])
