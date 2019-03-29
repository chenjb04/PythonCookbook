# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 19:47'

"""
用正则表达式处理Unicode字符串
"""
import re

s1 = '123'
s2 = '\u0031'
print(re.findall(r'\d+', s1))
# re默认对Unicode字符类型有了基本认识
print(re.findall(r'\d+', s2))



