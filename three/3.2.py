# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/30 15:07'

"""
执行精确的小数计算
"""
from decimal import Decimal
from decimal import localcontext

a = 4.2
b = 2.1
print(a + b)  # 6.300000000000001

c = Decimal('4.2')
d = Decimal('2.3')
print(c + d)  # 6.5

print(c / d)  # 1.826086956521739130434782609

# 控制浮点数的小数位数
with localcontext() as ctx:
    ctx.prec = 3
    print(c / d)  # 1.83