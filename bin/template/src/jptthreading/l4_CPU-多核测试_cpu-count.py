#!/usr/bin/python3
# coding: utf-8
# 我们可以监控到一个死循环线程会 100% 占用一个CPU, 两个死循环线程, 在多核 CPU 中, 可以监控到会占用 200% 的 CPU
# 要想把 N 核 CPU 的核心全部跑满, 就必须启动 N 个死循环线程
import threading, multiprocessing
def loop():
    x = 0
    while True: x = x ^ 1
print(multiprocessing.cpu_count())  # 4
for i in range(multiprocessing.cpu_count()):
    threading.Thread(target=loop).start()
