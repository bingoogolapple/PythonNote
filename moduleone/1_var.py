#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2017/12/15
# 描述:

name1 = 1
print(type(name1))  # <class 'int'>
name2 = name1

print(id(name1))  # 4410292160  id(变量名称) 查看内存地址
print(id(name2))  # 4410292160

name1 = 1.1

print(id(1))  # 4410292160
print(id(1.1))  # 4411642552
print(id(name1))  # 4411642552
print(id(name2))  # 4410292160


print(type(name1))  # <class 'float'>
name1 = '修改后'
print(type(name1))  # <class 'str'> str 为不可变类型
print('Hello World', name1, 'dddd', 'sdfsdfsdfsdf', name2)

