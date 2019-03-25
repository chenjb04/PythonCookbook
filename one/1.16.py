# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 18:03'

"""
筛选序列中的元素
"""
from itertools import compress

my_list = [1, 4, -5, 10, -7, 2, -1]
# 筛选大于0的元素
li = [n for n in my_list if n > 0]
print(li)
# 当原始数据大的时候可以使用生成器表达式
li1 = (n for n in my_list if n > 0)
print(list(li1))
# filter()函数筛选,filter()创建了一个迭代器,
li2 = filter(lambda d: int(d), ['1', '2'])
print(list(li2))
# compress 接收可迭代对象和bool序列，根据bool序列中True筛选元素，返回迭代器
l = ['a', 'b', 'c', 'd']
counts = [0, 3, 10, 4]
bool_list = [n > 5 for n in counts]
print(list(compress(l, bool_list)))