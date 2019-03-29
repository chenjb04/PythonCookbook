# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 21:40'

"""
在文本中处理HTML和XML实体
"""
import html

s = 'Elements are written as "<tag>text</tag>"'
print(html.escape(s))  # Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;
print(html.escape(s, quote=False))  # Elements are written as "&lt;tag&gt;text&lt;/tag&gt;"

s1 = 'spicy &quot;jalape&#241;o&quot.'
print(html.unescape(s1))  # spicy "jalapeño".