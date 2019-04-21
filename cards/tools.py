#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-21
# 描述:

card_list = [{'name': 'BGA', 'phone': '12345678912', 'qq': '123456789', 'email': '123456789@qq.com'}]


def show_menu():
    """显示菜单"""
    print("")
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print("")
    print("【1】新增名片")
    print("【2】显示全部")
    print("【3】搜索名片")
    print("")
    print("【0】退出系统")
    print("*" * 50)
    print("")


def new_card():
    """新增名片"""
    print("-" * 50)
    print("【新增名片】\n")

    # 1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    # 2. 使用用户输入的信息建立一个名片字典
    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str
    }

    # 3. 将名片字典添加到列表中
    card_list.append(card_dict)

    # 4. 提示用户添加成功
    print("\n添加【%s】的名片成功！\n" % name_str)
    print_card_title()
    print_card_dict(card_dict)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("【显示所有名片】\n")

    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何的名片记录，请使用【新增名片】功能添加名片！")
        return
    print_card_list()


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("【搜索名片】\n")

    # 1. 提示用户输入要搜索的姓名
    name_str = input("请输入要搜索的姓名：")
    # 2. 遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == name_str:
            print_card_title()
            print_card_dict(card_dict)
            deal_card_dict(card_dict)
            break
    else:
        print("抱歉，没有找到【%s】" % name_str)


def deal_card_dict(card_dict):
    action_str = input("请选择要执行的操作！【1】修改【2】删除【0】返回上级菜单")

    if action_str == "1":
        card_dict["name"] = input_card_info(card_dict["name"], "姓名：")
        card_dict["phone"] = input_card_info(card_dict["phone"], "电话：")
        card_dict["qq"] = input_card_info(card_dict["qq"], "QQ：")
        card_dict["email"] = input_card_info(card_dict["email"], "邮箱：")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(card_dict)
        print("删除名片成功！")


def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    # 1. 提示用户输入内容
    result_str = input(tip_message)
    # 2. 针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3. 如果用户没有输入内容，返回 `字典中原有的值`
    else:
        return dict_value


def print_card_title():
    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name.ljust(20), end="\t")

    print("")
    # 打印分隔线
    print("=" * 100)


def print_card_dict(card_item):
    print("%s\t%s\t%s\t%s" % (card_item["name"].ljust(20),
                              card_item["phone"].ljust(20),
                              card_item["qq"].ljust(20),
                              card_item["email"].ljust(20)))


def print_card_list():
    print_card_title()
    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print_card_dict(card_dict)
