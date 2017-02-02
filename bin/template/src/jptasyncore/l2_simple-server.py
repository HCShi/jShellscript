#!/usr/bin/python
# coding: utf-8
import asynchat, asyncore, socket
chat_room = {}  # 这个全局变量可以放到 ChatServer 中弄成成员变量, 不用 map 了
class ChatHandler(asynchat.async_chat):
    def __init__(self, sock):
        asynchat.async_chat.__init__(self, sock=sock, map=chat_room)
        self.set_terminator('\n')
        self.buffer = []
    def collect_incoming_data(self, data):  # 继承 asyn_chat, 只需重写 这两个方法就行了
        self.buffer.append(data)            # 这个方法可以监测到 socket 另一端发送的数据, 通过 append 来触发下面的函数
    def found_terminator(self):             # 当检测到 self.buffer 有 terminator 时触发
        msg = ''.join(self.buffer)
        print 'Received:', msg
        for handler in chat_room.itervalues():  # 可以不用 chat_room 变量, 而是在 ChatServer 类中存储建立的链接
            if hasattr(handler, 'push'):        # chat_room 中包含 dispatcher 和 asyn_chat 的对象, 后者才有 push 方法
                handler.push(msg + '\n')        # 传送的时候加上 terminator
        self.buffer = []                        # 处理完以后将 buffer 清空
class ChatServer(asyncore.dispatcher):          # 充当 服务器, 将每个会话链接交给 ChatHandler 来进行具体的处理
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self, map=chat_room)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(5)
    def handle_accept(self):  # 当有建立链接请求的时候触发这个函数
        pair = self.accept()  # 可以查看源代码, 看到很多的
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = ChatHandler(sock)  # 只需要传递 sock 就可以进行 回话处理了
server = ChatServer('localhost', 5050)
print 'Serving on localhost:5050'
asyncore.loop(map=chat_room)
