# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 15:35'


"""
在字符串的开头或结尾处做文本匹配
str.startswith()和str.endswith()
"""

filename = 'spam.txt'
print(filename.startswith('ftp:'))  # False
print(filename.endswith('.txt'))  # True

filenames = ['makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
# 注意：针对多个选项时，endswith和startswith必须传递元组的形式
print([name for name in filenames if name.endswith(('.c', '.h'))])
