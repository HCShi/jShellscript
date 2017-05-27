# !/usr/bin/python
# coding: utf-8
# 参考: [静觅: Python爬虫利器二之Beautiful Soup的用法](https://cuiqingcai.com/1319.html)
from bs4 import BeautifulSoup
import bs4
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, "lxml")  # 创建 BeautifulSoup 对象
# soup = BeautifulSoup(open('index.html'))  # 也可以直接将本地 html 文件打开
print(soup.prettify())  # 格式化输出
##################################################################
## bs4 将 HTML 转换成复杂的树形结构, 每个节点都是 Python 对象, 4 种: Tag, NavigableString, BeautifulSoup, Comment
## Tag
print(soup.title)  # <title>The Dormouse's story</title>
print(soup.head)  # <head><title>The Dormouse's story</title></head>
print(soup.a)  # 只输出了第一个  # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
print(soup.p)  # <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
print(type(soup.a))  # <class 'bs4.element.Tag'>
print(soup.name)  # [document]  # name 属性
print(soup.head.name)  # head  # soup 对象本身比较特殊, 它的 name 即为 [document], 对于其他内部标签, 输出的值便为标签本身的名称
print(soup.p.attrs)  # {'class': ['title'], 'name': 'dromouse'}  # 输出标签的属性
print(soup.p['class'])  # ['title']  # 单独获取某个属性
print(soup.p.get('class'))  # ['title']  # 利用get方法, 传入属性的名称, 二者是等价的
soup.p['class'] = "newClass"  # 对这些属性和内容等等进行修改
print(soup.p)  # <p class="newClass" name="dromouse"><b>The Dormouse's story</b></p>
del soup.p['class']  # 对某个属性进行删除
print(soup.p)  # <p name="dromouse"><b>The Dormouse's story</b></p>
##################################################################
## NavigableString 得到标签内部的文字
print(soup.p.string)  # The Dormouse's story
print(type(soup.p.string))  # <class 'bs4.element.NavigableString'>
##################################################################
## BeautifulSoup 文档的全部内容, 一个特殊的 Tag
print(type(soup.name))  # <type 'str'>
print(soup.name)  # [document]
print(soup.attrs)  # {} 空字典
##################################################################
## Comment 一个特殊类型的 NavigableString 对象, 其实输出的内容仍然不包括注释符号
print(soup.a)  # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
print(soup.a.string)  # Elsie  # 如果我们利用 .string 来输出它的内容, 我们发现它已经把注释符号去掉了, 所以这可能会给我们带来不必要的麻烦
print(type(soup.a.string))  # <class 'bs4.element.Comment'>
if type(soup.a.string) == bs4.element.Comment:  # 为了解决上面的麻烦, 我们最好先判断一下
    print(soup.a.string)

##################################################################
# 遍历文档树
##################################################################
print("\n# 直接子节点")
# .contents
print(soup.head.contents)  # [<title>The Dormouse's story</title>]  # tag 的 .content 属性可以将tag的子节点以列表的方式输出
print(soup.head.contents[0])  # #<title>The Dormouse's story</title>  # 上面输出为 列表
# .children 它返回的不是一个 list, 不过我们可以通过遍历获取所有子节点
print(soup.head.children)  # <listiterator object at 0x7f71457f5710>  # 是一个 list 生成器对象
for child in  soup.body.children:  # 获取 list 生成器对象中的内容
    print(child)

print("\n# 所有子孙节点")
# .descendants
# .contents 和 .children 属性仅包含tag的直接子节点, .descendants 属性可以对所有tag的子孙节点进行递归循环, 和 children类似, 我们也需要遍历获取其中的内容。
# for child in soup.descendants:
#     print child
# 运行结果如下, 可以发现, 所有的节点都被打印出来了, 先生最外层的 HTML标签, 其次从 head 标签一个个剥离, 以此类推。
print("这个太多了, 就注释了")

print("\n# 节点内容")
# .string
# 如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点。
# 如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同。
# 通俗点说就是：如果一个标签里面没有标签了, 那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了, 那么 .string 也会返回最里面的内容。例如
print(soup.head.string)  # The Dormouse's story
print(soup.title.string)  # The Dormouse's story
# 如果tag包含了多个子节点,tag就无法确定, string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
print(soup.html.string)  # None

print("\n# 多个内容")
# .strings  .stripped_strings
# .strings  # 获取多个内容, 不过需要遍历获取, 比如下面的例子
for string in soup.strings:  # 将所有的正文输出了
    # print(string)
