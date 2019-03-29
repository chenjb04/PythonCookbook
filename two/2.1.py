# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 15:31'

"""
对任意多的分隔符拆分字符串
re.split()
"""

import re

line = 'absd fjkd; afed, fjrel,asdf,    foo'
ret = re.split(r'[;,\s]\s*', line)
print(ret)