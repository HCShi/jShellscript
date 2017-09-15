#!/usr/bin/python
# coding: utf-8
##################################################################
## 1. sha256
from hashlib import sha256
print(sha256('jrp'.encode()).hexdigest())  # sha256 加密, 64 位
##################################################################
## 2. md5
from hashlib import md5
print(md5('jrp'.encode()).hexdigest())     # md5 加密, 32 位
##################################################################
## 3. sha1
from hashlib import sha1
print(sha1('jrp'.encode()).hexdigest())    # sha1 加密, 40 位
##################################################################
## 4. base64
import base64
print(base64.b64encode('jrp'.encode()))    # base64 加密
print(base64.b64decode(base64.b64encode('jrp'.encode())))  # 解密
##################################################################
## 总结:
# 1. .encode(encoding="utf-8") 可以简写为 .encode()
# 2. 加密以前都要 .encode() 变为 byte
