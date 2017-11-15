#!/usr/bin/python3
# coding: utf-8
import time
##################################################################
## sleep()
time.sleep(1)  # 程序暂停
##################################################################
## clock() On Unix, return the current processor time as a floating point number expressed in seconds.
start = time.clock()
print("耗时 =", time.clock() - start)
##################################################################
## time() Return the time in seconds since the epoch as a floating point number
then = time.time()
now = time.time()
print(now - then)
##################################################################
## datetime
from datetime import datetime
print(datetime.now())  # 当前时间
print(datetime(2015, 4, 19, 12, 20))  # 2015-04-19 12:20:00, 年月日时分
print(datetime(2015, 4, 19, 12, 20).timestamp())  # 1429417200.0, 时间戳, 单位 毫秒(ms)
print(datetime.fromtimestamp(datetime(2015, 4, 19, 12, 20).timestamp()))  # 时间戳 转化为 时间
print(datetime.utcfromtimestamp(datetime(2015, 4, 19, 12, 20).timestamp()))  # 格林威治时区
# datetime 有时区, timestamp 没有时区, 所以两者实在系统设定时区进行转换

# str <-> date
print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))  # 2015-06-01 18:19:59
print(datetime(2015, 4, 19, 12, 20).strftime('%a, %b %d %H:%M'))  # Sun, Apr 19 12:20

from datetime import timedelta  # 时间加减
print(datetime.now() + timedelta(days=1, hours=10))
