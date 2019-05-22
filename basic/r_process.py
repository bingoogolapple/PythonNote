#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-05-16
# 描述:

import time
import multiprocessing
import os
import random


def sing(p1):
    """唱歌 5秒钟"""
    print("---- sing 子进程 pid=%d，父进程的 pid=%d---" % (os.getpid(), os.getppid()))
    for i in range(3):
        print('%s 正在唱歌' % p1)
        time.sleep(1)


def dance(p1, p2):
    """跳舞 5秒钟"""
    print("---- dance 子进程 pid=%d，父进程的 pid=%d---" % (os.getpid(), os.getppid()))
    for i in range(3):
        print('%s 和 %s 正在跳舞' % (p1, p2))
        time.sleep(1)


def test1():
    print("---- 主进程 pid=%d，父进程的 pid=%d---" % (os.getpid(), os.getppid()))
    # target 指定将来这个进程去哪个函数执行代码
    # args 指定将来调用函数的时候传递什么数据过去，为元组，只有一个参数时后面要加个逗号
    p1 = multiprocessing.Process(target=sing, args=('BGA',))
    p2 = multiprocessing.Process(target=dance, args=('BGA', 'bingoogolapple'))
    p1.start()
    p2.start()


# test1()

print('----- 传递参数到子进程 -----')


def testa(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


def test2():
    p1 = multiprocessing.Process(target=testa, args=(11, 22, 33, 44, 55, 66, 77, 88), kwargs={"mm": 11})
    p1.start()


# test2()

print('----- 多进程之间不共享全局变量，即使传参数进去也不共享 -----')
nums = [11, 22, 33]


def testb(args):
    args.append(44)
    nums.append(44)
    print("testb 中 args=%s" % str(args))  # [11, 22, 33, 44]
    print("testb 中 nums=%s" % str(nums))  # [11, 22, 33, 44]
    time.sleep(3)


def testc(args):
    print("testc 中 args=%s" % str(args))  # [11, 22, 33]
    print("testc 中 nums=%s" % str(nums))  # [11, 22, 33]


def test3():
    p = multiprocessing.Process(target=testb, args=(nums,))
    p.start()
    p.join()  # 等待进程 p 执行完才往下走

    p2 = multiprocessing.Process(target=testc, args=(nums,))
    p2.start()


# test3()

print('----- 多进程之间通过 Queue 来实现数据共享 -----')


def download_from_web(q):
    """下载数据"""
    # 模拟从网上下载的数据
    data = [11, 22, 33, 44]

    # 向队列中写入数据
    for temp in data:
        print("---下载完数据 %d----" % temp)
        q.put(temp)
        time.sleep(1)


def analysis_data(q):
    """数据处理"""
    waitting_analysis_data = list()
    # 从队列中获取数据
    while True:
        time.sleep(1)
        data = q.get()
        print("---拿到下载的数据 %d----" % data)
        waitting_analysis_data.append(data)

        if q.empty():
            break

    # 模拟数据处理
    print(waitting_analysis_data)


def test4():
    # 1. 创建一个队列
    q = multiprocessing.Queue()
    # 2. 创建多个进程，将队列的引用当做实参进行传递到里面
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


# test4()

print('----- 进程池 -----')


def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d" % (msg, os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


def test5():
    pool = multiprocessing.Pool(3)  # 定义一个进程池，最大进程数 3
    for i in range(0, 10):
        # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
        # 每次循环将会用空闲出来的子进程去调用目标
        pool.apply_async(worker, (i,))

    print("----start----")
    pool.close()  # 关闭进程池，关闭后 pool 不再接收新的请求
    pool.join()  # 等待 pool 中所有子进程执行完成，必须放在 close 语句之后
    print("-----end-----")


# test5()

print('----- 多进程拷贝文件夹 -----')


def copy_file(q, file_name, old_folder_name, new_folder_name):
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    # 如果拷贝完了文件，那么就向队列中写入一个消息，表示已经完成
    q.put(file_name)


def test6():
    # 1. 获取用户要 copy 的文件夹的名字
    old_folder_name = input("请输入要copy的文件夹的名字：")

    # 2. 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass

    # 3. 获取文件夹的所有的待 copy 的文件名字  listdir()
    file_names = os.listdir(old_folder_name)

    # 4. 创建进程池
    po = multiprocessing.Pool(5)

    # 5. 创建一个队列
    q = multiprocessing.Manager().Queue()

    # 6. 向进程池中添加 copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))

    po.close()
    # po.join()
    all_file_num = len(file_names)  # 测一下所有的文件个数
    copy_ok_num = 0
    while True:
        file_name = q.get()
        # print("已经完成copy：%s" % file_name)
        copy_ok_num += 1
        print("\r拷贝的进度为：%.2f %%" % (copy_ok_num * 100 / all_file_num), end="")
        if copy_ok_num >= all_file_num:
            break

    print()


test6()
