#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-05-13
# 描述:

import socket


def send_file_2_client(new_client_socket, client_addr):
    # 1. 接收客户端 需要下载的文件名
    # 接收客户端发送过来的要下载的文件名
    file_name = new_client_socket.recv(1024).decode('utf-8')
    print('客户端(%s)需要下载文件是：%s' % (str(client_addr), file_name))

    file_content = None
    # 2. 打开这个文件，读取数据
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print('没有要下载的文件(%s)' % file_name)

    # 3. 发送文件的数据给客户端
    if file_content:
        new_client_socket.send(file_content)


def main():
    # 1. 买个手机(创建套接字 socket)
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 插入手机卡(绑定本地信息 bind)
    tcp_server_socket.bind(('', 8888))

    # 3. 将手机设置为正常的 响铃模式(让默认的套接字由主动变为被动 listen)
    tcp_server_socket.listen(128)

    try:
        # 循环目的：调用多次accept,从而为多个客户端服务
        while True:
            print('等待一个新的客户端的到来...')
            # 4. 等待别人的电话到来(等待客户端的链接 accept)
            new_client_socket, client_addr = tcp_server_socket.accept()

            print('一个新的客户端已经到来 %s' % str(client_addr))

            # 循环目的: 为同一个客户端 服务多次
            while True:
                # 接收客户端发送过来的请求
                recv_data = new_client_socket.recv(1024)

                # 如果 recv 解堵塞，那么有 2 种方式：
                # 1. 客户端发送过来数据
                # 2. 客户端调用close导致而了 这里 recv解堵塞
                if recv_data:
                    recv_data = recv_data.decode('utf-8')
                    print('客户端福送过来的请求是:%s' % recv_data)
                    # 回送一部分数据给客户端
                    new_client_socket.send('我是 server，收到了你发来的信息'.encode('utf-8'))

                    if recv_data == 'download':
                        send_file_2_client(new_client_socket, client_addr)
                else:
                    break

            # 关闭套接字
            # 关闭accept返回的套接字 意味着 不会在为这个客户端服务
            new_client_socket.close()
            print('已经为这个客户端服务完毕。。。。')
    finally:
        # 如果将监听套接字关闭了，那么会导致不能再次等待新客户端的到来，即 tcp_server_socket.accept() 就会失败
        tcp_server_socket.close()


if __name__ == '__main__':
    main()
