#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-23
# 描述:


class SingletonA(object):
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 1. 判断是否执行过初始化动作
        if SingletonA.init_flag:
            return

        # 2. 如果没有执行过，在执行初始化动作
        print("初始化单例对象")

        # 3. 修改类属性的标记
        SingletonA.init_flag = True


# 创建多个对象
singletonA1 = SingletonA()
print(singletonA1)

singletonA2 = SingletonA()
print(singletonA2)
