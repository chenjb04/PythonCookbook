# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/30 17:50'

"""
从字节串中打包和解包最大整数
"""

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

print(len(data))  # 16
print(int.from_bytes(data, 'little'))  # 69120565665751139577663547927094891008
print(int.from_bytes(data, 'big'))  # 94522842520747284487117727783387188

x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))  # b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(x.to_bytes(16, 'little'))  # b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'
