#!/usr/bin/python3
# coding: utf-8
import numpy as np
##################################################################
# numpy.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)  # 生成 ndarray 类的实例
# object 暴露数组接口方法的对象都会返回一个数组或任何(嵌套)序列
# dtype 数据类型; copy 可选, 默认为 true, 对象是否被复制; order C(按行) F(按列) A(任意, 默认)
# subok 默认情况下, 返回的数组被强制为基类数组, 如果为 true, 则返回子类; ndimin 指定返回数组的最小维数
a, b = np.array([1, 2, 3]), np.array([[1, 2], [3, 4]]); print(a, '\n', b)  # [1 2 3], [[1 2] [3 4]]
a = np.array([1, 2, 3], ndmin=2, dtype=complex); print(a)  # [[ 1.+0.j  2.+0.j  3.+0.j]], complex 不用带引号, int 需要
a = np.array(np.array([1, 2])); print(a)  # 可以多层嵌套
# dtype=np.int8, dtype=np.float32, dtype=np.int, dtype=int
##################################################################
# numpy.dtype(object, align, copy)  # 数据类型 描述了对应于数组的固定内存块的解释, 取决于以下方面
# object: 被转换为数据类型的对象; align: 如果为true, 则向字段添加间隔
# copy: 生成 dtype 对象的新副本, 如果为 flase, 结果是内建数据类型对象的引用
# 数据类型(整数、浮点或者 Python 对象); 数据大小; 字节序(小端或大端); 字段的名称, 每个字段的数据类型, 和每个字段占用的内存块部分; 如果数据类型是子序列, 它的形状和数据类型
# 字节顺序取决于数据类型的前缀 < 或 >; < 意味着编码是小端(最小有效字节存储在最小地址中); > 意味着编码是大端(最大有效字节存储在最小地址中)
dt = np.dtype(np.int32); print(dt)  # int32; 使用数组标量类型
dt = np.dtype('i4'); print(dt)  # int32; int8, int16, int32, int64 可替换为等价的字符串 'i1', 'i2', 'i4', 以及其他
dt = np.dtype('>i4'); print(dt)  # >i4; 使用端记号
# 下面的例子展示了结构化数据类型的使用, 这里声明了字段名称和相应的标量数据类型
dt = np.dtype([('age', np.int8)]); print(dt)  # [('age', 'i1')]; 首先创建结构化数据类型
a = np.array([(10,), (20,), (30,)], dtype=dt); print(a)  # [(10,) (20,) (30,)]; 现在将其应用于 ndarray 对象
print(a['age'])  # [10 20 30]; 文件名称可用于访问 age 列的内容
# 以下示例定义名为 student 的结构化数据类型, 其中包含字符串字段 name, 整数字段 age 和浮点字段 marks
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')]); print(student)  # [('name', 'S20'), ('age', 'i1'), ('marks', '<f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student); print(a)  # [('abc', 21, 50.0), ('xyz', 18, 75.0)]
# 'b': 布尔值; 'i': 符号整数; 'u': 无符号整数; 'f': 浮点; 'c': 复数浮点; 'm': 时间间隔;
# 'M': 日期时间; 'O': Python 对象; 'S', 'a': 字节串; 'U': Unicode; 'V': 原始数据(void)
##################################################################
## astype; 类型转换时用 astype, 不要直接修改 dtype
a = np.random.random(4); print(a)  # [ 0.10995627  0.23018423  0.12878835  0.60813773]
print(a.dtype, a.shape)  # float64 (4,)
a.dtype = 'float32'; print(a.shape)  # (8,); 改变 dtype, 发现数组长度翻倍; 而且打印出来很乱
a.dtype = 'float16'; print(a.shape)  # (16,); 改变dtype, 数组长度再次翻倍
a.dtype = 'float'  # 改变 dtype='float', 发现默认就是 float64, 长度也变回最初的 4
print(a)  # [ 0.10995627  0.23018423  0.12878835  0.60813773]
print(a.shape, a.dtype)  # (4,) dtype('float64')
a.dtype = 'int'
print(a.dtype, a.shape)  # int64, (4,)
print(a)  # [ 1637779016,  1069036447, -1764917584,  1071690807,  -679822259, 1071906619, -1611419360,  1070282372]
# 很多时候我们用 numpy 从文本文件读取数据作为 numpy 的数组, 默认的 dtype 是 float64
# 但是有些场合我们希望有些数据列作为整数; 如果直接改 dtype='int' 的话, 就会出错！原因如上
b = np.array([1., 2., 3., 4.]); print(b.dtype)  # float64
c = b.astype(int); print(c)  # [1 2 3 4]
print(c.shape, c.dtype)  # (4,) int64
