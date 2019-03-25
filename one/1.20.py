# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 22:52'

"""
将多个映射合并为单个映射
"""
from collections import ChainMap

a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
# 对于重复的键，会采用第一个映射中对应的值
print(c['z'])