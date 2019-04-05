#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-04-05
# 描述:

from oo.human import Human


class Student(Human):

    def __init__(self, school, name, age):
        self.school = school
        # 不建议用这种
        # Human.__init__(self, name, age)
        # 建议用这种方式调父类的构造方法
        super(Student, self).__init__(name, age)
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
        super(Student, self).test1()


print(Human)  # <class 'oo.human.Human'>
print(Student)  # <class '__main__.Student'>
print(type(Human))  # <class 'type'>
print(type(Student))  # <class 'type'>

print('-------------------------------------------')

student1 = Student('学校名字', 'BGA', 27)
print(student1)  # <__main__.Student object at 0x10c13d080>
# 访问实例变量
print(student1.name, student1.age)  # BGA 27
student1.test1()  # test1 BGA 27 我是全局变量
Student.test1(student1)  # test1 BGA 27 我是全局变量
# 类访问类变量
print(Student.name)  # bingoogolapple

print('-------------------------------------------')

# 实例的 __dict__ 包含了所有实例变量
print(student1.__dict__)  # {'name': 'BGA', 'age': 27, '_Student__grade': 0}
# 间接操作私有变量，不建议这样做
student1._Student__grade = 2
print(student1._Student__grade)
print(student1.__dict__)  # {'name': 'BGA', 'age': 27, '_Student__grade': 2}
# 类的 __dict__ 包含了类变量、方法
# {'__module__': '__main__', '__init__': <function Student.__init__ at 0x1100b4158>, 'update_grade': <function Student.update_grade at 0x1100b4840>, '__doc__': None}
print(Student.__dict__)

print('-------------------------------------------')

# 调用类方法
student1.test2()
Student.test2()
# 调用静态方法
student1.test3()
Student.test3()
