#!/usr/bin/python3
# coding: utf-8
data = np.array([[float(x) for x in re.split(r'\s+', line.strip())] for line in fileinput.input('TSP_Data')])  # jptalgorithm 中用到的读取文件处理的命令
# 通常会使用 line.strip().split()
