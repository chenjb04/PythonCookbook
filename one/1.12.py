# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 16:42'

"""
找出序列中出现次数最多的元素
"""

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'eyes', 'eyes', 'look', 'the', 'the', 'the', 'eyes'
]

word_count = Counter(words)
# Counter是一个字典，还可以做数学运算
print(word_count)
# 统计出现次数最多的两个元素
print(word_count.most_common(2))

morewords = ['hello', 'eyes', 'the', 'world', 'the']
# 增加计数
word_count.update(morewords)
print(word_count)

# 数学运算
a = Counter(words)
b = Counter(morewords)
c = a + b
print(c)
d = a - b
print(d)