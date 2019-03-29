# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 19:29'

"""
编写多行模式的正则表达式
"""
import re

text1 = '/* this is a comment */'
text2 = """/* this is a
          multiline comment */
"""
print(re.findall(r'/\*(.*?)\*/', text1))
# .匹配不到换行符
print(re.findall(r'/\*(.*?)\*/', text2))
# re.DOTALL 可以匹配到换行符
print(re.findall(r'/\*(.*?)\*/', text2, re.DOTALL))
