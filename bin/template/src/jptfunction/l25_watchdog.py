#!/usr/bin/python3
# coding: utf-8
# sudo apt install python3-watchdog  # 自带一些小工具, https://github.com/gorakhargosh/watchdog
import sys, time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
path = sys.argv[1] if len(sys.argv) > 1 else '.'
event_handler = LoggingEventHandler()  # 只要自己写一个 class 继承 LoggingEventHandler, 然后重写函数就行了
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()
try:
    while True: time.sleep(1)
except KeyboardInterrupt: observer.stop()
observer.join()
