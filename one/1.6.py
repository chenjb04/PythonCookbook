# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 15:07'

"""
在字典将键映射到多个值上
collection的defaultdict类
"""

from collections import defaultdict


d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
d['a'].append(4)
print(dict(d))

dic = {}
dic.setdefault('a', []).append(1)
dic.setdefault('a', []).append(2)
dic.setdefault('b', []).append(3)
dic.setdefault('a', []).append(4)
print(dic)
