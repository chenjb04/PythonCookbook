# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/30 15:24'

"""
二进制 八进制 十六进制
"""

x = 1234
# 十进制转二进制
print(bin(x))  # 0b10011010010
print(format(x, 'b'))  # 10011010010
# 十进制转八进制
print(oct(x))  # 0o2322
print(format(x, 'o'))  # 2322
# 十进制转十六进制
print(hex(x))  # 0x4d2
print(format(x, 'x'))  # 4d2

# 字符串形式整数转换为不同的进制
print(int('0x4d2', 16))  # 1234
print(int('2322', 8))  # 1234

# 注意八进制数指定要加上0o前缀