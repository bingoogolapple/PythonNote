#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-02
# 描述:

import tt.tt_one as newname

import moduleone.tt_two
import moduletwo.tt_three

# print(tt.tt_one.name)
print(newname.name)
print(moduleone.tt_two.name)
print(moduletwo.tt_three.name)

from tt_two import name

print(name)

from tt import tt_one

print(tt_one.name)

from moduletwo.tt_four import *
from moduletwo.tt_five import *

print(four_one)
print(four_two)
print(four_three)

print(five_one)
print(five_two)
# print(five_three)

from moduletwo.tt_six import six_one, six_two

print(six_one, six_two)

# 可以通过小括号包裹来换行
from moduletwo.tt_seven import (seven_one,
                                seven_two)

print(seven_one, seven_two)

import moduleone
print(moduleone.sys.path)
print(moduleone.datetime.date)