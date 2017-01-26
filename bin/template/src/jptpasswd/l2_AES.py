#!/usr/bin/python
# coding: utf-8
from Crypto.Cipher import AES
import random, string, base64
# 因为 AES 内部始终使用 16 字节的分组长度.
# 加密时, 如果明文字节长度不是 16 的整数倍, 则需要通过如 ZeroPadding、PKCS#7 等填充方式对其进行补位填充
text = 'hellojrp'
text = text + ('\0' * (16 - (len(text) % 16)))  # 补全不够 16 位
key = ''.join(random.sample(string.ascii_letters + string.digits, 32))  # 32 字节
cipher = AES.new(key, AES.MODE_CBC, key[:16])  # 生成 AESCipher 对象, 解释在下面
cipher_text = cipher.encrypt(text)  # 对数据进行加密

encode = base64.b64encode(cipher_text)  # 这三行是进行为便于传输, 一般对加密后的数据进行 base64 编码
cipher = AES.new(key, AES.MODE_CBC, key[:16])
cipher_text = base64.b64decode(encode)

text = cipher.decrypt(cipher_text)
print text.rstrip('\0')  # 去掉末尾的 0

# key: 初始密钥. 根据 AES 规范, 可以是 16 字节、24 字节和32 字节长, 分别对应 128 位、192 位和 256 位;
# mode: 加密模式. 可以寻找相关的文档了解. 接下来的示例中会用到 CBC 模式, 因此在此作一个简单的阐述: CBC 模式是先将明文切分成若干小段, 然后每一小段与初始块或者上一段的密文段进行异或运算后, 再与密钥进行加密;
# vi: 初始化向量. 在部分加密模式中需要使用到, 如对于 CBC 模式来说, 它必须是随机选取并且需要保密的; 而且它的长度和密码分组相同 (AES 的分组长度固定为 16 字节)
