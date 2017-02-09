#!/usr/bin/python3
# coding: utf-8
import time, threading
balance = 0  # 假定这是你的银行存款
lock = threading.Lock()  # 创建一个锁 ================================ 加线的这几行是新添的
def change_it(n):
    global balance  # 先存后取, 结果应该为0
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(100000):
        lock.acquire()  # 先要获取锁  ================================
        try:
            change_it(n)  # 放心地改
        finally:
            lock.release()  # 改完了一定要释放锁  ===================================
t1 = threading.Thread(target=run_thread, args=[5,])
t2 = threading.Thread(target=run_thread, args=[8,])
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)  # 多试几次, 可能会出现非 0 结果
