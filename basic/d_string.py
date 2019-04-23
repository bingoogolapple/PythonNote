#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-03-31
# 描述:


def test_str1():
    print('----- test_str1 -----')
    """
    str 为不可变类型
    str 和整数可以使用 * 重复拼接相同的字符串，不能进行其他计算
    """

    str1 = 'BGA'
    '''
    B <class 'str'>
    G <class 'str'>
    A <class 'str'>
    '''
    for c in str1:
        print(c, type(c))

    str1 = str1 * 3
    print(str1)  # BGABGABGA
    print(str1.count('GA'))  # 3
    print(str1.index('GA'))  # 1「不存在时会报错」
    print(str1.index('GA', 2))  # 4 从指定范围内找 [start,end)
    print('B' in 'BGA')  # True

    print('abcdef'[3])  # d
    print('abcdef'[3:])  # def
    print('abcdef'[:3])  # abc
    print('abcdef'[1:-2])  # bcd
    print('abcdef'[-1:])  # f
    print('abcdef'[:-1])  # abcde


def test_str2():
    print('----- test_str2 -----')
    '''
    abc
    def
    ghi
    '''
    print("abc\ndef\nghi")
    print(r"abc\ndef\nghi")  # abc\ndef\nghi
    print(R"abc\ndef\nghi")  # abc\ndef\nghi

    '''
abc
    def
    ghi
    '''
    print('''abc
    def
    ghi''')

    '''
    
    abc
    def
    ghi
    
    '''
    print('''
    abc
    def
    ghi
    ''')

    '''
    
    abc
    def
    ghi
    
    '''
    print("""
    abc
    def
    ghi
    """)


def test_str3():
    print('----- test_str3 -----')
    print(len("abcde"))  # 5
    print(max("aAbBeEcCdD"))  # e
    print(min("aAbBeEcCdD"))  # A
    print(sorted("aAbBeEcCdD"))  # ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    print(ord("A"))  # 65  获取 ASCII 码
    print(ord("a"))  # 97
    print(ord("1"))  # 49


def test_str4():
    print('----- test_str4 -----')
    # isspace 判断字符串中是否只包含空格和转移字符
    print(''.isspace())  # False
    print(' '.isspace())  # True
    print('\t'.isspace())  # True
    print('\t\r'.isspace())  # True

    '''
    isdecimal 判断是否只包含数字，全角数字「日常开发中推荐用这个」
    isdigit   判断是否只包含数字，全角数字、⑴、\u00b2
    isnumeric 判断是否只包含数字，全角数字、汉字数字
    '''
    print('一千零一')
    print('1'.isdecimal())  # True
    print('1.1'.isdecimal())  # False
    print('⑴'.isdigit())  # True
    print('一千零一'.isnumeric())  # True
    # 判断是否只包含字母或数字
    print('a2'.isalnum())  # True
    # 判断是否只包含字母
    print('a2'.isalpha())  # False
    print('a'.isalpha())  # True
    # 判断每个单词是否都是首字母大写，其余字母小写
    print('Your Presence Is A Gift To The World.'.istitle())  # True
    # 判断是否全大写
    print('BGA。。..'.isupper())  # True
    # 判断是否全小写
    print('bingoogolapple。。..'.islower())  # True


def test_str5():
    print('----- test_str5 -----')
    print('bingoogolapple'.startswith('bingo'))  # True
    print('bingoogolapple'.endswith('apple'))  # True
    # 检测指定范围内是否包含指定字符串，存在则返回开始的索引值，否则返回 -1
    print('bingoogolapple'.find('googol'))  # 3
    # 检测指定范围内是否包含指定字符串，存在则返回开始的索引值，否则报错
    print('bingoogolapple'.index('googol'))  # 3
    # 替换字符串中的内容，会返回新的字符串
    print('bingoogolapple'.replace('googol', 'GOOGOL'))  # binGOOGOLapple
    print('bingoogolapple'.count('g'))  # 2


def test_str6():
    print('----- test_str6 -----')
    # 把字符串的第一个字符大写
    print('bingo googol apple'.capitalize())  # Bingo googol apple
    # 把字符串的每个单词首字母大写
    print('bingo googol apple'.title())  # Bingo Googol Apple
    # 全部转换成大写
    print('Bingo Googol Apple'.upper())  # BINGO GOOGOL APPLE
    # 全部转换成小写
    print('Bingo Googol Apple'.lower())  # bingo googol apple
    # 反转大小写
    print('Bingo Googol Apple'.swapcase())  # bINGO gOOGOL aPPLE


def test_str7():
    print('----- test_str7 -----')
    poem = ['静夜思', '李白', ' 床前明月光', '疑是地上霜\t', '举头望明月\n', '低头思故乡']
    for item in poem:
        print('|%s|' % item.strip().center(12, '　'))


def test_str8():
    print('----- test_str8 -----')
    poem = '静夜思\n李白\t\n床前明月光\r\n疑是地上霜\n举头望明月\n低头思故乡'
    print(poem)
    print(poem.split())  # ['静夜思', '李白', '床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
    print('|'.join(poem.split()))  # 静夜思|李白|床前明月光|疑是地上霜|举头望明月|低头思故乡
    # 把字符串分成一个 3 元素的元组 (str前面, str, str后面)
    print('bingoogolapple'.partition('googol'))  # ('bin', 'googol', 'apple')


def test_str9():
    print('----- test_str9 -----')
    # 字符串[开始索引:结束索引:步长]，不包含结束索引
    num_str = "0123456789"
    # 1. 截取从 2 ~ 5 位置 的字符串
    print(num_str[2:6])  # 2345
    # 2. 截取从 2 ~ `末尾` 的字符串
    print(num_str[2:])  # 23456789
    # 3. 截取从 `开始` ~ 5 位置 的字符串
    print(num_str[:6])  # 012345
    # 4. 截取完整的字符串
    print(num_str[:])  # 0123456789
    # 5. 从开始位置，每隔一个字符截取字符串
    print(num_str[::2])  # 02468
    # 6. 从索引 1 开始，每隔一个取一个
    print(num_str[1::2])  # 13579

    # 倒序切片，-1 表示倒数第一个字符
    print(num_str[-1])  # 9
    # 7. 截取从 2 ~ `末尾 - 1` 的字符串
    print(num_str[2:-1])  # 2345678
    # 8. 截取字符串末尾两个字符
    print(num_str[-2:])  # 89
    # 9. 字符串的逆序（面试题），从最后一个字符开始往前
    print(num_str[-1::-1])  # 9876543210
    print(num_str[::-1])  # 9876543210


# 格式化输出，多个参数或有计算时用小括号括起来，单个参数不用加小括号
def format_print():
    print('----- format_print -----')
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


# test_str1()
# test_str2()
# test_str3()
# test_str4()
# test_str5()
# test_str6()
# test_str7()
# test_str8()
test_str9()
# format_print()
