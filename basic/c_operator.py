#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-01
# 描述:

a = 1 * 1
b = 1 * 1.0
c = 4 / 3  # 一个斜杠的结果是浮点数
d = 4 // 3  # 两个斜杠是整除，结果是整数
e = 5 % 2  # 取余
f = 2 ** 2  # 2 的平方
g = 2 ** 4  # 2 的 4 次方
print('a', a, type(a))  # <class 'int'>
print('b', b, type(b))  # 1.0 <class 'float'>
print('c', c, type(c))  # 1.3333333333333333 <class 'float'>
print('d', d, type(d))  # 1 <class 'int'>
print('e', e, type(e))  # 1 <class 'int'>
print('f', f, type(f))  # 4 <class 'int'>
print('g', g, type(g))  # 16 <class 'int'>

print(bin(17))  # 0b10001
print(oct(17))  # 0o21
print(int(0b10001))  # 17
print(hex(17))  # 0x11


print(int(True))
print(int(False))
