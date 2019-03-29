# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2019/3/29 21:58'

"""
文本分词
"""
import re
from collections import namedtuple

text = 'foo = 23 + 42 * 10'
tokens = [
    ('NAME', 'foo'), ('EQ', '='), ('NUM', 23), ('PLUS', '+'), ('NUM', 42), ('TIMES', '*'), ('NUM', 10)
]

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
# scanner = master_pat.scanner('foo = 42')
# print(scanner.match())  # <_sre.SRE_Match object; span=(0, 3), match='foo'>
# print(_.lastgroup())

Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

"""
Token(type='NAME', value='foo')
Token(type='WS', value=' ')
Token(type='EQ', value='=')
Token(type='WS', value=' ')
Token(type='NUM', value='42')
"""
