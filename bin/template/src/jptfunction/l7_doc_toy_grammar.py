#!/usr/bin/python
# coding: utf-8
def hello():
    """hello"""
    pass
print hello.__doc__
print 'hello {}, {}'.format('jrp', 'beijing')  # hello jrp, beijing
print 'hello %s, %s' % ('jrp', 'beijing')      # hello jrp, beijing
