# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/25 17:15'

"""
对不原生支持比较操作的对象排序
"""
from operator import attrgetter


class User(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


if __name__ == '__main__':
    users = [User(33), User(6), User(99), User(42)]
    print(sorted(users, key=lambda d: d.user_id))
    # 使用attrgetter 比lambda性能高，还可接收多个字段
    print(sorted(users, key=attrgetter('user_id')))
