# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/30 17:57'

"""
复数运算
"""
import cmath

a = complex(2, 4)
b = 3 - 5j
print(a)  # (2+4j)
print(b)  # (3-5j)

print(a.real)  # 2.0
print(a.imag)  # 4.0
print(a.conjugate())  # (2-4j)

print(a + b)  # (5-1j)
print(a * b)  # (26+2j)
print(a / b)  # (-0.4117647058823529+0.6470588235294118j)
print(a - b)  # (-1+9j)

print(cmath.sin(a))  # (24.83130584894638-11.356612711218174j)
print(cmath.cos(a))  # (-11.36423470640106-24.814651485634187j)
print(cmath.exp(a))  # (-4.829809383269385-5.5920560936409816j)

# 标准数学函数中不会产生复数值，如果希望产生复数值，需要使用cmath
print(cmath.sqrt(-1))  # 1j