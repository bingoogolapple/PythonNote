#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-21
# 描述:在一个函数中对全局变量进行修改的时候，到底是否需要使用 global 进行说明，要看是否对全局变量的指向进行了修改
# 如果修改了指向，即让全局变量指向一个新的地方，那么必须使用 global
# 如果仅仅修改了指向的空间中的数据，此时不用必须使用 global

print('----- 作用域 -----')

num = 10  # 全局变量


def test_scope1():
    # 在函数内部可以通过全局变量的引用获取对应的数据
    print(num)  # 10
    print(gl_title)  # BGA
    # 在开发时应该把模块中的所有全局变量定义在所有函数上方，就可以保证所有的函数都能够正常访问到每一个全局变量了
    # print(name)  # 会报错，调用函数 test9 时还未定义全局变量 name


# 建议定义全局变量时使用「g_」或「gl_」开头
gl_title = 'BGA'
nums = [11, 22]
test_scope1()
name = 'bingoogolapple'


def test_scope2():
    # 不允许在函数内部直接修改全局变量的值，如果使用赋值语句，会在函数内部定义一个局部变量
    num = 5
    print(num)  # 5


test_scope2()
print(num)  # 10


def test_scope3():
    # 希望修改全局变量的值，使用「global 变量名」声明一下即可，global 关键字会告诉解释器后面的变量是一个全局变量，再使用赋值语句时就不会创建局部变量
    global num
    num = 5
    print(num)  # 5

    nums.append(33)  # 修改引用里的值，并不是修改 nums 的指向


test_scope3()
print(num)  # 5
print(nums)  # [11, 22, 33]


def test_scope4(num_list):
    num_list.append(4)
    # 列表的 += 本质上是在调用 extend 方法
    num_list += [5, 6]
    num_list.extend([7, 8])
    print(num_list)  # [1, 2, 3, 4, 5, 6, 7, 8]


gl_list = [1, 2, 3]
test_scope4(gl_list)
print(gl_list)  # [1, 2, 3, 4, 5, 6, 7, 8]
