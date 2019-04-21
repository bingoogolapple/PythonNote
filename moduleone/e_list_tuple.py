#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-03-31
# 描述:列表可变，元祖不可变


def test_tuple1():
    print('----- test_tuple1 -----')
    print(type((1, 2, 3)))  # <class 'tuple'>
    print(type((1)))  # <class 'int'>
    print(type((1,)))  # <class 'tuple'> 元组里只有一个元素的话加个逗号，否则会被视为 int
    print(type(()))  # <class 'tuple'>
    print(3 in (1, 3, 5))  # True
    print(4 not in (1, 3, 5))  # True
    print(len((1, 3, 5)))  # 3
    print(max((1, 5, 3)))  # 5
    print(min((1, 5, 3)))  # 1
    print(sorted((1, 5, 3)))  # [1, 3, 5]


def test_tuple2():
    print('----- test_tuple2 -----')
    origin_tuple = (1, 3, 7, 4, 5, 3, 9)
    print(origin_tuple.index(3))  # 1 不存在时会报错
    print(origin_tuple.index(3, 2, 6))  # 5 从指定范围内找 [start,end)
    print(origin_tuple.count(3))  # 2


def test_tuple3():
    print('----- test_tuple3 -----')
    tuple_one = ('B', "bingo", 'G', 'googol', 'A', 'apple')
    # B bingo G googol A apple
    for item in tuple_one:
        print(item, end=' ')
    print()
    # 0 B 1 bingo 2 G 3 googol 4 A 5 apple
    for index, item in enumerate(tuple_one):
        print(index, item, end=' ')
    print()
    # (0, 'B') (1, 'bingo') (2, 'G') (3, 'googol') (4, 'A') (5, 'apple')
    for item in enumerate(tuple_one):
        print(item, end=' ')
    print()


def test_list1():
    print('----- test_list1 -----')
    print(type([1, 2, 3]))  # <class 'list'>
    print(type([1]))  # <class 'list'>
    print(type([]))  # <class 'list'>
    print(3 in [1, 3, 5])  # True
    print(4 not in [1, 3, 5])  # True
    print(len([1, 3, 5]))  # 3
    print(len([1, 3, ]))  # 2
    print(max([1, 5, 3]))  # 5
    print(min([1, 5, 3]))  # 1
    print(sorted([1, 5, 3]))  # [1, 3, 5]


def test_list2():
    print('----- test_list2 -----')
    list_one = [1, 3, 7, 4, 5, 3, 9]
    list_two = [11, 33, 22]
    print(list_one[1])  # 3
    print(list_one.index(3))  # 1 不存在时会报错
    print(list_one.index(3, 2, 6))  # 5 从指定范围内找 [start,end)
    print(list_one.count(3))  # 2 数据在列表中出现的次数
    list_one.insert(1, 11111)  # 指定索引位置插入值
    print(list_one)  # [1, 11111, 3, 7, 4, 5, 3, 9]
    list_one[1] = 22222  # 修改指定索引位置的值
    print(list_one)  # [1, 22222, 3, 7, 4, 5, 3, 9]

    del list_one[1]  # 删除指定索引的数据
    print(list_one)  # [1, 3, 7, 4, 5, 3, 9]
    name = 'BGA'
    print(name)
    # del 关键字本质上是用来将一个变量从内存中删除的，删除后后续的代码就不能再使用该变量了
    del name
    # print(name)

    list_one.append(9999)  # 末尾追加
    print(list_one)  # [1, 3, 7, 4, 5, 3, 9, 9999]
    list_one.extend(list_two)  # list_two 的内容追加到 list_one 末尾
    print(list_one)  # [1, 3, 7, 4, 5, 3, 9, 9999, 11, 33, 22]
    list_one.remove(3)  # 删除第一个出现的 3
    print(list_one)  # [1, 7, 4, 5, 3, 9, 9999, 11, 33, 22]
    list_one.pop()  # 删除末尾的数据
    print(list_one)  # [1, 7, 4, 5, 3, 9, 9999, 11, 33]
    list_one.pop(1)  # 删除指定索引的数据
    print(list_one)  # [1, 4, 5, 3, 9, 9999, 11, 33]
    list_one.sort()  # 升序排列
    print(list_one)  # [1, 3, 4, 5, 9, 11, 33, 9999]

    list_one.sort(reverse=True)  # 降序排列，不是反转
    list_one.sort(reverse=True)
    print(list_one)  # [9999, 33, 11, 9, 5, 4, 3, 1]
    list_one.reverse()  # 反转
    print(list_one)  # [1, 3, 4, 5, 9, 11, 33, 9999]
    list_one.reverse()  # 反转
    print(list_one)  # [9999, 33, 11, 9, 5, 4, 3, 1]

    list_one.insert(3, "可以插入不同类型的数据")
    print(list_one)  # [9999, 33, 11, '可以插入不同类型的数据', 9, 5, 4, 3, 1]
    list_one.clear()  # 清空列表
    print(list_one)  # []


