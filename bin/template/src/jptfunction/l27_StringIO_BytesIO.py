#!/usr/bin/python3
# coding: utf-8
from io import StringIO
# 要把 str 写入 StringIO, 我们需要先创建一个 StringIO, 然后像文件一样写入即可
f = StringIO()
tmp = f.write('hello'); print(tmp)  # 5, 返回值是 str 长度
f.write(' '); f.write('world!'); print(f.getvalue())  # hello world!, getvalue() 方法用于获得写入后的 str

# 要读取 StringIO, 可以用一个 str 初始化 StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline();
    if s == '': break;
    print(s.strip())

# 将 stdout 重定向到 StringIO
import sys
buff = StringIO()
temp = sys.stdout  # 保存标准 I/O 流
sys.stdout = buff  # 将标准 I/O 流重定向到 buff 对象
print(42, 'hello', 0.001)
sys.stdout =temp   # 恢复标准 I/O 流, 必须保存了再恢复, 否则就不能正常输出了...
print(buff.getvalue())

# StringIO 操作的只能是 str,  如果要操作二进制数据, 就需要使用 BytesIO
# BytesIO 实现了在内存中读写 bytes, 我们创建一个 BytesIO, 然后写入一些 bytes
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))  # 返回 6, 请注意, 写入的不是 str, 而是经过 UTF-8 编码的 bytes
print(f.getvalue())  # b'\xe4\xb8\xad\xe6\x96\x87'

# 和 StringIO 类似, 可以用一个 bytes 初始化 BytesIO, 然后, 像读文件一样读取
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())  # b'\xe4\xb8\xad\xe6\x96\x87'

# 总结
# StringIO 和 BytesIO 是在内存中操作 str 和 bytes 的方法, 使得和读写文件具有一致的接口

