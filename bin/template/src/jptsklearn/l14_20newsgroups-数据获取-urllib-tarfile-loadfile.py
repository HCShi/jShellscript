#!/usr/bin/python3
# coding: utf-8
# 本文所用到的数据集被称为 "20 种新闻组", 是一个经常被用来进行机器学习和自然语言处理的数据集, 它包含 20 种新闻类别的近 20000 篇新闻
# 其官方简介可参见 http://qwone.com/~jason/20Newsgroups/
from sklearn.datasets import fetch_20newsgroups
##################################################################
## 先热下身, 查看一下数据的结构
news = fetch_20newsgroups(subset='all')  # 先放着, 等那天能在终端翻墙以后再回来; 后来发现可以下载, 就是慢, 自己下载好了
# Downloading dataset from http://people.csail.mit.edu/jrennie/20Newsgroups/20news-bydate.tar.gz (14 MB);
# 会放到 ~/scikit_learn_data/20news-bydate_py3.pkz; 如果下载慢手动去下载放进去
print(dir(news))  # ['DESCR', 'data', 'description', 'filenames', 'target', 'target_names']
print(news.description)  # 18846; the 20 newsgroups by date dataset
print(len(news.data))  # 18846
print(type(news.data), type(news.data[0]))  # <class 'list'> <class 'str'>; 每个新闻是一整个 str
print(news.filenames, len(news.filenames))  # 一堆路径名
print(news.target, len(news.target))  # [10  3 17 ...,  3  1  7] 18846; 这里的 target 已经自动数值化了, 为 20 个分类
print(news.target_names, len(news.target_names))  # ['alt.atheism', ..., 'talk.religion.misc'] 20
# 计算机图形学 (comp.graphics), 与无神论 (alt.atheism) 以及基督教 (soc.religion.christian) ...

# 下面开始程序, 两种下载数据的方式, 上边的算一种
##################################################################
## 方法一: fetch_20newsgroups() 获取数据集, 设定更多参数
# 我们有多种方式来获取这个数据集, 一种简单的方法是使用 sclearn 的自带函数 sklearn.datasets.fetch_20newsgroups
# 这个函数能自动从网上下载 "20 种新闻组" 的数据并进行读取; 为了节省计算和处理的时间, 我们仅选取 20 种分类中的四种进行之后的分析工作
categories = ["alt.atheism", "soc.religion.christian", "comp.graphics", "sci.med"]  # 选取需要下载的新闻分类
twenty_train = fetch_20newsgroups(subset="train", categories=categories, shuffle=True, random_state=42)  # 下载并获取训练数据, 也是先全部下载, 再提取部分
print(twenty_train.target_names)  # ['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']

##################################################################
## 方法二: 我们更常用的方法是直接从网络下载我们所需要的数据
# 用 Python 所提供的 urllib 库来完成数据包的下载工作, 并解压.
# 从网络下载文件可以使用 urllib.request.urlretrieve 这个函数.
# 通常, 我们下载到的数据包都是压缩文件, 这时候我们可以使用 tarfile 这个库来完成
from urllib import request
# request.urlretrieve("http://jizhi-10061919.cos.myqcloud.com/sklearn/20news-bydate.tar.gz", "data.tar.gz")  # 国内资源
request.urlretrieve("http://people.csail.mit.edu/jrennie/20Newsgroups/20news-bydate.tar.gz", "data.tar.gz")  # 官网, .gz 已经 gitignore 了
# 解压下载的数据包
import tarfile
tar = tarfile.open("data.tar.gz", "r:gz")
tar.extractall('tmp_dataset/'); tar.close()  # 两个目录 20news-bydate-test 20news-bydate-train
# 选取需要下载的新闻分类
categories = ['alt.atheism','soc.religion.christian', 'comp.graphics', 'sci.med']
# 从硬盘获取训练数据
from sklearn.datasets import load_files  # 原来 load_files 是读取这样的结构数据啊, 上面的 fetch_20Newsgroups 做了好多工作啊...
twenty_train = load_files('tmp_dataset/20news-bydate-train',
        categories=categories,
        load_content = True,
        encoding='latin1',
        decode_error='strict',
        shuffle=True, random_state=42)
print(twenty_train.target_names)  # ['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']; 显示训练数据的分类
