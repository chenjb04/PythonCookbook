# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 15:26'

"""
在两个字典中寻找共同点
"""

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 18,
    'x': 11,
    'y': 2
}

# a和b相同的键
print(a.keys() & b.keys())
# b中没有a的键
print(a.keys() - b.keys())
# a和b相同的键值
print(a.items() & b.items())
# 字典的keys()方法支持集合操作 items()方法支持类似集合的操作
