#!/usr/bin/python
# coding: utf-8
import socket
sock = socket.socket()
sock.connect(('127.0.0.1', 1234))
print sock.recv(1024)  # 必须指定缓冲大小
