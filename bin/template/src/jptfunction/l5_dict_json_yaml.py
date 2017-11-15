#!/usr/bin/python3
# coding: utf-8
dic = dict({'a': 'A', 'b': 'B'})
print(dic.items(), dic.keys(), dic.values())  # Iterable, 'dict_values' object does not support indexing
print(next(iter(dic.values())))  # 将 dic.values() 转化为可迭代对象, 就可以用 next, 或者用 list() 对上面进行转型用索引
##################################################################
## 构造
words = ['hello', 'world', 'jia']; word_dict = dict((word, len(words) / (i+1)) for i, word in enumerate(words)); print(word_dict)  # Zipf's law
##################################################################
## get(); 针对 KeyError 的情况特别好使
dic = {'name':'Tim', 'age':23}
print(dic.get('workage'), 0)  # 如果没有的话, 初始值为 0
dic['workage'] = dic.get('workage', 0) + 1  # dic = {'age': 23, 'workage': 1, 'name': 'Tim'}
##################################################################
## dict()
keys = ['Name', 'Sex', 'Age']; values = ['Tim', 'Male', 23]
print(list(zip(keys, values)))  # [('Name', 'Tim'), ('Sex', 'Male'), ('Age', 23)]
dic = dict(zip(keys, values)); print(dic)  # {'Age': 23, 'Name': 'Tim', 'Sex': 'Male'}
# 测试去重
a = dict(zip(['a', 'a', 'b'], [1, 2, 3])); print(a)  # 会去重, 但是会丢失数据; ConditionalFreqDist
##################################################################
# Convert
import json, yaml
print(dict([(1, 'jrp')]))  # 只有长度是 2 的 tuple 才可以
# change int to "str"
strs = "{1: 'jrp'}"  # print(dict([(1, 'jrp')])) 的结果就是这个 strs, 但是要用 yaml 去解析..., 因为 json.loads 需要 key 被 "" 包围
print(yaml.load(strs), type(yaml.load(strs)))  # type of dict
print('eval: ', eval(strs), 'type: ', type(eval(strs)))  # dict's type, eval 执行一个字符串表达式, 并返回表达式的值
# change ' to "
strs = "{u'key':u'val'}"; print(strs)
strs = strs.replace("'", '"'); print(strs)
print(json.loads(strs.replace('u"', '"')))  # load return a type of dict
##################################################################
# 格式化输出
print(json.dumps([{'a': "A"}], indent=2))  # type(json) 是 str
print('\n'.join([x + ': ' +  y for x, y in {'a': 'A', 'b': 'B'}.items()]))
for x, y in {'a': 'A', 'b': 'B'}.items(): print(str(x) + ':\t' + str(y))  # 有时候上面那种方法在 [] 列表化时类型问题报错
import pprint; pprint.pprint({'a': {'b': 'B'}}, indent=1)  # 效果不是很好
##################################################################
# load dump
# file  # {"normal_count": 1} 带缩进的, 如果是 [{"normal_count": 1}], 下面就是 str 了
print(json.loads('{"a": "A"}'), type('{"a": "A"}'), type(json.loads('{"a": "A"}')))  # 将 python str 类型转化为 python dict
print(json.load(open('./l5_dict_json.json')))
print(json.dumps(open('./l5_dict_json.json').read(), indent=2))
##################################################################
# 键值翻转, 遍历
d = dict(name='Bob', age=20); print(dict(zip(d.values(), d.keys())))  # 键值反转
for item in d: print(item)  # name, age; 直接遍历输出的只是 key
for k, v in d.items(): print(k, v)  # items(), values(), keys() 返回值可以 list 列表化

# 总结:
# 1. load()/loads(), str 中的 key 部分必须用 "", 好变态, '' 的用 yaml
# 2. JSON 类型:   {}    []    'string'  123.456    ture/false  null
# 3. python 类型: dict  list  str       int/float  True/False  None
# 4. dumps() 方法返回一个 str, 内容就是标准的 JSON.
# 5. dump() 方法可以直接把 JSON 写入一个 file-like Object
# 5. loads() 或者对应的 load() 把 JSON 反序列化为 Python 对象, 前者把 JSON 的字符串反序列化, 后者从 file-like Object 中读取
# 6. dump: dict -> json(str);    load: str(json) -> dict
