#!/bin/bash
##################################################################
## 用户
w  # 查看当前活动用户
whoami  # 查看当前用户
who&w   # 查看当前有几个终端 +1 和各个终端的命令

id coder352              # UID, GID; 查看指定用户信息
last                     # 查看用户登录日志
cut -d: -f1 /etc/passwd  # 查看系统所有用户
cut -d: -f1 /etc/group   # 查看系统所有组

crontab -l          # 查看当前用户的计划任务
finger -s coder352  # 用户相关信息, 登录时间

users   # 有哪些 user, 和 /home 下类似
groups  # 有哪些 groups
