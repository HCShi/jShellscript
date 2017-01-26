#!/usr/bin/python
# coding: utf-8
import json
# list <-> json
data_list = [{'a': "A", 'b': (2, 4), 'c': 3.0}]  # list对象
print 'LIST:', repr(data_list), type(data_list)   # 上面的原样输出, list
data_json = json.dumps(data_list, indent=2)  # json.dumps() 把 Python 对象编码转换成 Json 字符串, 不加 indent 没有格式化
print "JSON:", data_json, type(data_json), repr(data_json)  # 元组转化为 list, json 格式是 str, 显示出 '\n' 的位置
data_list = json.loads(data_json)  # json.loads() 把 Json 格式字符串解码转换成 Python 对象(默认是 list[unicode])
print "LIST:", data_list, type(data_list)

# dict <-> json
data_dict = {'a': "A", 'b': (2, 4), 'c': 3.0}  # dict对象
print "DICT:", repr(data_dict), type(data_dict)
data_json = json.dumps(data_dict)  # str 对象, json 格式就是 str
print "JSON:", data_json, type(data_json)  # {"a": "A", "c": 3.0, "b": [2, 4]} <type 'str'>
data_dict = json.loads(data_json)
print "DICT", data_dict, type(data_dict)  # 子元素同样是 unicode

# list + tuple <-> dict
tmp_list = [('name', 'jrp')]  # 只有长度是 2 的 tuple 才可以
print 'DICT:', dict(tmp_list)  # {'name': 'jrp'}

# file  # {"normal_count": 1} 带缩进的, 如果是 [{"normal_count": 1}], 下面就是 str 了
data = json.load(open('./l5_dict_json.json'))  # 将文件默认为 json, 并将其加载并转化为 list, 如果文件不是 json 格式会报错
print 'DICT:', data, type(data) # {u'normal_count': 1}, dict
data = json.dumps(open('./l5_dict_json.json').read(), indent=2)  # 这里要用上 read(), 但是结果带 "", 就跟 repr() 的结果一样
print 'JSON:', data, type(data) # "{\n    \"normal_count\": 1\n}\n" <type 'str'>, 这里的带上了 "", 不太好用

# 总结:   --------- 文件中 dict 必须用 ""
# json.load()  # 针对不同的内容返回不同的类型, 有 dict 或者 list
# json.dumps()  # 可以将 list 或 dict 转化为 str(json的默认类型)

# dict: key <-> value
data = {'name': 'jrp'}; print type(data)  # dict
print dict(zip(data.values(), data.keys()))  # {'jrp': 'name'}
