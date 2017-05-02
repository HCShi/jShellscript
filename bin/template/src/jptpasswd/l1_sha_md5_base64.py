#!/usr/bin/python
# coding: utf-8
from hashlib import sha256
print(sha256('jrp'.encode()).hexdigest())  # sha256 加密, 64 位

from hashlib import md5
print(md5('jrp'.encode()).hexdigest())     # md5 加密, 32 位

from hashlib import sha1
print(sha1('jrp'.encode()).hexdigest())    # sha1 加密, 40 位

import base64
print(base64.b64encode('jrp'.encode()))    # base64 加密
print(base64.b64decode(base64.b64encode('jrp'.encode())))  # 解密
