# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 14:11'

"""
实现优先级队列
heapq模块实现
"""

import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """
        :param item:
        :param priority: 取负值使队列优先级从高到低排序
        :return:
        """
        # index使相同优先级的元素以适当的顺序排列，元组形式传递可以对优先级高级进行排序，因为元组索引index不同
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


if __name__ == '__main__':
    q = PriorityQueue()
    q.push("a", 1)
    q.push("b", 5)
    q.push("c", 3)
    q.push("d", 1)
    print(q.pop())
    print(q.pop())
    # 当优先级一致时，和插入队列顺序一致
    print(q.pop())
