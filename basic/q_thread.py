#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-05-16
# 描述:

import time
import threading


def sing(p1):
    """唱歌 5秒钟"""
    for i in range(3):
        print('%s 正在唱歌' % p1)
        time.sleep(1)


def dance(p1, p2):
    """跳舞 5秒钟"""
    for i in range(3):
        print('%s 和 %s 正在跳舞' % (p1, p2))
        time.sleep(1)


def test1():
    # sing('BGA')
    # dance('BGA', 'bingoogolapple')

    print(threading.enumerate())

    # target 指定将来这个线程去哪个函数执行代码
    # args 指定将来调用函数的时候传递什么数据过去，为元组，只有一个参数时后面要加个逗号
    t1 = threading.Thread(target=sing, args=('BGA',))
    t2 = threading.Thread(target=dance, args=('BGA', 'bingoogolapple'))
    print(threading.enumerate())
    t1.start()
    print(threading.enumerate())  # start 之后 enumerate 才会包含
    t2.start()
    print(threading.enumerate())


########################################################################

# 定义一个全局变量，多线程之间共享全局变量
g_num = 0


def testa(num):
    global g_num
    for i in range(num):
        # 上锁，如果之前没有被上锁，那么此时 上锁成功
        # 如果上锁之前 已经被上锁了，那么此时会堵塞在这里，直到 这个锁被解开位置
        mutex.acquire()
        g_num += 1
        # 解锁
        mutex.release()
    print("-----in test1 g_num=%d----" % g_num)


def testb(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("-----in test2 g_num=%d=----" % g_num)


# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def test2():
    t1 = threading.Thread(target=testa, args=(1000000,))
    t2 = threading.Thread(target=testb, args=(1000000,))

    t1.start()
    t2.start()

    # 等待上面的2个线程执行完毕....
    time.sleep(2)

    print("-----in main Thread g_num = %d---" % g_num)


test2()


def testc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


def test3():
    t1 = threading.Thread(target=testc, args=(11, 22, 33, 44, 55, 66, 77, 88), kwargs={"mm": 11})
    t1.start()


test3()
