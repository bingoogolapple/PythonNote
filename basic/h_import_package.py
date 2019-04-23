#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-02
# 描述:

import tt.tt_one as newname

import basic.tt_two
import othermodule.tt_three

# print(tt.tt_one.name)
print(newname.name)
print(basic.tt_two.name)
print(othermodule.tt_three.name)

from tt_two import name

print(name)

from tt import tt_one

print(tt_one.name)

from othermodule.tt_four import *
from othermodule.tt_five import *

print(four_one)
print(four_two)
print(four_three)

print(five_one)
print(five_two)
# print(five_three)

from othermodule.tt_six import six_one, six_two

print(six_one, six_two)

# 可以通过小括号包裹来换行
from othermodule.tt_seven import (seven_one,
                                  seven_two)

print(seven_one, seven_two)

import basic

print(basic.sys.path)
print(basic.datetime.date)
