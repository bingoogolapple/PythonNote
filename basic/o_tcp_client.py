#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-05-13
# 描述:

import socket


def download_file(tcp_socket):
    download_file_name = input('请输入要下载的文件名:')
    tcp_socket.send(download_file_name.encode('utf-8'))

    recv_data = tcp_socket.recv(1024)
    if recv_data:
        # 7. 保存接收到的数据到一个文件中
        with open("[新]" + download_file_name, 'wb') as f:
            f.write(recv_data)


def main():
    # 1. 创建 tcp 的套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 链接服务器
    tcp_socket.connect(('127.0.0.1', 8888))

    while True:
        # 3. 发送数据/接收数据
        send_data = input('请输入要发送的数据:')
        if send_data:
            tcp_socket.send(send_data.encode('utf-8'))

            recv_data = tcp_socket.recv(1024)
            print(recv_data.decode('utf-8'))

            if send_data == 'download':
                download_file(tcp_socket)
            elif send_data == 'exit':
                break
        else:
            break

    # 4. 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