def test_list3():
    print('----- test_list3 -----')
    list_one = ['B', "bingo", 'G', 'googol', 'A', 'apple']
    # B bingo G googol A apple
    for item in list_one:
        print(item, end=' ')
    print()
    # 0 B 1 bingo 2 G 3 googol 4 A 5 apple
    for index, item in enumerate(list_one):
        print(index, item, end=' ')
    print()
    # (0, 'B') (1, 'bingo') (2, 'G') (3, 'googol') (4, 'A') (5, 'apple')
    for item in enumerate(list_one):
        print(item, end=' ')
    print()


def test_slice():
    print('----- test_slice -----')
    # 列表或元祖[开始索引:结束索引:步长]，不包含结束索引
    list_one = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 1. 截取从 2 ~ 5 位置 的元素
    print(list_one[2:6])  # [2, 3, 4, 5]
    # 2. 截取从 2 ~ `末尾` 的元素
    print(list_one[2:])  # [2, 3, 4, 5, 6, 7, 8, 9]
    # 3. 截取从 `开始` ~ 5 位置 的元素
    print(list_one[:6])  # [0, 1, 2, 3, 4, 5]
    # 4. 截取完整的元素
    print(list_one[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 5. 从开始位置，每隔一个元素截取元素
    print(list_one[::2])  # [0, 2, 4, 6, 8]
    # 6. 从索引 1 开始，每隔一个取一个
    print(list_one[1::2])  # [1, 3, 5, 7, 9]

    # 倒序切片，-1 表示倒数第一个元素
    print(list_one[-1])  # 9
    # 7. 截取从 2 ~ `末尾 - 1` 的元素
    print(list_one[2:-1])  # [2, 3, 4, 5, 6, 7, 8]
    # 8. 截取元素末尾两个元素
    print(list_one[-2:])  # [8, 9]
    # 9. 元素的逆序（面试题），从最后一个元素开始往前
    print(list_one[-1::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(list_one[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def test_list_tuple():
    print('----- test_list_tuple -----')
    list_one = ['B', "bingo", 'G', 'googol', 'A', 'apple']
    print(type(list_one))  # <class 'list'>
    tmp = tuple(list_one)
    print(type(list_one))  # <class 'list'>
    print(type(tmp))  # <class 'tuple'>
    tmp = list(tmp)
    print(type(tmp))  # <class 'list'>

    print([1, 2] + [3, 4])  # [1, 2, 3, 4]
    print((1, 2) + (3, 4))  # (1, 2, 3, 4)
    print(["BGA"] * 4)  # ['BGA', 'BGA', 'BGA', 'BGA']
    print(("BGA",) * 4)  # ('BGA', 'BGA', 'BGA', 'BGA')
    print((1, 2, 3) < (2, 2, 3))  # True


# test_tuple1()
# test_tuple2()
# test_tuple3()
# test_list1()
# test_list2()
# test_list3()
# test_slice()
test_list_tuple()
