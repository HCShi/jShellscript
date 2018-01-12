#!/usr/bin/python
# coding: utf-8
# 参考: 崔庆才
from lxml import etree
# html = open('file.html').read()
html = """
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>测试-常规用法</title>
</head>
<body>
<div id="content">
    <ul id="useful">
        <li>这是第一条信息</li>
        <li>这是第二条信息</li>
        <li>这是第三条信息</li>
    </ul>
    <ul id="useless">
        <li>不需要的信息 1</li>
        <li>不需要的信息 2</li>
        <li>不需要的信息 3</li>
    </ul>
    <div id="url">
        <a href="http://jikexueyuan.com">极客学院</a>
        <a href="http://jikexueyuan.com/course/" title="极客学院课程库">点我打开课程库</a>
    </div>
</div>
</body>
</html>
"""
##################################################################
## XPath
## 1. 生成对象
selector = etree.HTML(html)
## 2. 提取文本, -------- xpath 可以通过 Chrome 中获得 --------
print(' '.join(selector.xpath('//ul/li/text()')))                              # // 两个表示从根路径开始; text() 内部输出文本
print(' '.join(selector.xpath('//ul[@id="useful"]/li/text()')))                # 添加条件, 上面的输出 6 个, 这里的输出 3 个
print(' '.join(selector.xpath('//html/body/div/ul[@id="useful"]/li/text()')))  # 可以补全所有的路径
## 3. 提取属性
print(' '.join(selector.xpath('//a/@href')))   # http://jikexueyuan.com http://jikexueyuan.com/course/
print(' '.join(selector.xpath('//a/@title')))  # 极客学院课程库
## 4. 其他情况
print(selector.xpath('//div[starts-with(@id, "con")]/text()'))           # 以 id="con-" 开头的 div; 这个还不知道为什么不能运行出正确结果...
print(selector.xpath('string(.)'))                                       # 还会保持缩进..., 好神奇
print(selector.xpath('string(.)').replace('\n', ' ').replace(' ', ';'))  # 将子标签中的内容也取出来, 并美化
##################################################################
## pyquery: 像 jquery 一样选择标签; 比 XPath 方便...
from pyquery import PyQuery as pq
## 0. 简单用法
print(pq('<div><span>toto</span><span>tata</span></div>').text())  # toto tata
print(pq('<div><span class="hello">toto</span><span>tata</span></div>').text())  # toto tata

## 1. 构造 $
# doc = pq(url='www.baidu.com')  # 可以直接传网站
doc = pq(html)  # doc 就像 jQuery 中的 $
print(type(doc))  # <class 'pyquery.pyquery.PyQuery'>

## 2. 提取元素
print(doc)  # 原样输出
print(doc.html())  # 只是把最外面的 <html> 去去掉了...
print(doc.text())  # 只输出文本
li = doc('li')   # 选取标签...
print(type(li))  # <class 'pyquery.pyquery.PyQuery'>; 还是 PyQuery 对象, 可以链式操作
print(li, li.text())
doc = pq('<p id="hello" class="hello"></p>')
p = doc('#hello'); print(p)  # <p id="hello" class="hello"/>
print(p.attr('class', 'jiaruipeng'))  # <p id="hello" class="jiaruipeng"/>

## 3. 删除元素
doc = pq(html)
print(doc("#content").remove())  # 会把删掉的元素返回, 这里会打印出来
print(doc.html())

## 4. 遍历
doc = pq(html)
lis = doc('li')
print(lis)
for li in lis.items(): print(li.html())
print(lis.each(lambda e: e))

## 5. 属性操作
p = pq('<p id="hello" class="hello"></p>')('p')
print(p.attr("id"))           # hello; 获取属性
print(p.attr("id", "plop"))   # <p id="plop" class="hello"/>; 修改属性
print(p.attr("id", "hello"))  # <p id="hello" class="hello"/>

p = pq('<p id="hello" class="hello"></p>')('p')  # 因为上面会修改原来样本
print(p.addClass('beauty'))  # <p id="hello" class="hello beauty"/>
print(p.removeClass('hello'))  # <p id="hello" class="beauty"/>
print(p.css('font-size', '16px'))  # <p id="hello" class="beauty" style="font-size: 16px"/>
print(p.css({'background-color': 'yellow'}))  # <p id="hello" class="beauty" style="font-size: 16px; background-color: yellow"/>

## 6. DOM 操作
p = pq('<p id="hello"></p>')('p')
print(p.append(' check out <a href="baidu"></a>'))  # <p id="hello"> check out <a href="baidu"/></p>
print(p.prepend('Oh yes!'))  # <p id="hello">Oh yes! check out <a href="baidu"/></p>
d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>'); print(d)
d.empty()
print(d)  # <div class="wrap"/>

## 7. 网页请求
# PyQuery 本身还有网页请求功能, 而且会把请求下来的网页代码转为 PyQuery 对象
print(pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True))
print(pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True))
# 这部分还是用 requests 比较好...

## 8. Ajax
# https://pythonhosted.org/pyquery/ajax.html
##################################################################
## 总结
# 1. XPath 的用法多少有点晦涩难记
# 2. PyQuery 初始化之后, 返回类型是 PyQuery, 利用了选择器筛选一次之后, 返回结果的类型依然还是 PyQuery, 这简直和 jQuery 如出一辙, 不能更赞
#    BeautifulSoup 和 XPath 返回的是什么? 列表!
# 3. 感觉以后模板可以用 pyquery 生成了...
# 4. BeautifulSoup 中 prettify() 和 unwrap() 这两个函数目前还是很好用的...
