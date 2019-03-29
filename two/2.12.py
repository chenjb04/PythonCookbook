# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 20:20'

"""
文本过滤和清洗
"""

s = 'pythoñ\fis\tawesome\r\n'
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None,
}
a = s.translate(remap)
print(a)  # pythoñ is awesome