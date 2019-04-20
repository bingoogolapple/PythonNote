#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-03-31
# 描述:

# ---------------------------- set -----------------------------

def test_set1():
    print('----- test_set1 -----')
    set1 = {1, 3, 7, 4, 5, 3, 7}
    print(type(set1))  # <class 'set'>
    print(type(set()))  # <class 'set'> 定义空的集合用 set()
    print(type({}))  # <class 'dict'> 空的字典
    print(set1)  # {1, 3, 4, 5, 7} 不重复
    print(len(set1))  # 5 不重复
    print(7 in set1)  # True
    print(7 not in set1)  # False


def test_set2():
    print('----- test_set2 -----')
    set1 = {1, 3, 7, 4, 5, 3, 7}
    set2 = {1, 2, 3, 4, 5, 6}
    set3 = {3, 4, 7}
    print(set2 - set3)  # {1, 2, 5, 6} 求两个集合差集
    print(set2 & set3)  # {3, 4} 求两个集合交集
    print(set2 | set3)  # {1, 2, 3, 4, 5, 6, 7} 求两个集合并集

    print(set2.difference(set3))  # {1, 2, 5, 6}「求两个集合差集」
    print(set3.difference(set2))  # {7}「求两个集合差集」
    print(set2.union(set3))  # {1, 2, 3, 4, 5, 6, 7}「求两个集合并集」
    print(set2.intersection(set3))  # {3, 4}「求两个集合交集」
    print(set2.symmetric_difference(set3))  # {1, 2, 5, 6, 7}「求两个集合中不重复的元素集合」

    print(set2.issubset(set1))  # False
    print(set3.issubset(set1))  # True
    print(set1.issuperset(set3))  # True

    set2.intersection_update(set3)  # 求两个集合交集，并赋值给左侧集合
    print(set2)  # {3, 4}
    set3.difference_update(set2)  # 求两个集合差集，并赋值给左侧集合
    print(set3)  # {7}
    set3.update(set2)  # 合并集合，并赋值给左侧集合
    print(set3)  # {3, 4, 7}

    # discard 和 remove 都可以删除 set 当中的元素
    set3.remove(3)  # 移除的元素在集合中不存在时会报错
    set3.discard(3)  # 移除的元素在集合中不存在时不会报错
    print(set3)  # {4, 7}
    set3.add("新增的")
    print(set3)  # {4, '新增的', 7}
    print(set3.pop())  # 不确定「随机移除一个元素」
    print(set3)  # 不确定，pop 是随机移除一个元素
    set3.clear()
    print(set3)  # set()

    print({1, 3, 4}.isdisjoint({2, 5, 6}))  # True「isdisjoint 判断两个集合是否不包含相同的任意一个元素，不包含则返回 True，否则返回 False」
    print({1, 3, 4}.isdisjoint({2, 3, 5, 6}))  # False


test_set1()
test_set2()


# ----------------------------- dict ----------------------------

def test_dict1():
    print('----- test_dict1 -----')
    dict1 = {'key1': 1, "key2": 2, 3: 4, "3": 2, True: 'bool 类型作为 key', (1, 2): '要求 key 为不可变类型，如元组'}
    print(type(dict1))  # <class 'dict'>
    print(type({}))  # <class 'dict'>
    print(dict1)  # {'key1': 1, 'key2': 2, 3: 4, '3': 2, True: 'bool 类型作为 key', (1, 2): '要求 key 为不可变类型，如元组'}


