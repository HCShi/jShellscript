#!/usr/bin/python3
# coding: utf-8
import threading
balance = 0  # 假定这是你的银行存款
lock = threading.Lock()  # 创建一个锁 ================================ 加线的这几行是新添的
def change_it(n):
    global balance  # 先存后取, 结果应该为 0
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(100000):
        lock.acquire()  # 先要获取锁  ================================
        try: change_it(n)  # 放心地改
        finally: lock.release()  # 改完了一定要释放锁  ===================================
t1 = threading.Thread(target=run_thread, args=[5,])
t2 = threading.Thread(target=run_thread, args=[8,])
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)  # 一直是 0
# 一个线程调用 Lock 的 acquire() 方法获得锁时, 这把锁就进入 "locked" 状态; 只有一个线程 1 可以获得锁
# 一个线程 2 试图获得这个锁, 线程 2 就会变为 "block" 同步阻塞状态, 直到线程 1 调用锁的 release() 方法释放锁之后, 该锁进入 "unlocked" 状态
# 线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁, 并使得该线程进入运行 (running) 状态
