#!/usr/bin/python
# coding: utf-8
from lxml import etree
# html = open('./l2.html').read()  # 将 l2.html 直接复制进来了
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
        <li>不需要的信息1</li>
        <li>不需要的信息2</li>
        <li>不需要的信息3</li>
    </ul>
    <div id="url">
        <a href="http://jikexueyuan.com">极客学院</a>
        <a href="http://jikexueyuan.com/course/" title="极客学院课程库">点我打开课程库</a>
    </div>
</div>
</body>
</html>
"""
# 1. 生成对象
selector = etree.HTML(html)

# 2. 提取文本, -------- xpath 可以通过 Chrome 中获得 --------
print(' '.join(selector.xpath('//ul/li/text()')))  # print selector.xpath() 会显示 unicode
print(' '.join(selector.xpath('//ul[@id="useful"]/li/text()')))  # 添加条件, 上面的输出 6 个, 这里的输出 3 个
print(' '.join(selector.xpath('//html/body/div/ul[@id="useful"]/li/text()')))  # 可以补全所有的路径

# 3. 提取属性
print(' '.join(selector.xpath('//a/@href')))  # http://jikexueyuan.com http://jikexueyuan.com/course/
print(' '.join(selector.xpath('//a/@title')))  # 极客学院课程库

# 4. 其他情况
# selector.xpath('//div[starts-with(@id, "test")]/text()')  # 以 id="text-" 开头的 div
# selector.xpath('string(.)').replace('\n', '').replace(' ', '')  # 将子标签中的内容也取出来, 并美化
