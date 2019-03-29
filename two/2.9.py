# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 19:38'

"""
将unicode文本统一表示为规范形式
"""
import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)  # Spicy Jalapeño
print(s2)  # Spicy Jalapeño
print(s1 == s2)  # False
print(len(s1))  # 14
print(len(s2))  # 15

# 第一个参数表示字符串以哪种方式规范表示
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1)
print(t2)
print(t1 == t2)  # True