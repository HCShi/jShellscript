#!/usr/bin/python3
# coding: utf-8
import threading
counterA, counterB = 0, 0
mutexA, mutexB = threading.Lock(), threading.Lock()
class MyThread(threading.Thread):
    def __init__(self): threading.Thread.__init__(self)
    def run(self):
        self.fun1(); self.fun2()  # 竟然锁不住, 运行太快了
    def fun1(self):
        global mutexA, mutexB
        if mutexA.acquire():
            print("I am %s , get res: %s" % (self.name, "ResA"))
            if mutexB.acquire():
                print("I am %s , get res: %s" % (self.name, "ResB"))
                mutexB.release()
            mutexA.release()
    def fun2(self):
        global mutexA, mutexB
        if mutexB.acquire():
            print("I am %s , get res: %s" % (self.name, "ResB"))
            if mutexA.acquire():
                print("I am %s , get res: %s" % (self.name, "ResA"))
                mutexA.release()
            mutexB.release()
if __name__ == "__main__":
    for i in range(0, 100):
        my_thread = MyThread()
        my_thread.start()
