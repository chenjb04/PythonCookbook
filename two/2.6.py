# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 18:06'

"""
以不区分大小写的方式对文本做查找和替换
"""
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall(r'python', text, flags=re.IGNORECASE))
print(re.sub(r'python', 'snake', text, flags=re.IGNORECASE))


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


print(re.sub(r'python', matchcase('snake'), text, flags=re.IGNORECASE))