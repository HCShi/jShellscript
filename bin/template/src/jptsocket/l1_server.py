#!/usr/bin/python
# coding: utf-8
import socket
sock = socket.socket()          # 可以不用声明 IPv4 和 TCP, 生成一个 socketobject, 和下面的 socke 类型相同
sock.bind(('127.0.0.1', 1234))  # 里面传的的 (元组)
sock.listen(4)                  # 设立最大连接数, 这句话必须有
while True:                     # 一般下面的 socke 会写成 conn, 但我认为那样不好, 很难想到 conn 和 socket 是同一种东西
    socke, addr = sock.accept() # 阻塞式监听, 应该用一个 list/dict 来存放连接, socke 是一个新的 socket, 并且和客户端的 sock 不是同一个
    print addr                  # addr 还是一个元组 ('127.0.0.1', 45678)
    socke.send('hello')         # 数据传输
    socke.close()               # 关闭 socket, type(socke) -> socket._socketobject
