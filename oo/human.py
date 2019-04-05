#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-05
# 描述:

test_global = '我是全局变量'


class Human:
    # 类变量
    sum = 0
    name = 'bingoogolapple'

    # 构造函数，也能主动调用，返回值为 None
    # 第一个参数可以不叫 self，但 Python 官方建议命名为 self
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age

        Human.sum += 1
        # 执行了 Human 的 __init__ 方法 1 bingoogolapple bingoogolapple 我是全局变量
        print('执行了 Human 的 __init__ 方法', Human.sum, Human.name, self.__class__.name, test_global)

    # 定义成员方法
    def test1(self):
        print('父类 test1', self.name, self.age, test_global)
        self.__test4()

    # 定义类方法
    @classmethod
    def test2(cls):
        print('调用了类方法', cls.name)

    # 定义静态方法
    @staticmethod
    def test3():
        print('调用了静态方法', Human.name, Human.sum)

    # 定义私有方法，两个下划线 __ 开头的方法为私有方法
    def __test4(self):
        print('访问了私有方法', self.name)
