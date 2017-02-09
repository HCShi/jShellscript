#!/usr/bin/python3
# coding: utf-8
import threading
import asyncio  # Python 3.4 引入, Python 3.5 引入了更加简单的 async 和 await
@asyncio.coroutine  # generator 标记为 coroutine 类型, 然后把这个 coroutine 扔到 EventLoop 中执行
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    r = yield from asyncio.sleep(1)  # 异步调用 asyncio.sleep(1), 主线程并未等待, 而是去执行 EventLoop 中其他可以执行的 coroutine 了
    # yield from 语法可以让我们方便地调用另一个generator. 由于 asyncio.sleep() 也是一个 coroutine
    # 所以线程不会等待 asyncio.sleep(), 而是直接中断并执行下一个消息循环. 当 asyncio.sleep() 返回时
    # 线程就可以从 yield from 拿到返回值 (此处是None), 然后接着执行下一行语句
    print('Hello again! (%s)' % threading.currentThread())
loop = asyncio.get_event_loop()  # 从 asyncio 模块中直接获取一个 EventLoop 的引用
# loop.run_until_complete(hello())  # 然后把需要执行的协程扔到 EventLoop 中执行, 就实现了异步 IO
tasks = [hello(), hello()]  # task 封装 两个 coroutine
loop.run_until_complete(asyncio.wait(tasks))
# loop.close()  # 因为下面还有任务, 这里就不能结束

# 异步网络连接来获取 sina、sohu 和 163 的网站首页
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect  # 异步操作需要在 coroutine 中通过 yield from 完成
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n': break  # Ignore the body, close the socket 只输出 HTTP Header, HTTP Body 会被中断
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# async 和 await 是针对 coroutine 的新语法, 要使用新的语法, 只需要做两步简单的替换
# 1. @asyncio.coroutine 替换为 async 2. 把 yield from 替换为 await
async def hello():  # 只有这个函数需要修改, 其他的不变
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")
loop = asyncio.get_event_loop(); loop.run_until_complete(hello()); loop.run_until_complete(asyncio.wait(tasks))
loop.close()
