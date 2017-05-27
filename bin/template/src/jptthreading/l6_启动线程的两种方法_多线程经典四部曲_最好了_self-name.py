#!/usr/bin/python3
# coding: utf-8
import threading
##################################################################
# 方法一: 将函数传递进 Thread 对象
def thread_fun(num):
    for n in range(0, int(num)): print("I come from %s, num: %s" % (threading.currentThread().getName(), n))
def main(thread_num):
    thread_list = [];  # 多线程经典四步曲
    for i in range(0, thread_num): thread_list.append(threading.Thread(target=thread_fun, name=str(thread_num), args=(20,)))  # 先创建线程对象
    for thread in thread_list: thread.start()  # 启动所有线程
    for thread in thread_list: thread.join()  # 主线程中等待所有子线程退出
if __name__ == "__main__":
    main(3)
##################################################################
# 方法二: 继承自 threading.Thread 类
class MyThread(threading.Thread):
    def __init__(self): threading.Thread.__init__(self);  # 这里一定要注册一下
    def run(self): print("I am %s" % self.name)  # 需要重写 run(), 上面是用 target 指定函数; self.name, 线程自己有默认的名字
if __name__ == "__main__":
    for thread in range(0, 5):
        t = MyThread()
        t.start()
