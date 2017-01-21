#!/usr/bin/python
# coding: utf-8
import asynchat, asyncore, socket, threading
class ChatClient(asynchat.async_chat):  # 这里实现和服务器端 ChatHandler 逻辑类似的
    def __init__(self, host, port):
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.set_terminator('\n')
        self.buffer = []
    def collect_incoming_data(self, data):  # 当 socket 对面发来消息的时候触发
        self.buffer.append(data)  # 通过操作 self.buffer, 当检测到 terminator 触发 found_terminator
    def found_terminator(self):  # 进行逻辑操作
        msg = ''.join(self.buffer)
        print 'Received:', msg
        self.buffer = []
client = ChatClient('localhost', 5050)
threading.Thread(target=asyncore.loop).start()  # 使用双线程来控制交互
while True:
    msg = raw_input('> ')
    client.push(msg + '\n')
