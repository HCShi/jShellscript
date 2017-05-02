#!/usr/bin/python
# coding: utf-8
from mininet.topo import Topo

class Lab3Topo(Topo):
    """lab 3 topo"""
    def __init__(self):
        """ create custom topo"""
        Topo.__init__(self)
        # add hosts
        H1 = self.addHost('H1')
        H2 = self.addHost('H2')
        H3 = self.addHost('H3')
        H4 = self.addHost('H4')
        Web = self.addHost('Web')
        # add switchs
        S1 = self.addSwitch("S1")
        S2 = self.addSwitch("S2")
        # add links
        self.addLink(H1, S1)
        self.addLink(H2, S1)
        self.addLink(H3, S1)
        self.addLink(H4, S1)
        self.addLink(S1, S2)
        self.addLink(S2, Web)
topos = {"mytopo": (lambda : Lab3Topo())}
