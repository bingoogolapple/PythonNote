#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-05-05
# 描述:


def copy_small_file():
    # 1. 打开
    file_read = open("a_var.py")
    file_write = open("a_var.py.bak", "w")

    # 2. 读、写
    text = file_read.read()
    file_write.write(text)

    # 3. 关闭
    file_read.close()
    file_write.close()


def copy_large_file():
    # 1. 打开
    file_read = open("a_var.py")
    file_write = open("a_var.py.bak", "w")

    # 2. 读、写
    while True:
        # 读取一行内容
        text = file_read.readline()

        # 判断是否读取到内容
        if not text:
            break

        file_write.write(text)

    # 3. 关闭
    file_read.close()
    file_write.close()


copy_large_file()
