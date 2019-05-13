#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-05-13
# 描述:广播 -> 单工，对讲机 -> 半双工，打电话 -> 全双工

import socket


def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 如果不绑定端口的话会随机分配一个端口
    udp_socket.bind(("", 8877))

    while True:
        # 从键盘获取数据
        send_data = input('请输入要发送的数据：')

        # 转成二进制后发送
        # udp_socket.sendto(b'first udp msg', ('127.0.0.1', 7788))
        udp_socket.sendto(send_data.encode('utf-8'), ('127.0.0.1', 7788))

        # 如果输入的数据是 exit，那么就退出程序
        if send_data == 'exit':
            print('正常退出')
            break

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
