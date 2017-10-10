#!/usr/bin/python3
# coding: utf-8
##################################################################
## clip() Given an interval, values outside the interval are clipped to the interval edges.
# interval of [0, 1] is specified, values smaller than 0 become 0, and values larger than 1 become 1
a = np.arange(10); print(a.clip(2, 4))  # [2 2 2 3 4 4 4 4 4 4]
