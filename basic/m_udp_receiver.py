#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-05-13
# 描述:

import socket


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定一个本地信息
    local_addr = ("", 7788)
    udp_socket.bind(local_addr)  # 必须绑定自己电脑的 ip 以及 port，其他的不行

    while True:
        # 3. 接收数据，recv_data 这个变量中存储的是一个元组(接收到的二进制数据，(发送方的 ip, port))
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)  # (b'first udp msg', ('127.0.0.1', 54811))

        recv_msg = recv_data[0]  # 存储接收的数据
        print(type(recv_msg))  # <class 'bytes'>

        send_addr = recv_data[1]  # 存储发送方的地址信息
        print(type(send_addr))  # <class 'tuple'>

        # 4. 打印接收到的数据
        recv_msg = recv_msg.decode('utf-8')
        if recv_msg == 'exit':
            print('正常退出')
            break
        print("%s:%s" % (str(send_addr), recv_msg))

    # 5. 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
