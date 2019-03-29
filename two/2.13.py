# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 20:36'

"""
对齐文本字符串
"""

s = "hello world"
print(s.ljust(20, '-'))  # hello world---------
print(s.rjust(20, '='))  # =========hello world
print(s.center(20, '*'))  # ****hello world*****

print(format(s, '>20'))
print(format(s, '<20'))
print(format(s, '^20'))

print(format(s, '->20s'))  # ---------hello world
print(format(s, '=<20s'))  # hello world=========
print(format(s, '*^20s'))  # ****hello world*****

x = 1.2345
print(format(x, '=>10'))  # ====1.2345
print(format(x, '-^10.2f'))  # ---1.23---