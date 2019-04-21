#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-21
# 描述:

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


test_scope3()
print(num)  # 5


def test_scope4(num_list):
    num_list.append(4)
    # 列表的 += 本质上是在调用 extend 方法
    num_list += [5, 6]
    num_list.extend([7, 8])
    print(num_list)  # [1, 2, 3, 4, 5, 6, 7, 8]


gl_list = [1, 2, 3]
test_scope4(gl_list)
print(gl_list)  # [1, 2, 3, 4, 5, 6, 7, 8]
