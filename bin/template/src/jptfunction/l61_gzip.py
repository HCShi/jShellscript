#!/usr/bin/python3
# coding: utf-8
import gzip
##################################################################
## 压缩文件
import gzip
content = b"Lots of content here"  # 这里一定要用 byte; 否则 str 类型的不能写进去
with gzip.open('tmp.txt.gz', 'wb') as f: f.write(content)  # 解压后会是 tmp.txt; 里面是 Lots of content here
with gzip.open('tmp.gz', 'wb') as f: f.write(content)  # 解压后会是 tmp
##################################################################
## 读取文件
with gzip.open('tmp.gz', 'rb') as f:
    print(f.read())
##################################################################
## 实例
with gzip.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wordninja', 'wordninja_words.txt.gz')) as f:
    words = f.read().decode().split()
