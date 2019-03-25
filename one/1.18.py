# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 21:33'

"""
将名称映射到序列的元素中
命名元组
"""

from collections import namedtuple

Subscriber = namedtuple("Subscriber", ['address', 'joined'])
sub = Subscriber('123@123.com', '2019/3/25')
print(sub)
print(sub.address)
print(sub.joined)

# namedtuple为不可变对象，如果修改需要_replace()方法
Stock = namedtuple('Stock', ['name', 'price', 'date'])
s = Stock('a', 12.5, '2019/3/25')
s = s._replace(name='b')
print(s)