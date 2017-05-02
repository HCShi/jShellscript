#!/usr/bin/python3
# coding: utf-8
from wsgiref.simple_server import make_server
def application(environ, start_response):  # 符合WSGI标准的一个HTTP处理函数, 它接收两个参数
# environ: 包含所有 HTTP 请求信息的 dict 对象, start_response: 发送 HTTP 响应的函数
    with open('tmp', 'w') as f:
        for x, y in environ.items():
            f.write((str(x) + ':\t' + str(y) + '\n'))
    method = environ['REQUEST_METHOD']; print(method)
    path = environ['PATH_INFO']; print(path)
    start_response('200 OK', [('Content-Type', 'text/html')])  # (HTTP 响应码, 一组list表示的HTTP Header_每个Header用一个包含两个str的tuple表示)
    body = '<h1>Hello, %s!</h1>' % (path[1:] or 'web')
    return [body.encode('utf-8')]  # 通过 start_response() 发送 HTTP Header, 最后返回 HTTP Body
httpd = make_server('', 8000, application)  # 创建一个服务器, IP 地址为空, 端口是 8000, 处理函数是 application
httpd.serve_forever()  # 开始监听HTTP请求
# nc -v localhost 8000 -> GET /info HTTP/1.1 或者 浏览器 localhost:8000/info
