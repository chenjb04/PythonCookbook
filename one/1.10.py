# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 15:38'

"""
消除序列重复项并且保持顺序不变
"""


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    li = [1, 1, 2, 4, 5, 2, 4, 6]
    print(list(dedupe(li)))

    a = [
        {"x": 1, "y": 2},
        {"x": 1, "y": 3},
        {"x": 2, "y": 4},
        {"x": 1, "y": 2},
    ]
    print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
    print(list(dedupe(a, key=lambda d: d['x'])))
