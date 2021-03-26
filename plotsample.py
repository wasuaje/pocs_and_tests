# -*- coding: utf-8 -*-
"""
Demo of a simple plot with a custom dashed line.

A Line object's ``set_dashes`` method allows you to specify dashes with
a series of on/off lengths (in points).
"""
import numpy as np
import matplotlib.pyplot as plt

a=[1,2,3,4]
b=[3,6,9,12]
data=[a,b]
#x = np.line(0, 10)
line, = plt.plot(a,b, '-', linewidth=1)

#dashes = [10, 5, 100, 5] # 10 points on, 5 off, 100 on, 5 off
#line.set_dashes(dashes)

plt.show()