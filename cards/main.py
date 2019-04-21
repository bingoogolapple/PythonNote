#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-21
# 描述:

import cards.tools as tools

while True:
    # 显示功能菜单
    tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3 针对名片的操作
    if action_str in ['1', '2', '3']:
        # 新增名片
        if action_str == '1':
            tools.new_card()
        # 显示全部名片
        elif action_str == '2':
            tools.show_all()
        # 查询名片
        elif action_str == '3':
            tools.search_card()
    # 0 退出系统
    elif action_str == '0':
        print("欢迎再次使用【名片管理系统】")
        break
    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的参数不正确，请重新选择")
