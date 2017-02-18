#!/usr/bin/python
# coding: utf-8
# 默认指定文件为 fabfile.py, 放到根项目就行了, 否则需要 -f file_name.py 来执行, 下面的命令都是默认的 fabfile.py
def hello(): print('Hello Jrp')  # fab hello 就可以执行这个函数... gg, 只是这一行就是一个简单的 项目构建工具, Makefile...
def hello(name="world"): print("Hello %s!" % name)  # fab hello:name=jrp 或者 fab hello:jrp, 还带函数重载的功能

from fabric.api import local, abort, lcd  # 可以调用本地的命令了
def test_local(): local("ls")  # 本地 Shell 命令并与之交互  # def push(): local("git push")  # 根据自己的习惯来定义函数
def test_abort(): abort("abort here")  # 会报错, 内容就是 str参数
def test_lcd(): lcd('~')  # 好像只是切换目录, local() 作用的还是当前目录 ...

from fabric.api import cd, run, env, put  # 这些是远程的命令
env.user = 'coder352'  # 服务器登录用户名, password 选项不太好用
env.sudo_user = 'root'  # sudo 用户为 root, 这个可以不用定义, 还没发现有什么用
env.hosts = ['172.17.0.2']  # 如果有多个主机, fabric会自动依次部署, docjubuntu -> sudo service ssh start -> 第一个 docker container IP 是 .2
def test_cd():  # cd 是在远程主机上操作的, 远程主机通过 env 来定义
    with cd('/home/coder352'): run('ls')
def test_put(): put('./l1_random_string.py', '/home/coder352')
