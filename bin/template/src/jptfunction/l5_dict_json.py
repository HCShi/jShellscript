#!/usr/bin/python3
# coding: utf-8
print(dict([('name', 'jrp')]))  # 只有长度是 2 的 tuple 才可以
import json
# 格式化
print(json.dumps([{'a': "A"}], indent=2))  # type(json) 是 str
print('\n'.join([x + ': ' +  y for x, y in {'a': 'A', 'b': 'B'}.items()]))
for x, y in {'a': 'A', 'b': 'B'}.items(): print(str(x) + ':\t' + str(y))  # 有时候上面那种方法在 [] 列表化时类型问题报错
import pprint; pprint.pprint({'a': {'b': 'B'}}, indent=1)  # 效果不是很好

# file  # {"normal_count": 1} 带缩进的, 如果是 [{"normal_count": 1}], 下面就是 str 了
print(json.loads('{"a": "A"}'))  # 将 python str 类型转化为 python dict
print(json.load(open('./l5_dict_json.json')))
print(json.dumps(open('./l5_dict_json.json').read(), indent=2))
d = dict(name='Bob', age=20); print(dict(zip(d.values(), d.keys())))  # 键值反转
for k, v in d.items(): print(k, v)  # items(), values(), keys() 返回值可以 list 列表化

# 总结:
# 1. 读取文件时, 文件中 dict 必须用 "", 好变态
# 2. JSON 类型:   {}   []   'string' 123.456   ture/false null
# 3. python 类型: dict list str      int/float True/False None
# 4. dumps() 方法返回一个 str, 内容就是标准的JSON.
# 5. dump() 方法可以直接把 JSON 写入一个 file-like Object
# 5. loads() 或者对应的 load() 把 JSON 反序列化为 Python 对象, 前者把 JSON 的字符串反序列化, 后者从 file-like Object 中读取
