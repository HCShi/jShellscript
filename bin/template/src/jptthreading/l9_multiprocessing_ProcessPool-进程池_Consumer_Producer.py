#!/usr/bin/python
#coding=utf-8
# function: 自定义进程池遍历目录下文件, url: http://walkerqt.blog.51cto.com/1310630/1414703
# Queue 是进程和线程安全的; Queue 实现了 queue.Queue 的大部分方法, 但 task_done() 和 join() 没有实现
from multiprocessing import Process, Queue, Lock
import time, os
class Consumer(Process):  # 消费者
    def __init__(self, queue, ioLock):
        super(Consumer, self).__init__()
        self.queue, self.ioLock = queue, ioLock
    def run(self):
        while True:
            task = self.queue.get()  # 队列中无任务时, 会阻塞进程
            if isinstance(task, str) and task == 'quit': break;
            time.sleep(1)  # 假定任务处理需要 1 秒钟
            self.ioLock.acquire()  # 这里只是添加一个 print 的锁, 否则 print 会很乱
            print( str(os.getpid()) + '  ' + task)
            self.ioLock.release()
        self.ioLock.acquire()
        print 'Bye-bye'
        self.ioLock.release()
def Producer():  # 生产者
    queue = Queue()  # 这个队列是进程 / 线程安全的
    ioLock = Lock()  # 生成一个 threading.Lock 并返回一个 proxy
    subNum = 4  # 子进程数量
    workers = build_worker_pool(queue, ioLock, subNum)
    start_time = time.time()
    for parent, dirnames, filenames in os.walk(r'D:\test'):
        for filename in filenames:
            queue.put(filename)
            ioLock.acquire()
            print('qsize:' + str(queue.qsize()))
            ioLock.release()
            while queue.qsize() > subNum * 10:  # 控制队列中任务数量
                time.sleep(1)
    for worker in workers: queue.put('quit')
    for worker in workers: worker.join()
    ioLock.acquire()
    print('Done! Time taken: {}'.format(time.time() - start_time))
    ioLock.release()
def build_worker_pool(queue, ioLock, size):  # 创建进程池
    workers = []
    for _ in range(size):
        worker = Consumer(queue, ioLock)
        worker.start()
        workers.append(worker)
    return workers
if __name__ == '__main__':
    Producer()

