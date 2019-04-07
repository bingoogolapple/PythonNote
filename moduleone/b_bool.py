#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-01
# 描述:

# 只有 True 和 False。其他类型值非 0 或长度非 0 即真，否则为 False

a = True
print(a)  # True
a = False
print(a)  # False
print(type(a))  # <class 'bool'>

print(bool(1))  # True
print(bool(0))  # False
print(bool(-1))  # True
print(bool(' '))  # True
print(bool(''))  # False
print(bool('a'))  # True
print(bool([]))  # False
print(bool([3]))  # True
print([1] or [])  # [1]
print([] or [1])  # [1]
print([1] and [])  # []
print([] and [1])  # []
print(0 and 2)  # 0
print(2 and 0)  # 0
print(1 and 2)  # 2
print(2 and 1)  # 1

b = 1.1
print(1 is 1)  # True。is 对比内存地址是否相等
print(b is 1.1)  # True

c = {1, 2, 3}
d = {2, 1, 3}
print(c == d)  # True
print(c is d)  # False

e = (1, 2, 3)
f = (1, 2, 3)
g = (2, 1, 3)
print(e == f)  # True
print(e is f)  # False

print(e == g)  # False
print(e is g)  # False

h = 'Hello'
print(type(h) == str)  # True
print(isinstance(h, str))  # True
print(isinstance(h, int))  # True
print(isinstance(h, (int, float, str)))  # True
print(isinstance(h, (int, float)))  # False

i = 1
j = 2
k = 3
print(i or j and k)  # 1。and 优先级高于 or
print(i or (j and k))  # 1
print((i or j) and k)  # 3
