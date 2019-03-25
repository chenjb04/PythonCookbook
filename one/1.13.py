# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 17:10'

"""
通过公共键对字典列表进行排序
"""
from operator import itemgetter

rows = [
    {'name': "a", "id": 1001, 'lname': 'z'},
    {'name': "c", "id": 1005, 'lname': 'f'},
    {'name': "d", "id": 1002, 'lname': 'n'},
    {'name': "b", "id": 1006, 'lname': 'q'},
]

# lambda也可以实现，但是itemgetter性能更高
rows_by_name = sorted(rows, key=itemgetter('name'))
rows_by_id = sorted(rows, key=itemgetter('id'))
print(rows_by_name)
print(rows_by_id)

