# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 13:51'

"""
找到最大或者最小的N个元素
heapq模块解决
"""

import heapq

nums = [-2, 15, 89, 26, 1, 55, 32, -78, 5, 10]
print(heapq.nsmallest(4, nums))
print(heapq.nlargest(4, nums))

portfolio = [
    {"name": "IBM", "price": 98.2},
    {"name": "A", "price": 198.2},
    {"name": "B", "price": 90.89},
    {"name": "C", "price": 20.7},
]

print(heapq.nsmallest(2, portfolio, key=lambda s: s['price']))
print(heapq.nlargest(2, portfolio, key=lambda s: s['price']))