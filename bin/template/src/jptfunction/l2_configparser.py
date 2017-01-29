#!/usr/bin/python3
# coding: utf-8
import string, os, sys
import configparser
cfg = configparser.ConfigParser()

# 写入
cfg.add_section('aliyun.com')  # 添加 Section
cfg.set('aliyun.com', 'password', 'root, hello, world')  # 添加键值对, split(', '), 可以将其分开
cfg.set('aliyun.com', 'username', 'root')
cfg.add_section('qcloud.com')
cfg.write(open("/home/coder352/Documents/thiscandel/tmp.ini", "w"))  # 保存

# 读取
cfg.read('/home/coder352/Documents/thiscandel/tmp.ini')
print(cfg.sections())  # 得到所有的 Section, 并以 list 的形式返回
print(cfg.options('aliyun.com'))  # 得到该 Section 的所有 Option, 返回 list
print(cfg.items('aliyun.com'))  # 得到该 Section 的所有键值对, list 嵌套元组
print(cfg.get('aliyun.com', 'password'))  # 得到 Section 中 Option 的值，返回为 string 类型
# 不使用 getint, getfloat 等, 因为可以自己转换

# 删除
cfg.remove_option('aliyun.com', 'username')
print(cfg.options('aliyun.com'))
cfg.remove_section('aliyun.com')
print(cfg.sections())
