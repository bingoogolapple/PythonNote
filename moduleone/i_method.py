#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-05
# 描述:


def test1():
    print('test1')


def test2(p1, p2):
    """方法描述

    :param p1:参数1
    :param p2:参数2
    :return:返回值为None
    """
    print('p1 = ', p1, 'p2 = ', p2)
    p1 + p2


# 仅仅位置参数
def test3(p1, p2):
    """方法描述

    :param p1:参数1
    :param p2:参数2
    :return:参数1和参数2的和
    """
    print('p1 = ', p1, 'p2 = ', p2)
    return p1 + p2


# 通过 tuple 返回多个值
def test4(p1, p2):
    print('p1 = ', p1, 'p2 = ', p2)
    return p1 + 1, p2 + 1


# 加上了默认参数
def test5(p1, p2=3):
    print('p1 = ', p1, 'p2 = ', p2)
    return p1 + p2


# *变量名 定义可变长参数，其实是个 tuple。必须放到最后
def test6(p1, p2, *istuple):
    print('p1 = ', p1, 'p2 = ', p2, 'istuple = ', istuple)
    result = p1 + p2
    for num in istuple:
        result += num
    return result


# **变量名 定义关键字参数，其实是个 dict。必须放到最后
def test7(p1, p2, **isdict):
    print('p1 = ', p1, 'p2 = ', p2, 'isdict = ', isdict)


# 可选参数和命名参数同时存在时，命名参数必须放到最后
def test8(p1, p2, *istuple, **isdict):
    print('p1 = ', p1, 'p2 = ', p2, 'istuple = ', istuple, 'isdict = ', isdict)


print('----- 调用要放到定义之后，默认返回为 None -----')
print(test1)  # <function test1 at 0x101dfbe18>
print(type(test1))  # <class 'function'>
print(test1())  # None

print('----- 不写 return 时返回 None -----')
print(test2)  # <function test2 at 0x107004158>
print(type(test2))  # <class 'function'>
print(test2(1, 2))  # None

print('----- 必须写 return 才会返回结果 -----')
print(test3(1, 2))  # 3

print('----- 指定名称来调换参数顺序 -----')
print(test3(p2=1, p1=2))  # 3

print('----- 通过 tuple 返回多个值 -----')
test4Result = test4(1, 2)
a, b = test4(1, 2)
print(test4Result)  # (2, 3)
print('a = ', a, 'b = ', b)  # a =  2 b =  3

print('----- 默认参数 -----')
print(test5(1))  # 4
print(test5(1, 2))  # 3

print('----- *变量名 定义可变长参数必须放到最后，其实是个 tuple -----')
print(test6(1, 2))  # 3
print(test6(1, 2, 3))  # 6
print(test6(1, 2, 3, 4))  # 10

print('----- **变量名 定义关键字参数必须放到最后，其实是个 dict，必须指定参数名称 -----')
test7(1, 2)
test7(1, 2, b=3)
test7(1, 2, b=3, g=4)

print('----- 可选参数和命名参数同时存在时，命名参数必须放到最后 -----')
test8(1, 2)
test8(1, 2, 3)
test8(1, 2, 3, b=4)
test8(1, 2, *[1, 2, 3], **{'b': 1, 'g': 2})
test8(1, 2, bga='bga', *[1, 2, 3], **{'b': 1, 'g': 2})
test8(1, 2, bga='bga', *[1, 2, 3], agb='agb', **{'b': 1, 'g': 2})

print('----- 作用域 -----')

num = 10  # 全局变量


def test9():
    print(num)  # 10


test9()


def test10():
    num = 5
    print(num)  # 5


test10()
print(num)  # 10

print('----- lambda表达式，原型为【lambda 参数:操作(参数)】 -----')


def test_fun_param(item_list, action):
    for index, item in enumerate(item_list):
        item_list[index] = (action(item))
    return item_list


def times(p1):
    return p1 * 2


print(test_fun_param(['p1', 'p2'], times))  # ['p1p1', 'p2p2']
print(test_fun_param(['p1', 'p2'], lambda p1: p1 * 3))  # ['p1p1p1', 'p2p2p2']

print('----- test closure1 -----')


def test_closure1(p1):
    base = 2

    def print_count(p2):
        print(base + p1 + p2)

    return print_count


closure1 = test_closure1(3)
closure1(1)  # 6
closure1(2)  # 7

print('----- test closure2 -----')


def test_closure2(p1):
    base = 2
    return lambda p2: base + p1 + p2


closure2 = test_closure2(3)
closure2(1)  # 6
closure2(2)  # 7
