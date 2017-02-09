#!/usr/bin/python3
# coding: utf-8
import threading; print(threading.currentThread())  # 输出当前线程名称

# 新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 2:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
    print('thread %s ended.' % threading.current_thread().name)
print('thread %s is running...' % threading.current_thread().name)  # 主线程默认 MainThread
t = threading.Thread(target=loop, name='LoopThread')  # 子线程的名字在创建的时候指定, 系统默认指定名字
t.start()
t.join()  # 不加 join, 进 loop 以后就出不来的, 不会执行下面这句就直接结束了
print('thread %s ended.' % threading.current_thread().name)
threading.Thread(target=loop).start()  # 简短的写法
