# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 16:00'

"""
对切片进行命名
"""

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a])
print(a.start)
print(a.stop)
print(a.step)
# indices返回一个(start, stop,step)元组，避免索引出界异常
print(a.indices(len("hello")))