#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-02
# 描述:

print('请输入参数：')
# a = input()
a = 1
print('参数为', a, type(a))
a = int(a)

if a == 1:
    print('aa')
elif a == 2:
    print('bb')
elif a == 3:
    print('cc')
elif a == 4:
    # 空语句/占位语句
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
