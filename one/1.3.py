# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 13:39'

"""
保存最后N个元素
使用deque解决
"""
from collections import deque


def search(lines, pattern, history=5):
    """
    匹配文本， 当有匹配时输出当前匹配行和检查过的N行文本
    :param lines: 文本
    :param pattern: 匹配的文本
    :param history: 指定队列的固定长度大小
    :return:
    """
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('1_3.txt', 'r', encoding='utf-8') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end="")
            print(line, end="")
            print('-'*20)

    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    q.append(5)
    print(q)
    q.popleft()
    print(q)