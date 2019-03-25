# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 22:17'

"""
同时对数据做转换和换算
生成器方式
"""

nums = [1, 2, 3, 4, 5]
s = sum(i * i for i in nums)
print(s)

info = [
    {'name': "a", 'price': 10},
    {'name': "b", 'price': 15},
    {'name': "c", 'price': 1},
    {'name': "d", 'price': 2},
]

min_price = min(s['price'] for s in info)
print(min_price)