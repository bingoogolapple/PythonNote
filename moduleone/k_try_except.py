#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-23
# 描述:


class BGAErrorOne(Exception):
    pass


class BGAErrorTwo(Exception):
    def __init__(self, arg1, arg2):
        super().__init__(arg1, arg2)
        self.arg1 = arg1
        self.arg2 = arg2


def input_age():
    # 提示用户输入一个整数
    num = int(input("输入一个整数："))
    # 使用 8 除以用户输入的整数并且输出
    if num > 400:
        raise BGAErrorTwo('参数1', '参数2')
    if num > 300:
        raise BGAErrorOne('自定义无参异常')
    elif num > 200:
        raise Exception('测试抛出异常')
    else:
        result = 8 / num
        return result


try:
    age = input_age()
    print(age)
except ValueError:
    print("请输入正确的整数")
except (ValueError, ZeroDivisionError):
    print("多个异常中的某一个")
except Exception as error:
    print("未知错误 %s：%s" % (type(error), error))
else:
    print("try 里面没报错才会走到这里")
    int(input("输入一个整数测试 else 报错："))
finally:
    print("无论是否出现错误都会执行的代码。try 通过了，else 里报错也会走到 finally 这里")

print("-" * 50)
