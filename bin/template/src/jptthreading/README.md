参考: [CTOlib](http://www.ctolib.com/docs-Python-Multithreading-c-index.html)
### Description
``` zsh
thread     # 多线程的底层支持模块, 一般不建议使用
threading  # 对 thread 进行了封装, 将一些线程的操作对象化
```
``` python
from threading  # 这样使用
from threading import Thread, Condition  # 这样不好
```
### threading 模块
``` zsh
Thread            # 线程类, 可以创建进程实例, 这是我们用的最多的一个类, 你可以指定线程函数执行或者继承自它都可以实现子线程功能

Timer             # 与 Thread 类似, 但要等待一段时间后才开始运行
Lock              # 锁原语, 这个我们可以对全局变量互斥时使用
RLock             # 可重入锁, 使单线程可以再次获得已经获得的锁
Condition         # 条件变量, 能让一个线程停下来, 等待其他线程满足某个"条件"
Event             # 通用的条件变量, 多个线程可以等待某个事件发生, 在事件发生后, 所有的线程都被激活
Semaphore         # 为等待锁的线程提供一个类似"等候室"的结构
BoundedSemaphore  # 与 Semaphore 类似, 但不允许超过初始值
Queue             # 实现了多生产者(Producer), 多消费者(Consumer)的队列, 支持锁原语, 能够在多个线程之间提供很好的同步支持
```
### Thread 类
``` zsh
getName(self)              # 返回线程的名字
isAlive(self)              # 布尔标志, 表示这个线程是否还在运行中
isDaemon(self)             # 返回线程的 daemon 标志
join(self, timeout=None)   # 阻塞当前上下文, 直至该线程运行结束, 程序挂起, 如果给出 timeout, 则最多阻塞 timeout 秒
run(self)                  # 定义线程的功能函数, 这个是在继承自 Thread 时, 需要重写的方法
setDaemon(self, daemonic)  # 把线程的 daemon 标志设为 daemonic
# 执行一个主线程, 主线程又创建一个子线程, 当主线程完成想退出时, 会检验子线程是否完成; 如果子线程未完成, 则主线程会等待子线程完成后再退出
# 但是有时候我们需要的是, 只要主线程完成了, 不管子线程是否完成, 都要和主线程一起退出, 这时就可以用 setDaemon 方法, 并设置其参数为 True
setName(self, name)        # 设置线程的名字
start(self)                # 开始线程执行
```
### Queue 提供的类
``` zsh
Queue          # 队列
LifoQueue      # 后入先出(LIFO)队列
PriorityQueue  # 优先队列
```
