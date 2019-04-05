#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-05
# 描述:


def test1():
    print('test1')


def test2(p1, p2):
    print('p1 = ', p1, 'p2 = ', p2)
    p1 + p2


# 仅仅位置参数
def test3(p1, p2):
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
print(test1())  # None
print('----- 不写 return 时返回 None -----')
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
