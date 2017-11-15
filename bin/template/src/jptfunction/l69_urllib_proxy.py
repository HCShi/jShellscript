#!/usr/bin/python3
# coding: utf-8
from urllib import request
##################################################################
## 下载文件
url = "https://www.baidu.com"
response = request.urlopen(url)
raw = response.read().decode('utf8')
print(type(raw), len(raw))  # <class 'str'> 227
##################################################################
## 设置代理
proxies = {'http': 'http://127.0.0.1:1080'}
request.ProxyHandler(proxies)  # 设置代理要放到 urlopen() 之前
raw = request.urlopen(url).read().decode('utf8')
print(type(raw), len(raw))  # <class 'str'> 227
