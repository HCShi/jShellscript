#!/usr/bin/python3
# coding: utf-8
# asyncio 可以实现单线程并发 IO 操作. 如果仅用在客户端, 发挥的威力不大. 如果把 asyncio 用在服务器端
# 例如 Web 服务器, 由于 HTTP 连接就是 IO 操作, 因此可以用单线程 +coroutine 实现多用户的高并发支持.
# asyncio实现了TCP、UDP、SSL等协议, aiohttp则是基于asyncio实现的HTTP框架
import asyncio
from aiohttp import web
async def index(request):  # aiohttp.web.request 实例, 包含了所有浏览器发送过来的 HTTP 协议里面的信息, 一般不用自己构造
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')
# aiohttp.web.response 实例, 由 web.Response(body='') 构造, 继承自 StreamResponse, 功能为构造一个 HTTP 响应类声明
# class aiohttp.web.Response(*, status=200, headers=None, content_type=None, body=None, text=None)
async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))
# aiohttp 的初始化函数 init() 也是一个 coroutine, loop.create_server() 则利用 asyncio 创建 TCP 服务
async def init(loop):
    app = web.Application(loop=loop)  # 上面两个函数是处理函数, 这里是创建 Web 服务器, 处理 URL HTTP
    app.router.add_route('GET', '/', index)  # 将处理函数注册进其应用路径 Application.router
    app.router.add_route('GET', '/hello/{name}', hello)
    # 用协程创建监听服务, 其中 loop 为传入函数的协程, 并使用 aiohttp 中的 HTTP 协议簇 (protocol_factory)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)  # aiohttp.RequestHandlerFactory(协议簇创建套接字)用 make_handle() 创建
    # yield from 返回一个创建好的, 绑定IP、端口、HTTP 协议簇的监听服务的协程, yield from 的作用是使 srv 的行为模式和 loop.create_server() 一致
    print('Server started at http://127.0.0.1:8000...')
    return srv
# 下面是创建协程, 初始化协程并返回监听服务, 进入协程执行
loop = asyncio.get_event_loop()  # 返回 asyncio.BaseEventLoop 的对象, 协程的基本单位
loop.run_until_complete(init(loop))  # 运行协程, 直到完成, BaseEventLoop.run_until_complete(future)
loop.run_forever()  # 运行协程, 直到调用 stop(), BaseEventLoop.run_forever()

# 各种缩写
# app   Application
# loop  WindowsSelectEventLoop
# srv   SocketSever
