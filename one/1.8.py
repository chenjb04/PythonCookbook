# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 15:19'

"""
与字典有关的计算问题
zip()可以解决
"""

prices = {
    "a": 10.2,
    'b': 56.1,
    "c": 20.5,
    'd': 17.5
}

# 最大值
print(max(zip(prices.values(), prices.keys())))
# 最小值
print(min(zip(prices.values(), prices.keys())))
# 排序
print(sorted(zip(prices.values(), prices.keys())))
# 注意 zip()创建了一个迭代器，它的内容只能被消费一次
