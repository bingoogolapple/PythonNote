#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-03-31
# 描述:

# ---------------------------- set -----------------------------

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

# ----------------------------- dict ----------------------------

dict1 = {'key1': 1, "key2": 2, 3: 4, "3": 2, True: 'bool 类型作为 key', (1, 2): '要求 key 为不可变类型，如元组'}
print(type(dict1))  # <class 'dict'>
print(type({}))  # <class 'dict'>
print(dict1)  # {'key1': 1, 'key2': 2, 3: 4, '3': 2, True: 'bool 类型作为 key', (1, 2): '要求 key 为不可变类型，如元组'}
