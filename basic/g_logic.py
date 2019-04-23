#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-02
# 描述:

import random

condition = False
# 使用 not 关键字取非
if not condition:
    print('aaaaaa')
else:
    print('bbbbbbbbbb')

# 包含开始和结尾
a = random.randint(1, 3)
b = random.randint(1, 3)
print(a, b)

if ((a == 1 and b == 1)
        or (a == 2 and b == 2)
        or (a == 3 and b == 3)
        or (a == 4 and b == 4)
        or (a == 5 and b == 5)):
    print('aa')
elif a == 1 or b == 2:
    print('bb')
elif a == 3 and b == 1:
    print('cc')
elif a == 4:
    # 空语句/占位语句。如果在开发程序时不希望立刻编写分支内部的代码，可以使用 pass 关键字，表示一个占位符，能够保证程序的代码结构正确！程序运行时，pass 关键字不会执行任何的操作！
    pass
else:
    print('dd')

counter = 1
while counter <= 10:
    print(counter, end=' ')
    counter += 1
    # 没有 ++counter、counter++、--counter、counter-- 语法
else:
    print('正常结束时会执行到这里，加了 break 就不会，即使是最后一次循环时 break 也不会走到这里')

listOne = ['11', '22', '33']
for item in listOne:
    print(item, end=' ')
else:
    print('正常结束时会执行到这里，加了 break 就不会，即使是最后一次循环时 break 也不会走到这里')

# 3 4 5 6 7 8 9
for item in range(3, 10):
    print(item, end=' ')
print()

# 3 6 9
for item in range(3, 10, 3):
    print(item, end=' ')
print()

# 10 8 6 4
for item in range(10, 2, -2):
    print(item, end=' ')
print()

# enumerate 的第二个参数可以指定开始索引，默认为 0
for index, item in enumerate(listOne):
    print(index, item)

listTwo = [1, 2, 3, 4, 5, 6, 7, 8]
print(listTwo[0:len(listTwo):2])  # [1, 3, 5, 7]
