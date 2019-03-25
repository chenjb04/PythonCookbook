# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 18:16'

"""
从字典中提取子集
字典推倒式
"""

prices = {
    'a': 65,
    'b': 100,
    'c': 15,
    'd': 20,
    'e': 13,
}

# 提取值大于50的元素
p1 = {key: value for key, value in prices.items() if value > 50}
print(p1)