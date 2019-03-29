# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 21:27'


"""
以固定的列数重新格式化文本
"""
import textwrap

s = "hello world1, hello world2\
    hello world3,\
    hello world4"
print(textwrap.fill(s, 30))
"""
hello world1, hello world2
hello world3,    hello world4
"""
print(textwrap.fill(s, 70))
"""
hello world1, hello world2    hello world3,    hello world4
"""
print(textwrap.fill(s, 30, initial_indent=' '))
"""
 hello world1, hello world2
hello world3,    hello world4
"""
print(textwrap.fill(s, 30, subsequent_indent=' '))
"""
hello world1, hello world2
 hello world3,    hello world4
"""