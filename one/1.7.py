# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 15:13'

"""
实现有序字典
collections的OrderDict类
"""

from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(dict(d))
# OrderedDict大小为dict的两倍，由于额外创建的链表导致
