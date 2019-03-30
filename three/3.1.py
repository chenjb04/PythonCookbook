# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/30 11:53'

"""
对数值进行取整
"""

print(round(1.23, 1))  # 1.2
print(round(1.235, 2))  # 1.24
print(round(1.20, 2))  # 1.2
print(round(1.5, 0))  # 2.0

print(round(1627731, -1))  # 1627730
print(round(1627731, -2))  # 1627700
print(round(1627731, -3))  # 1628000