# coding: utf-8
# from threading import Thread, Condition
import threading, time, random  # 感觉 Condition 麻烦的话去看 ./l10_Queue_Consumer_Producer.py
##################################################################
# Condition(条件变量) 实现复杂同步; 流程为: acquire -> wait -> notify -> release
# acquire(), release(); 类似于 Lock 类  # wait() notify() notifyAll() 进入阻塞和唤醒其它, 这三个方法是特有的
# 首先 acquire 一个条件变量, 然后判断一些条件, 如果条件不满足则 wait; 如果条件满足, 进行一些处理改变条件后, 通过 notify 方法通知其他线程
# 其他处于 wait 状态的线程接到通知后会重新判断条件; 不断的重复这一过程, 从而解决复杂的同步问题
queue = []; MAX_NUM = 10; condition = threading.Condition()  # 工厂方法, 能让一个或多个线程 wait
class ProducerThread(threading.Thread):
    def run(self):
        global queue  # 表明是上面全局定义的那个 queue
        while True:
            condition.acquire()  # 请求一个锁
            if len(queue) == MAX_NUM:
                print("Queue full, producer is waiting")
                condition.wait()  # 释放锁, 进入阻塞
                print("Space in queue, Consumer notified the producer")
            num = random.randint(1, 5)  # 从 1-5 中选择一个数
            queue.append(num); print("Produced", num)  # list append num
            condition.notify()  # 唤醒一个在这个 condition 上阻塞的进程
            # 消费者被唤醒, 但要等到 release() 才能开始执行, notify() 并不释放 lock, lock 仍然为生产者所有, 如果没有消费者在 wait() 状态, 则空操作
            condition.release()  # 执行完以后, 释放锁
            time.sleep(random.random())  # secs 为单位
class ConsumerThread(threading.Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()  # 请求锁
            if not queue:
                print("Nothing in queue, consumer is waiting")
                condition.wait()  # 队列为空, 释放锁, 阻塞自己
                print("Producer added something to queue and notified the consumer")
            num = queue.pop(0); print("Consumed", num)
            condition.notify()
            condition.release()
            time.sleep(random.random())
ProducerThread().start()
ConsumerThread().start()
