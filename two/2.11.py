# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 20:09'

"""
从字符串中去掉不需要的字符
"""

s = ' hello world \n'
# 去掉两边的空白字符
print(s.strip())
# 去掉左边的空白字符
print(s.lstrip())
# 去掉右边的空白字符
print(s.rstrip())

t = '---hello world ===='
print(t.lstrip('-'))
print(t.rstrip('='))


