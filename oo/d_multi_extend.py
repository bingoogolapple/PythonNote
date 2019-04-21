#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-21
# 描述:Python 支持多重继承


class A:

    def __init__(self):
        self.name = 'A'

    def test(self):
        print("A --- test 方法")

    def demo(self):
        print("A --- demo 方法")


class B:
    def __init__(self):
        self.name = 'B'

    def test(self):
        print("B --- test 方法")

    def demo(self):
        print("B --- demo 方法")


class C(A, B):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass


class D(B, A):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass


# __mro__ 确定 C 类对象调用方法的顺序，从左往右找第一个存在的
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# 创建子类对象
c = C()
c.test()  # A --- test 方法
c.demo()  # A --- demo 方法
print(c.name)  # A

# __mro__ 确定 D 类对象调用方法的顺序，从左往右找第一个存在的
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# 创建子类对象
d = D()
d.test()  # B --- test 方法
d.demo()  # B --- demo 方法
print(d.name)  # B
