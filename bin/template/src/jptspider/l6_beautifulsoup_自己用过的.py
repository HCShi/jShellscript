#!/usr/bin/python
# coding: utf-8
from bs4 import BeautifulSoup
import bs4
html = """
<html><head><title> The Dormouse's story </title></head>
<body>
  <p class="title" name="dromouse"><b> The Dormouse's story </b></p>
  <p class="story"> Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"> <!-- Elsie --> </a> ,
    <a href="http://example.com/lacie" class="sister" id="link2"> Lacie </a> and
    <a href="http://example.com/tillie" class="sister" id="link3"> Tillie </a>;
  and they lived at the bottom of a well. </p>
  <p class="story"> ... </p>
</body>
"""
soup = BeautifulSoup(html, "html.parser")  # html 通过 requests.get(url) 获得; 第二个参数表示使用 Python 标准库
##################################################################
## find_all(), attrs[] 得到所有的 **链接**
links = soup.find_all('a')  # 找到所有的 a 标签
print(type(links))  # <class 'bs4.element.ResultSet'>
for link in links:
    print(link)  # 输出如下面三行
    # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    print(link.attrs['href'])  # 输出对应的属性值, 输出如下面三行
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie
##################################################################
## get_text() 将原始文字提取出来
raw = soup.get_text(); print(raw); print(type(raw))  # <class 'str'>
#  The Dormouse's story
#
#  The Dormouse's story
#  Once upon a time there were three little sisters; and their names were
#       ,
#      Lacie  and
#      Tillie ;
#   and they lived at the bottom of a well.
#  ...
##################################################################
## get_text() 可以转化任意字符串, 但记得标记添加参数 'html.p'
print(BeautifulSoup('hello </br> world <a> jiaruipeng', 'html.parser').get_text())
