#!/usr/bin/python
# coding: utf-8
from mininet.topo import Topo
class MyTopo(Topo):
    "Simple topology example."
    def __init__(self):
        "Create custom topo."
        Topo.__init__(self)  # Initialize topology, 将当前对象注册到 Topo 中
        # Add hosts and switches
        leftHost1 = self.addHost('H1')
        leftHost2 = self.addHost('H2')
        rightHost1 = self.addHost('H3')
        rightHost2 = self.addHost('H4')
        leftSwitch = self.addSwitch('s1')
        rightSwitch = self.addSwitch('s2')
        # Add links
        self.addLink(leftHost1, leftSwitch)
        self.addLink(leftHost2, leftSwitch)
        self.addLink(leftSwitch, rightSwitch)
        self.addLink(rightSwitch, rightHost1)
        self.addLink(rightSwitch, rightHost2)
topos = {'mytopo': (lambda: MyTopo())}
