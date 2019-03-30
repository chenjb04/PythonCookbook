# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/30 15:18'

"""
对数值做格式化输出
"""

x = 1234.56789
print(format(x, '0.2f'))  # 1234.57
print(format(x, '=>10.1f'))  # ====1234.6
print(format(x, '-^10.1f'))  # --1234.6--
print(format(x, ','))  # 1,234.56789
print(format(x, '0,.1f'))  # 1,234.6

print(format(x, '0.2e'))  # 1.23e+03