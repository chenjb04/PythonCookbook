# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 20:49'

"""
字符串连接和合并
"""

parts = ['hello', 'world', 'very', 'good']
print(' '.join(parts))  # hello world very good

a = 'hello'
b = 'world'
# +操作符做大量的字符串拼接时性能低效
print(a + ' ' + b)  # hello world

# 生成器表达式比较高效
data = ['hello', 'world', 2019]
print(' '.join(str(r) for r in data))  # hello world 2019