#!/usr/bin/python3
# coding: utf-8
# Python 对协程的支持是通过 generator 实现 (for 迭代或者 next 获取 yield 返回值), yield 不但可以返回值, 它还可以接收调用者发出的参数
def consumer():  # 是一个生成器
    r = ''
    while True:
        n = yield r  # send() 的时候先赋值 n, 然后循环到这里 返回 r
        if not n: return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
def produce(c):
    c.send(None)  # 启动生成器, 执行到 n = yield r, 返回'' (因为 r='')
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 切换到 consumer 执行, 然后 produce 拿到 consumer 处理的结果, 继续生产下一条消息
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()  # 关闭 consumer
c = consumer()
produce(c)
# 1. 传 none 值到 consumer(), 激活, 执行到 n = yield r, 返回'' (因为r='')
# 2. 执行 produce(c), n=1, 执行r = c.send(n)时, 执行consumer(), 但是从if not n: 开始执行, 此时n=1, r被赋值为'200 OK',
#   while循环继续走到n = yield r返回r值, generator记录上下文并挂起
# 3. produce(c)函数中的r被赋值为 consumer()的返回值也就是'200 OK', 打印输出;
# 注意, 两个函数中的r不是同一个r, send(n)仅仅起到传递参数的作用;
