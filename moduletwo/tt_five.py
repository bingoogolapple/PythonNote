#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-02
# 描述:

# 指定其他模块配置「from moduletwo.tt_five import *」时只导出 five_one 和 five_two
__all__ = ['five_one', 'five_two']

five_one = "five_one"
five_two = "five_two"
five_three = "five_three"
