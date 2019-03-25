# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 13:21'

"""
从任意长度的可迭代对象中分解元素
*表达式解决
"""

data = ['ACME', 50, 91.1, (2019, 3, 25)]
name, *_, (*_, date) = data
print(name, date)

items = [10, 1, 8, 6, 25, 12]
first, *middle, last = items
print(first, middle, last)