#    print(repr(string))  # 可以将 回车 输出为 u'\n'
    pass
print("太多了, 被我注释了")
# .stripped_strings  # 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容
for string in soup.stripped_strings:
#    print(repr(string))
    pass
print("太多了, 被我注释了")

print("\n# 父节点")
# .parent 属性
p = soup.p
print(p.parent.name)  # body
content = soup.head.title.string
print(content.parent.name)  # title

print("\n# 全部父节点")
# parents 属性  # 通过元素的 .parents 属性可以递归得到元素的所有父辈节点, 例如
content = soup.head.title.string
for parent in  content.parents:
    print(parent.name)  # title, head, html, [document]

print("\n# 兄弟节点")
# next_sibling  .previous_sibling 属性
# 兄弟节点可以理解为和本节点处在统一级的节点, .next_sibling 属性获取了该节点的下一个兄弟节点, .previous_sibling 则与之相反, 如果节点不存在, 则返回 None
# 注意：实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白, 因为空白或者换行也可以被视作一个节点, 所以得到的结果可能是空白或者换行
print(soup.p.next_sibling)  # 实际该处为空白
print(soup.p.prev_sibling)  # None   没有前一个兄弟节点, 返回 None
print(soup.p.next_sibling.next_sibling)  # 结果为下面几行  # 下一个节点的下一个兄弟节点是我们可以看到的节点
# #<p class="story">Once upon a time there were three little sisters; and their names were
# #<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
# #<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# #<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# #and they lived at the bottom of a well.</p>

print("\n# 全部兄弟节点")
# next_siblings  .previous_siblings 属性  # 通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出
for sibling in soup.a.next_siblings:
    print((repr(sibling)))  # 结果下面几行
# u',\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# u' and\n'
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# u'; and they lived at the bottom of a well.'
# None

print("\n# 前后节点")
# next_element  .previous_element 属性  # 与 .next_sibling  .previous_sibling 不同, 它并不是针对于兄弟节点, 而是在所有节点, 不分层次
# 比如 head 节点为  <head><title>The Dormouse's story</title></head>  # 那么它的下一个节点便是 title, 它是不分层次关系的
print(soup.head.next_element)  # <title>The Dormouse's story</title>

print("\n# 所有前后节点")
# next_elements  .previous_elements 属性  # 通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样
# for element in last_a_tag.next_elements:
#     print(repr(element))

##################################################################
# 搜索文档树
##################################################################
print("\n# find_all( name , attrs , recursive , text , **kwargs )")  # find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
print("\n# 1) name")
# name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉
# A.传字符串  # 最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<b>标签
print(soup.find_all('b'))  # [<b>The Dormouse's story</b>]
print(soup.find_all('a'))  #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# B.传正则表达式
# 如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到
import re
for tag in soup.find_all(re.compile("^b")):
    print((tag.name))  # body, b
# C.传列表  # 如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签
print(soup.find_all(["a", "b"]))
# D.传 True  # True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
for tag in soup.find_all(True):
    print((tag.name))  # html, head, title, body, p, b, p, a, a
# E.传方法
# 如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数 [4] ,如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False
# 下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')  # 将这个方法作为参数传入 find_all() 方法,将得到所有<p>标签:
print(soup.find_all(has_class_but_no_id))

print("\n 2) keyword 参数")
# 注意：如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,
# Beautiful Soup会搜索每个tag的”id”属性
print(soup.find_all(id='link2'))  # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
# 如果传入 href 参数,Beautiful Soup会搜索每个tag的”href”属性
print(soup.find_all(href=re.compile("elsie")))  # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
# 使用多个指定名字的参数可以同时过滤tag的多个属性
print(soup.find_all(href=re.compile("elsie"), id='link1'))  # [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]
# 在这里我们想用 class 过滤, 不过 class 是 python 的关键词, 这怎么办？加个下划线就可以
print(soup.find_all("a", class_="sister"))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# 有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'lxml')
# print data_soup.find_all(data-foo="value")  # SyntaxError: keyword can't be an expression
# 但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag
print(data_soup.find_all(attrs={"data-foo": "value"}))  # [<div data-foo="value">foo!</div>]

