# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 22:35'

"""
在字节串上执行文本操作
"""

data = b'hello world'
print(data[0:5])  # b'hello'
print(data.startswith(b'hello'))  # True
print(data.replace(b'hello', b'this is'))  # b'this is world'
print(data[0])  # 104
print(data[1])  # 101