#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-03-31
# 描述:

# str 为不可变类型
print('abcdef'[3])  # d
print('abcdef'[3:])  # def
print('abcdef'[:3])  # abc
print('abcdef'[1:-2])  # bcd
print('abcdef'[-1:])  # f
print('abcdef'[:-1])  # abcde

print("abc\ndef\nghi")
print(r"abc\ndef\nghi")
print(R"abc\ndef\nghi")

print('''abc
def
ghi''')

print('''
abc
def
ghi
''')

print("""
abc
def
ghi
""")

print(len("abcde"))  # 5
print(max("aAbBeEcCdD"))  # e
print(min("aAbBeEcCdD"))  # A
print(sorted("aAbBeEcCdD"))  # ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
print(ord("A"))  # 65  获取 ASCII 码
print(ord("a"))  # 97
print(ord("1"))  # 49
