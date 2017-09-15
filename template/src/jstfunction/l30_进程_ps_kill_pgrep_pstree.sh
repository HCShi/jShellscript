#!/bin/bash
##################################################################
## ps faux / ps -elf
sudo ps faux
sudo ps -elf
# 常用命令选项
# a: 显示当前终端下的所有进程信息
# u: 使用以用户为主的格式输出进程信息
# x: 显示当前用户在所有终端下的进程信息
# -e: 显示系统内的所有进程信息
# -l: 使用长格式显示进程信息
# -f: 使用完整的格式显示进程信息
sudo ps -elf | grep nginx  # 显示 nginx 的进程号
##################################################################
## kill 杀死进程
# 以 nginx 为例
sudo ps -elf | grep nginx  # 显示 nginx 的进程号
kill -QUIT pid_of_nginx    # 从容停止 nginx
kill -TERM pid_of_nginx    # 快速停止 nginx
kill -INT pid_of_nginx     # 快速停止 nginx
pkill -9 nginx             # 强制停止
sudo nginx -s stop/quit    # 这样也可以停止 nginx
# 重启进程
sudo nginx -s reload                  # 或者
ps -ef | grep nginx && kill -HUP pid  # 发送信号重启
##################################################################
## pgrep 根据特定条件查询进程 PID 信息
pgrep -l sslocal    # 查看 shadowsocks 的进程号
pgrep -Ul coder352  # 查看用户 coder352 的进程信息
pgrep -t sslocal    # 根据进程所在的终端进行查找
##################################################################
## pstree 以树型结构显示各进程间的关系
pstree -pua coder352  # 列出 coder352 用户的所有进程树
# -p: 列出进程的PID号
# -u: 列出进程对应的用户名
# -a: 列出进程对应的完整命令
