# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 20:58'

"""
给字符串中的变量名做插值处理
"""
import sys

s = '{name} has {n} messages'
print(s.format(name='Guido', n=30))  # Guido has 30 messages

name = 'Guido'
n = 30
# vars返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()。
print(s.format_map(vars()))  # Guido has 30 messages


class SafeSub(dict):
    """
    定义__missing__方法类处理缺少值情况
    """
    def __missing__(self, key):
        return '{' + key + '}'


def sub(text: str):
    return text.format_map(SafeSub(sys._getframe(1).f_locals))


# 确定n未定义
del n
print(s.format_map(SafeSub(vars())))  # Guido has {n} messages

n = 30
print(sub('hello {name}'))  # hello Guido
print(sub('{n} messages'))  # 30 messages
print(sub('{color} yellow'))  # {color} yellow