def test_dict2():
    print('----- test_dict2 -----')
    dict1 = {'name': 'BGA', 'B': 'bingo', 'G': 'googol', 'A': 'apple'}
    print(len(dict1))  # 4
    print(dict1['name'])  # BGA「如果 key 不存在会报错」
    print(dict1.get('name'))  # BGA「如果 key 不存在则返回 None」

    dict1.setdefault('name1', '我是默认值')
    print(dict1.get('name1'))  # 我是默认值
    print(dict1['name1'])  # 我是默认值

    print(dict1.get('name2'))  # None
    print(dict1.get('name2', '我是默认值'))  # 我是默认值
    # print(dict1['name2'])  # 会报错

    dict1['age'] = 27  # 不存在则新增
    dict1['name'] = 'bingoogolapple'  # 存在则修改
    print(dict1)  # {'name': 'bingoogolapple', 'B': 'bingo', 'G': 'googol', 'A': 'apple', 'age': 27}
    print(dict1.pop('B'))  # bingo「删除指定 key 并返回 value，如果 key 不存在会报错」
    print(dict1)  # {'name': 'bingoogolapple', 'G': 'googol', 'A': 'apple', 'age': 27}
    print(dict1.popitem())  # ('age', 27)「删除末尾键值对」
    print(dict1)  # {'name': 'bingoogolapple', 'G': 'googol', 'A': 'apple'}

    temp_dict = {'BGA': 'bingoogolapple', 'name': 'BGA'}
    dict1.update(temp_dict)  # 合并字典，旧的字典里已经存在的会被覆盖
    print(dict1)  # {'name': 'BGA', 'G': 'googol', 'A': 'apple', 'BGA': 'bingoogolapple'}
    dict1.clear()  # 清空字典
    print(dict1)


def test_dict3():
    print('----- test_dict3 -----')
    dict1 = {'short': 'BGA', 'long': 'bingoogolapple', 'B': 'bingo', 'G': 'googol', 'A': 'apple'}
    '''
    short BGA
    long bingoogolapple
    B bingo
    G googol
    A apple
    '''
    for key in dict1:
        print(key, dict1[key])
    '''
    short BGA
    long bingoogolapple
    B bingo
    G googol
    A apple
    '''
    for key in dict1.keys():
        print(key, dict1[key])
    print(dict1.keys())  # dict_keys(['short', 'long', 'B', 'G', 'A'])
    '''
    BGA
    bingoogolapple
    bingo
    googol
    apple
    '''
    for value in dict1.values():
        print(value)
    print(dict1.values())  # dict_values(['BGA', 'bingoogolapple', 'bingo', 'googol', 'apple'])
    '''
    ('short', 'BGA')
    ('long', 'bingoogolapple')
    ('B', 'bingo')
    ('G', 'googol')
    ('A', 'apple')
    '''
    for item in dict1.items():
        print(item)
    print(
        dict1.items())  # dict_items([('short', 'BGA'), ('long', 'bingoogolapple'), ('B', 'bingo'), ('G', 'googol'), ('A', 'apple')])
    '''
    short BGA
    long bingoogolapple
    B bingo
    G googol
    A apple
    '''
    for key, value in dict1.items():
        print(key, value)


def test_dict4():
    print('----- test_dict4 -----')
    print(dict.fromkeys(['B', 'G', 'A']))  # {'B': None, 'G': None, 'A': None}
    print(dict.fromkeys(('B', 'G', 'A')))  # {'B': None, 'G': None, 'A': None}
    print(dict.fromkeys(['B', 'G', 'A'], 10))  # {'B': 10, 'G': 10, 'A': 10}
    print(dict.fromkeys(('B', 'G', 'A'), 10))  # {'B': 10, 'G': 10, 'A': 10}

    dict1 = {'short': 'BGA', 'long': 'bingoogolapple', 'B': 'bingo', 'G': 'googol', 'A': 'apple'}
    dict2 = dict1.copy()  # 拷贝字典
    dict2['B'] = '修改后'
    print(dict1)  # {'short': 'BGA', 'long': 'bingoogolapple', 'B': 'bingo', 'G': 'googol', 'A': 'apple'}
    print(dict2)  # {'short': 'BGA', 'long': 'bingoogolapple', 'B': '修改后', 'G': 'googol', 'A': 'apple'}
    print(dict1.__contains__('short'))  # True
    print(dict1.__contains__('short1'))  # False
    print('short' in dict1)  # False


test_dict1()
test_dict2()
test_dict3()
test_dict4()
