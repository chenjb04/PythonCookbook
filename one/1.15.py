# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 17:24'

"""
根据字段将记录分组
"""
from operator import itemgetter
from itertools import groupby

rows = [
    {'name': 'a', 'date': '2019/3/25'},
    {'name': 'b', 'date': '2019/2/26'},
    {'name': 'c', 'date': '2019/8/27'},
    {'name': 'd', 'date': '2019/3/25'},
    {'name': 'e', 'date': '2019/2/26'},
    {'name': 'f', 'date': '2019/8/27'},
]
# 先进行排序在分组
rows.sort(key=itemgetter('date'))

# groupby()创建了一个迭代器，每次迭代都会返回一个值和一个子迭代器，子迭代器产生包含该值的项
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(" ", i)