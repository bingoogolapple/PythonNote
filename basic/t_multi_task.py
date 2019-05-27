#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-05-27
# 描述:

import time
from greenlet import greenlet
from urllib import request
import gevent

# 打补丁后使用 gevent 时就可以直接用 time.sleep
gevent.monkey.patch_all()


def yield_task1():
    while True:
        print("--- yield_task1 ---")
        time.sleep(0.1)
        yield


def yield_task2():
    while True:
        print("--- yield_task2 ---")
        time.sleep(0.1)
        yield


def test_yield_multi_task():
    t1 = yield_task1()
    t2 = yield_task2()
    # 先让 yield_task_1 运行一会，当 yield_task_1 中遇到 yield 的时候，再返回到 next(t1) 末尾
    # 然后执行 yield_task_2，当它遇到 yield 的时候，再次切换到 yield_task_1 中，这样 t1/t2/t1/t2 的交替运行，最终实现了多任务，协程
    while True:
        next(t1)
        next(t2)


# test_yield_multi_task()

class TestGreenlet:
    def __init__(self):
        self.gr1 = greenlet(self.greenlet_task1)
        self.gr2 = greenlet(self.greenlet_task2)
        # 切换到 gr1 中运行
        self.gr1.switch("main 传递的")

    def greenlet_task1(self, param):
        while True:
            print("--- greenlet_task1 ---", param)
            self.gr2.switch("task1传递的")
            time.sleep(0.5)

    def greenlet_task2(self, param):
        while True:
            print("--- greenlet_task2 ---", param)
            self.gr1.switch("task2传递的")
            time.sleep(0.5)


# TestGreenlet()


class TestGevent:
    def __init__(self):
        print("----1---")
        self.g1 = gevent.spawn(self.f1, 5)
        print("----2---")
        self.g2 = gevent.spawn(self.f2, 5)
        print("----3---")
        self.g3 = gevent.spawn(self.f3, 5)
        print("----4---")
        self.g1.join()
        self.g2.join()
        self.g3.join()

    def f1(n):
        for i in range(n):
            print(gevent.getcurrent(), i)
            # gevent.sleep(0.5)
            time.sleep(0.5)

    def f2(n):
        for i in range(n):
            print(gevent.getcurrent(), i)
            # gevent.sleep(0.5)
            time.sleep(0.5)

    def f3(n):
        for i in range(n):
            print(gevent.getcurrent(), i)
            # gevent.sleep(0.5)
            time.sleep(0.5)

    def downloader(img_name, img_url):
        req = request.urlopen(img_url)
        img_content = req.read()

        with open(img_name, "wb") as f:
            f.write(img_content)

    def download(self):
        gevent.joinall([
            gevent.spawn(self.downloader, "1.jpg", "https://avatars3.githubusercontent.com/u/8949716?s=100&v=4"),
            gevent.spawn(self.downloader, "2.jpg", "https://avatars3.githubusercontent.com/u/8949716?s=460&v=4")
        ])

# TestGevent()
