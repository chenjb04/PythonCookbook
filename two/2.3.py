# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 15:46'

"""
利用shell通配符做字符串匹配
fnmatch, fnmatchcase
"""

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))  # True
print(fnmatch('dat45.csv', 'dat[0-9]*.csv'))  # True
# fnmatchcase 区别大小写，而fnmatch根据操作系统不同而是否区分大小写
print(fnmatchcase('dat45.csv', 'dat[0-9]*.CSV'))  # False

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W CRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])




