#!/usr/bin/python3
# coding: utf-8
# 存储在计算机内存中的数据取决于 CPU 使用的架构, 它可以是小端 (最小有效位存储在最小地址中) 或大端 (最小有效字节存储在最大地址中)
import numpy as np
##################################################################
# numpy.ndarray.byteswap(); 函数通过传入 true 来原地大端和小端之间切换
a = np.array([1, 256, 8755], dtype=np.int16); print(a)  # [1 256 8755]
print(list(map(hex, a)))  # ['0x1', '0x100', '0x2233']; 以十六进制表示内存中的数据
print(a.byteswap(True))  # [256 1 13090]
print(list(map(hex, a)))  # ['0x100', '0x1', '0x3322']
