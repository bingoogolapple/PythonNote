#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-03-31
# 描述:

"""
str 为不可变类型
str 和整数可以使用 * 重复拼接相同的字符串，不能进行其他计算
"""

print('BGA' * 3)  # BGABGABGA

print('abcdef'[3])  # d
print('abcdef'[3:])  # def
print('abcdef'[:3])  # abc
print('abcdef'[1:-2])  # bcd
print('abcdef'[-1:])  # f
print('abcdef'[:-1])  # abcde

print("abc\ndef\nghi")
print(r"abc\ndef\nghi")
print(R"abc\ndef\nghi")

print('''abc
def
ghi''')

print('''
abc
def
ghi
''')

print("""
abc
def
ghi
""")

print(len("abcde"))  # 5
print(max("aAbBeEcCdD"))  # e
print(min("aAbBeEcCdD"))  # A
print(sorted("aAbBeEcCdD"))  # ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
print(ord("A"))  # 65  获取 ASCII 码
print(ord("a"))  # 97
print(ord("1"))  # 49


# 格式化输出，多个参数或有计算时用小括号括起来，单个参数不用加小括号
def format_print():
    # 长度至少占 6，不够前面补空格
    print('%6d' % 100)  # 「   100」
    # 六位整数，不够前面补 0
    print('%06d' % 100)  # 「000100」
    # 控制小数点后两位数，不够补 0
    print('%.2f' % 100.235)  # 100.23
    # %% 输出 %
    print('%.2f%%' % 100.235)  # 100.23%

    name = input('请输入称重菜名称：')  # 哈哈
    # 输入的类型都是 str，整型和浮点型需要类型转换
    price = int(input('请输入单价：'))  # 11
    weight = float(input('请输入重量：'))  # 22

    # 名称 = 哈哈 单价 = 11 重量 = 22.0 总价 = 242.0
    print('名称 =', name, "单价 =", price, "重量 =", weight, "总价 =", price * weight)
    # 名称 = 哈哈，单价 = 11，重量 = 22.000000，总价 = 242.000000
    print('名称 = %s，单价 = %d，重量 = %f，总价 = %f' % (name, price, weight, price * weight))
    # 名称 = 哈哈，单价 = 11，重量 = 22.00，总价 = 242.000
    print('名称 = %s，单价 = %d，重量 = %.2f，总价 = %.3f' % (name, price, weight, price * weight))
    tuple_params = (name, price, weight, price * weight)  # % 后面其实就是元祖类型的参数
    print('名称 = %s，单价 = %d，重量 = %.2f，总价 = %.3f' % tuple_params)


format_print()
