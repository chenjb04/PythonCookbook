# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 13:10'

"""
将一个包含N个元素的元组和序列拆分为N个单独的变量
可迭代对象都可通过赋值操作分解单独的变量
"""
t = (4, 5)
x, y = t
print("x=", x, "y=", y)

data = ['ACME', 50, 91.1, (2019, 3, 25)]
name, _, price, date = data
print(name, price, date)