#!/usr/bin/python3
# coding: utf-8
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')  # debug, info, warning, error 几个级别
def foo(s): return 10 / int(s)
def bar(s): return foo(s) * 2
def main():
    n = 5; logging.info('n = %d' % n)  # 这里用了 info, 所以只有上面是 logging.INFO 才可以
    try: bar('0')  # 不用每个函数都写 try, 只要有一个地方写就行了
    except Exception as e: logging.exception(e)  # logging 好处是可以输出到文件
main(); print('END')

class Dict(dict):  # 先编写一个类, 下面的 TestDict 就是测试类, 一般测试类要分开文件放
    def __init__(self, **kw): super().__init__(**kw)
    def __getattr__(self, key):
        try: return self[key]
        except KeyError: raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value): self[key] = value
import unittest  # 单元测试可以同时测试好多情况, 代码重构时比较方便
class TestDict(unittest.TestCase):  # 编写一个测试类, 从 unittest.TestCase 继承
    def test_init(self):  # test_ 开头的方法默认是测试方法, 测试的时候会执行
        d = Dict(a=1, b='test')
        self.assertEqual(abs(-1), 1)  # 断言函数返回的结果与 1 相等
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):  # 期待抛出指定类型的 Error, 比如通过 d['empty'] 访问不存在的 key 时, 断言会抛出 KeyError
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):  # 通过 d.empty 访问不存在的 key 时, 我们期待抛出 AttributeError
            value = d.empty
if __name__ == '__main__':
    unittest.main()