print("\n 3) text 参数")
# 通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True
print(soup.find_all(text="Elsie"))  # [u'Elsie']
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))  # [u'Elsie', u'Lacie', u'Tillie']
print(soup.find_all(text=re.compile("Dormouse")))  # [u"The Dormouse's story", u"The Dormouse's story"]
print(soup.find_all(text="Elsie"))  # [u'Elsie']
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))  # [u'Elsie', u'Lacie', u'Tillie']
print(soup.find_all(text=re.compile("Dormouse")))  # [u"The Dormouse's story", u"The Dormouse's story"]

print("\n 4) limit 参数")
# find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.
# 效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.
# 文档树中有3个tag符合搜索条件,但结果只返回了2个,因为我们限制了返回数量
print(soup.find_all("a", limit=2))  # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

print("\n 5) recursive 参数")
# 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
# 一段简单的文档:
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
# 是否使用 recursive 参数的搜索结果:
soup.html.find_all("title")
# # [<title>The Dormouse's story</title>]
soup.html.find_all("title", recursive=False)
# # []

print("\n find( name , attrs , recursive , text , **kwargs )")
# 它与 find_all() 方法唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果

print("\n find_parents()  find_parent()")
# find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等. find_parents() 和 find_parent() 用来搜索当前节点的父辈节点,
# 搜索方法与普通tag的搜索方法相同,搜索文档搜索文档包含的内容

print("\n find_next_siblings()  find_next_sibling()")
# 这2个方法通过 .next_siblings 属性对当 tag 的所有后面解析的兄弟 tag 节点进行迭代, find_next_siblings() 方法返回所有符合条件的后面的兄弟节点,
# find_next_sibling() 只返回符合条件的后面的第一个tag节点

print("\n find_previous_siblings()  find_previous_sibling()")
# 这2个方法通过 .previous_siblings 属性对当前 tag 的前面解析的兄弟 tag 节点进行迭代,
# find_previous_siblings() 方法返回所有符合条件的前面的兄弟节点, find_previous_sibling() 方法返回第一个符合条件的前面的兄弟节点

print("\n find_all_next()  find_next()")
# 这2个方法通过 .next_elements 属性对当前 tag 的之后的 tag 和字符串进行迭代,
# find_all_next() 方法返回所有符合条件的节点, find_next() 方法返回第一个符合条件的节点

print("\n find_all_previous() 和 find_previous()")
# 这2个方法通过 .previous_elements 属性对当前节点前面的 tag 和字符串进行迭代,
# find_all_previous() 方法返回所有符合条件的节点, find_previous()方法返回第一个符合条件的节点

##################################################################
# CSS选择器
##################################################################
# 我们在写 CSS 时, 标签名不加任何修饰, 类名前加点, id名前加 #, 在这里我们也可以利用类似的方法来筛选元素,
# 用到的方法是 soup.select(), 返回类型是 list
print("\n 通过标签名查找")
print(soup.select('title'))  # [<title>The Dormouse's story</title>]
print(soup.select('a'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print(soup.select('b'))  # [<b>The Dormouse's story</b>]

print("\n 通过类名查找")
print(soup.select('.sister'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print("\n 通过 id 名查找")
print(soup.select('#link1'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

print("\n 组合查找")  # 组合查找即和写 class 文件时, 标签名与类名、id名进行的组合原理是一样的, 例如查找 p 标签中, id 等于 link1的内容, 二者需要用空格分开
print(soup.select('p #link1'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

print("\n 直接子标签查找")
print(soup.select("head > title"))  # [<title>The Dormouse's story</title>]

print("\n 属性查找")  # 查找时还可以加入属性元素, 属性需要用中括号括起来, 注意属性和标签属于同一节点, 所以中间不能加空格, 否则会无法匹配到。
print(soup.select('a[class="sister"]'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print(soup.select('a[href="http://example.com/elsie"]'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
# 同样, 属性仍然可以与上述查找方式组合, 不在同一节点的空格隔开, 同一节点的不加空格
print(soup.select('p a[href="http://example.com/elsie"]'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

print("\n 以上的 select 方法返回的结果都是列表形式, 可以遍历形式输出, 然后用 get_text() 方法来获取它的内容")
soup = BeautifulSoup(html, 'lxml')
print(type(soup.select('title')))  # list
print(soup.select('title')[0].get_text())  # The Dormouse's story
for title in soup.select('title'):
    print(title.get_text())  # The Dormouse's story
# 好, 这就是另一种与 find_all 方法有异曲同工之妙的查找方法, 是不是感觉很方便？
