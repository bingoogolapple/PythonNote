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

print(type((1, 2, 3)))  # <class 'tuple'>
print(type((1)))  # <class 'int'>
print(type((1,)))  # <class 'tuple'> 元组里只有一个元素的话加个逗号，否则会被视为 int
print(type(()))  # <class 'tuple'>

print(type([1, 2, 3]))  # <class 'list'>
print(type([1]))  # <class 'list'>
print(type([]))  # <class 'list'>

print(3 in [1, 3, 5])  # True
print(4 not in [1, 3, 5])  # False
print(len([1, 3, 5]))  # 3
print(len([1, 3, ]))  # 2
print(len("abcde"))  # 5
print(len((1, 3, 5)))  # 3
print(max("aAbBeEcCdD"))  # e
print(min("aAbBeEcCdD"))  # A
print(max((1, 5, 3)))  # 5
print(min((1, 5, 3)))  # 1
print(sorted((1, 5, 3)))  # [1, 3, 5]
print(sorted("aAbBeEcCdD"))  # ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
print(ord("A"))  # 65  获取 ASCII 码
print(ord("a"))  # 97
print(ord("1"))  # 49

# ---------------------------------------------------------

set1 = {1, 3, 7, 5, 3, 7}
print(type(set1))  # <class 'set'>
print(type(set()))  # <class 'set'> 定义空的集合用 set()
print(type({}))  # <class 'dict'> 空的字典
print(set1)  # {1, 3, 5, 7} 不重复
print(len(set1))  # 4 不重复
print(7 in set1)  # True
print(7 not in set1)  # False

set2 = {1, 2, 3, 4, 5, 6}
set3 = {3, 4, 7}
print(set2 - set3)  # {1, 2, 5, 6} 求两个集合差集
print(set2 & set3)  # {3, 4} 求两个集合交集
print(set2 | set3)  # {1, 2, 3, 4, 5, 6, 7} 求两个集合并集

# ---------------------------------------------------------

dict1 = {'key1': 1, "key2": 2, 3: 4, "3": 2, True: 'bool 类型作为 key', (1, 2): '要求 key 为不可变类型，如元组'}
print(type(dict1))  # <class 'dict'>
print(type({}))  # <class 'dict'>
print(dict1)  # {'key1': 1, 'key2': 2, 3: 4, '3': 2, True: 'bool 类型作为 key', (1, 2): '要求 key 为不可变类型，如元组'}
