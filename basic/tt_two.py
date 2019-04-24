#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-02
# 描述:

name = "tt_two"

# 在导入文件时，文件中所有没有任何缩进的代码都会被执行一遍，导入多少次就会执行多少次
print('导入了 tt_two')

# 直接导入 tt_two 时输出 tt_two，导入 basic.tt_two 时输出 basic.tt_two
# 直接运行时输出 __main__
print(__name__)


def tt_two_method():
    print('tt_two 中的方法')


if __name__ == '__main__':
    print('作为模块被导入时不会执行到这里，只有单独运行当前文件时才会执行到这里')
    tt_two_method()
