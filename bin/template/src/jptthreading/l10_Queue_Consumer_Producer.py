#!/usr/bin/python
# coding = utf-8
# Queue 封装了 Condition 的行为, 如 wait(), notify(), acquire();  Python 中的是 synchronized queue 同步队列
# 这个队列有一个 condition, 它有自己的 lock, 如果你使用 Queue, 你不需要为 condition 和 lock 而烦恼
# 优点是对于 读取/修改 mutex 方便, 不用显式的表达锁, 缺点是 对于 mutex 不明显, 或者需要对代码段加锁的不方便
from threading import Thread
import time, random
from queue import Queue
queue = Queue(10)
class ProducerThread(Thread):
    def run(self):  # 重写 Thread 的 run() 方法
        global queue
        while True:
            num = random.randint(1, 5)  # 1, 2, 3, 4, 5
            queue.put(num)  # put() 在插入数据前有一个获取 lock 的逻辑, put() 也检查队列是否已满; 如果已满, 它会在内部调用 wait(), 生产者开始等待
            print("Produced", num); time.sleep(random.random())
class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()  # get() 从队列中移出数据前会获取 lock, get() 会检查队列是否为空, 如空, 消费者进入等待状态
            # get() 和 put() 都有适当的notify(), 去看 Queue 的源码吧
            queue.task_done()  # task_done 在多线程中告诉 queue 上面的 get() 完成了
            print("Consumed", num); time.sleep(random.random())
ProducerThread().start()
ConsumerThread().start()

