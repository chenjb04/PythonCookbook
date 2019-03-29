# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 16:27'

"""
查找和替换文本
"""
import re

text = 'yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

date = 'today is 2012/2/27. PyCon starts 2013/3/13.'
print(re.sub(r'(/)', '-', date))
# subn 返回替换完的字符串和替换的次数
print(re.subn(r'(/)', '-', date))


