#!/usr/bin/python3
# coding: utf-8
from pyquery import PyQuery
print(PyQuery('<div><span>toto</span><span>tata</span></div>').text())
print(PyQuery('<div><span class="hello">toto</span><span>tata</span></div>').text())
