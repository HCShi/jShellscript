#!/usr/bin/python3
# coding: utf-8
# 一个线程使用自己的局部变量比使用全局变量好, 因为局部变量只有线程自己能看见, 不会影响其他线程
# 全局变量的修改必须加锁
import threading
local_school = threading.local()  # 创建全局 ThreadLocal 对象
# 全局变量 local_school 就是一个 ThreadLocal 对象, 每个 Thread 对它都可以读写 student 属性, 但互不影响
# 可以把 local_school 看成全局变量, 但每个属性如 local_school.student 都是线程的局部变量, 也不用管理锁的问题
def process_student():
    std = local_school.student  # 获取当前线程关联的 student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
# Hello, Alice (in Thread-A)
# Hello, Bob (in Thread-B)
def process_thread(name):
    local_school.student = name  # 绑定 ThreadLocal 的 student
    process_student()
t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
