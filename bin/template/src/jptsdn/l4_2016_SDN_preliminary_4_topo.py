#!/usr/bin/python
# coding: utf-8
from mininet.topo import Topo
class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        switchs = [self.addHost('S%d' % i) for i in range(1, 5)]
        host1 = self.addHost('H1', ip='10.0.0.1')
        host2 = self.addHost('H2', ip='10.0.0.2')
        host3 = self.addHost('D1', ip='10.0.0.3')
        host4 = self.addHost('D2', ip='10.0.0.4')
        self.addLink(host1, switchs[0])
        self.addLink(host2, switchs[0])
        self.addLink(host3, switchs[3])
        self.addLink(host4, switchs[3])
        self.addLink(switchs[0], switchs[1])
        self.addLink(switchs[0], switchs[2])
        self.addLink(switchs[3], switchs[1])
        self.addLink(switchs[3], switchs[2])
topos={'mytopo': (lambda: MyTopo())}
