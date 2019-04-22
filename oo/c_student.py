#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-05
# 描述:

from oo.c_human import Human


class Student(Human):

    def __init__(self, school, name, age):
        self.school = school
        # 不建议用这种。Python 2.x 不支持 super() 时使用，Python 3.x 中建议使用 super(). 调用父类方法
        # Human.__init__(self, name, age)

        # super(Student, self).__init__(name, age)
        super().__init__(name, age)  # 使用 super(). 调用原本在父类中封装的方法
        print('执行了 Student 的 __init__ 方法')  # 执行了 Student 的 __init__ 方法 我是全局变量

        # 两个下划线 __ 开头的变量为私有变量
        self.__grade = 0

    def update_grade(self, grade):
        if grade < 0:
            self.__grade = 0
        else:
            self.__grade = grade

    def test1(self):
        print('子类 test1')
        # 不建议用这种。Python 2.x 不支持 super() 时使用，Python 3.x 中建议使用 super(). 调用父类方法
        # Human.test1(self)

        # super(Student, self).test1()
        super().test1()  # 使用 super(). 调用原本在父类中封装的方法


def oop_test0():
    print('----- print_type -----')
    print(Human)  # <class 'oo.human.Human'>
    print(Student)  # <class '__main__.Student'>
    print(type(Human))  # <class 'type'>
    print(type(Student))  # <class 'type'>


def oop_test1():
    print('----- oop_test1 -----')
    student1 = Student('学校名字', 'BGA', 27)
    print(student1)  # <__main__.Student object at 0x10c13d080>
    # 访问实例变量
    print(student1.name, student1.age)  # BGA 27
    student1.test1()  # test1 BGA 27 我是全局变量
    Student.test1(student1)  # test1 BGA 27 我是全局变量


def oop_test2():
    print('----- oop_test2 -----')
    student1 = Student('学校名字', 'BGA', 27)
    # 实例的 __dict__ 包含了所有实例变量
    print(student1.__dict__)  # {'name': 'BGA', 'age': 27, '_Student__grade': 0}
    # 间接操作私有变量，不建议这样做
    student1._Student__grade = 2
    print(student1._Student__grade)
    print(student1.__dict__)  # {'name': 'BGA', 'age': 27, '_Student__grade': 2}
    # 类的 __dict__ 包含了类变量、方法
    # {'__module__': '__main__', '__init__': <function Student.__init__ at 0x1100b4158>, 'update_grade': <function Student.update_grade at 0x1100b4840>, '__doc__': None}
    print(Student.__dict__)


def oop_test3():
    print('----- oop_test3 -----')
    student1 = Student('学校名字', 'BGA', 27)
    # 类访问类变量
    print(Student.name)  # bingoogolapple
    # 调用类方法
    student1.test2()
    Student.test2()
    # 调用静态方法
    student1.test3()
    Student.test3()


oop_test0()
oop_test1()
oop_test2()
oop_test3()
