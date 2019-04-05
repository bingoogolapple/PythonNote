#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-03-31
# 描述:

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
print(len((1, 3, 5)))  # 3
print(max((1, 5, 3)))  # 5
print(min((1, 5, 3)))  # 1
print(sorted((1, 5, 3)))  # [1, 3, 5]
