# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 19:25'


"""
定义实现最短匹配的正则表达式
"""
import re

text = 'computer "no." phone "yes."'
print(re.findall(r'\"(.*)\"', text))
# ? 表示非贪婪匹配，尽可能少的匹配
print(re.findall(r'\"(.*?)\"', text))
