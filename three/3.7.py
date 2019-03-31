# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/31 18:15'


"""
处理无穷大和NaN
"""
import math

# inf表示无穷大
a = float('inf')
b = float('-inf')
c = float('nan')

print(a)  # inf
print(b)  # -inf
print(c)  # nan

# 检测是否出现了这些值
print(math.isnan(c))  # True
print(math.isinf(b))  # True

# 无穷大值会传播
print(a + 45)  # inf
print(a * 10)  # inf
print(10 / a)  # 0.0
# 特定的操作产生nan结果
print(a / a)  # nan
print(a + b)  # nan

# nan会通过所有的操作进行传播，不会引发异常
print(c + 12)  # nan
print(c * 10)  # nan
print(c / 2)  # nan
print(10 / c)  # nan