#!/usr/bin/python3
# coding: utf-8
from mininet.topo import Topo  # 这个文件不一定能运行...
class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        switchs = [self.addHost('S%d' % i) for i in range(1, 5)]  # 批量添加 switch
        host1 = self.addHost('H1')  # 这里就不适合用循环, 因为名字不一样, 但可以读配置
        host2 = self.addHost('H2')
        host3 = self.addHost('D1')
        host4 = self.addHost('D2')
        self.addLink(host1, switchs[0])  # 这里也不适合用循环, 因为不规律, 但是可以读取配置
        self.addLink(host2, switchs[0])
        self.addLink(host3, switchs[3])
        self.addLink(host4, switchs[3])
        self.addLink(switchs[0], switchs[1])  # 这里也不适合用循环, 因为不规律, 但可以读配置
        self.addLink(switchs[0], switchs[2])
        self.addLink(switchs[3], switchs[1])
        self.addLink(switchs[3], switchs[2])
topos={'mytopo': (lambda: MyTopo())}  # 最后一定要用 mytopo, 因为 sudomn 里面用的是 mytopo
