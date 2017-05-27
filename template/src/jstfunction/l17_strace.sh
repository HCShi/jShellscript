#!/bin/bash
# 修改了 /etc/hosts 以后, sudo 变得非常慢, 于是查到了这个命令
# Is one of the files/directories it needs to read on a networked mount, or is it somehow triggering reading from a slow usb device?
sudo strace -r -o trace.log sudo echo hi
# Each line will start with the time taken since entering the previous syscall
