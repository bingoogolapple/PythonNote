#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-05-22
# 描述:

import time
from collections import Iterable
from collections import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个可以迭代的对象，即可以使用 for，那么必须实现 __iter__ 方法"""
        return self  # 调用 iter(xxxobj) 的时候，只要 __iter__ 方法返回一个 迭代器即可，至于是自己还是别的对象都可以的, 但是要保证是一个迭代器(即实现了 __iter__  __next__方法)

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


def test_iter():
    print('----- test_iter -----')
    classmate = Classmate()
    classmate.add("老王")
    classmate.add("王二")
    classmate.add("张三")

    print("判断是否是可以迭代的对象:", isinstance(classmate, Iterable))
    classmate_iterator = iter(classmate)
    print("判断是否是迭代器:", isinstance(classmate_iterator, Iterator))
    print(next(classmate_iterator))

    for name in classmate:
        print(name)
        time.sleep(1)


# test_iter()


class Fibonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a

            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1

            return ret
        else:
            raise StopIteration


def test_fibonacci_iter():
    print('----- test_fibonacci_iter -----')
    fibo = Fibonacci(10)
    for num in fibo:
        print(num)


# test_fibonacci_iter()


def create_num(all_num):
    print("----1---")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("----2---")
        ret = yield a  # 如果一个函数中有 yield 语句，那么这个就不再是函数，而是一个生成器的模板
        print("----3--- %s" % ret)
        a, b = b, a + b
        current_num += 1
        print("----4---")


def test_yield():
    # 如果在调用 create_num 的时候，发现这个函数中有 yield，那么此时不是调用函数，而是创建一个生成器对象
    obj = create_num(4)

    ret = next(obj)
    print("obj:", ret)

    ret = next(obj)
    print("obj:", ret)

    ret = next(obj)
    print("obj:", ret)

    for num in obj:
        print(num)

    obj2 = create_num(10)
    while True:
        try:
            ret = next(obj2)
            print(ret)
        except Exception as ret:
            print(type(ret))  # <class 'StopIteration'>
            print(ret.value)
            break


# test_yield()


# 通过 send 来启动生成器
def test_send():
    obj = create_num(10)

    # ret = obj.send(None)  # send一般不会放到第一次启动生成器，如果非要这样做，那么传递None
    ret = next(obj)
    print(ret)

    # send 里面的数据会传递给 create_num 中的 ret 当做 yield a 的结果，然后 ret 保存这个结果
    # send 的结果是下一次调用 yield 时，yield 后面的值
    ret = obj.send("第一次 send")
    print(ret)
    ret = obj.send("第二次 send")
    print(ret)


test_send()
