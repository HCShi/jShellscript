#!/usr/bin/python
# coding=utf-8
import re  # 没有 ./l1_re_findall_search_sub_split.py 中的常用, patten 模式已经被放弃了
##################################################################
## compile match
pattern = re.compile(r'hello')  # 将正则表达式编译成 Pattern 对象
match = pattern.match('hello hello world!')  # 使用 Pattern 匹配文本, 获得匹配结果, 无法匹配时将返回 None
if match: print(match.group(), match.groups(), match)  # hello (); 只能匹配第一个
# match(string[, pos[, endpos]]) | re.match(pattern, string[, flags]):
# pos 和 endpos 的默认值分别为 0 和 len(string); re.match() 无法指定这两个参数, 参数 flags 用于编译 pattern 时指定匹配模式
# 注意: 这个方法并不是完全匹配; 当 pattern 结束时若 string 还有剩余字符, 仍然视为成功; 想要完全匹配, 可以在表达式末尾加上边界匹配符 '$'
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
# re.I(re.IGNORECASE): 忽略大小写 (括号内是完整写法, 下同)
# M(MULTILINE): 多行模式, 改变'^'和'$'的行为 (参见上图)
# S(DOTALL): 点任意匹配模式, 改变'.'的行为
# L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
# U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
# X(VERBOSE): 详细模式; 这个模式下正则表达式可以是多行, 忽略空白字符, 并可以加入注释; 以下两个正则表达式是等价的:
b = re.compile(r"\d+\.\d*")
##################################################################
## Match; 少写 compile, 但无法复用模式
m = re.match(r'hello', 'hello world!'); print(m.group())  # hello
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print(m.string)       # string: 匹配时使用的文本
print(m.re)           # re: 匹配时使用的 Pattern 对象
print(m.pos)          # pos: 文本中正则表达式开始搜索的索引; 值与 Pattern.match() 和 Pattern.seach() 方法的同名参数相同
print(m.endpos)       # endpos: 文本中正则表达式结束搜索的索引; 值与 Pattern.match() 和 Pattern.seach() 方法的同名参数相同
print(m.lastindex)    # lastindex: 最后一个被捕获的分组在文本中的索引; 如果没有被捕获的分组, 将为 None
print(m.lastgroup)    # lastgroup: 最后一个被捕获的分组的别名; 如果这个分组没有别名或者没有被捕获的分组, 将为 None
print(m.group(1, 2))  # group([group1, ...]):
# 获得一个或多个分组截获的字符串; 指定多个参数时将以元组形式返回; group1可以使用编号也可以使用别名; 编号 0 代表整个匹配的子串;
# 不填写参数时, 返回 group(0); 没有截获字符串的组返回 None; 截获了多次的组返回最后一次截获的子串]
print(m.groups())            # 以元组形式返回全部分组截获的字符串, 相当于调用 group(1, 2, ..., last)
print(m.groupdict())         # 返回以有别名的组的别名为键、以该组截获的子串为值的字典, 没有别名的组不包含在内
print(m.start(2))            # start([group]); 返回指定的组截获的子串在 string 中的起始索引 (子串第一个字符的索引) group 默认值为 0
print(m.end(2))              # end([group]); 返回指定的组截获的子串在 string 中的结束索引 (子串最后一个字符的索引 +1), group 默认值为 0
print(m.span(2))             # span([group]); 返回 (start(group), end(group))]
print(m.expand(r'\2 \1\3'))  # expand(template);
# 将匹配到的分组代入 template 中然后返回. template中可以使用 \id 或 \g<id>、\g<name> 引用分组, 但不能使用编号 0. \id 与 \g<id> 是等价的;
# 但 \10 将被认为是第 10 个分组, 如果你想表达 \1 之后是字符 '0', 只能使用 \g<1>0
##################################################################
## Pattern 对象是一个编译好的正则表达式, Pattern 不能直接实例化, 必须使用 re.compile() 进行构造
p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)
print(p.pattern)     # pattern: 编译时用的表达式字符串
print(p.flags)       # flags: 编译时用的匹配模式. 数字形式
print(p.groups)      # groups: 表达式中分组的数量
print(p.groupindex)  # groupindex: 以表达式中有别名的组的别名为键、以该组对应的编号为值的字典, 没有别名的组不包含在内
##################################################################
## 实例方法: search, split, findall, finditer, sub, subn
pattern = re.compile(r'world')  # 将正则表达式编译成 Pattern 对象
match = pattern.search('hello world!')  # 这个例子中使用 match() 无法成功匹配
if match: print(match.group())  # world
p = re.compile(r'\d+')
print(p.split('one1two2three3four4'))  # ['one', 'two', 'three', 'four', '']
p = re.compile(r'\d+')
print(p.findall('one1two2three3four4'))  # ['1', '2', '3', '4']
p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'): print(m.group(), end=' ')  # 1 2 3 4
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(p.sub(r'\2 \1', s))  # say i, world hello!; 位置交换, 好厉害...
def func(m): return m.group(1).title() + ' ' + m.group(2).title()
print(p.sub(func, s))  # I Say, Hello World! # 还可以添加函数, 更厉害了...
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(p.subn(r'\2 \1', s))  # ('say i, world hello!', 2)
def func(m): return m.group(1).title() + ' ' + m.group(2).title()
print(p.subn(func, s))  # ('I Say, Hello World!', 2)
