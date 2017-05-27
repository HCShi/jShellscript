#!/usr/bin/python
# coding: utf-8
from multiprocessing.dummy import Pool  # 这里只是简单的测试多线程, 后面有 scapy
import requests
def getsource(url):
    print(requests.get(url).content)  # content 返回 utf-8, text 返回 unicode
    print(requests.get(url).text.encode('utf-8'))  # 但有时两个可以通用
    # converts a unicode object to a string object.
pool = Pool(4)  # 4 核 CPU
urls = ['https://www.baidu.com', 'https://www.taobao.com']
results = pool.map(getsource, urls)
pool.close()
pool.join()  # 等待多线程完成后回到主线程, 因为 I/O 密集, 所以...
