#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作者:王浩 邮件:bingoogolapple@gmail.com
# 创建时间:2019-05-28
# 描述:

# 导入re模块
import re


class SingleRegularExpression:
    """
    匹配单个字符

    .	匹配任意1个字符（除了\n）
    []	匹配[]中列举的字符
    \d	匹配数字，即 0-9
    \D	匹配非数字，即不是数字
    \s	匹配空白，即空格、tab 键
    \S	匹配非空白
    \w	匹配单词字符，即 a-z、A-Z、0-9、_
    \W	匹配非单词字符
    """

    def __init__(self):
        pass

    @staticmethod
    def test1():
        # 使用 match 方法能够匹配出以 xxx 开头的字符串，re.match(正则表达式,要匹配的字符串)
        result = re.match('BGA', 'BGA=>bingo googol appleBGA')

        # 如果上一步匹配到数据的话，可以使用group方法来提取数据
        print(result)
        if result:
            print(result.group())  # BGA

    @staticmethod
    def test2():
        ret = re.match('.', 'M')
        print(ret.group())  # M
        ret = re.match('t.o', 'too')
        print(ret.group())  # too
        ret = re.match('t.o', 'two')
        print(ret.group())  # two

    @staticmethod
    def test3():
        # 如果hello的首字符小写，那么正则表达式需要小写的h
        ret = re.match('h', 'hello Python')
        print(ret.group())  # h

        # 如果hello的首字符大写，那么正则表达式需要大写的H
        ret = re.match('H', 'Hello Python')
        print(ret.group())  # H

        # 大小写h都可以的情况
        ret = re.match('[hH]', 'hello Python')
        print(ret.group())  # h
        ret = re.match('[hH]', 'Hello Python')
        print(ret.group())  # H
        ret = re.match('[hH]ello Python', 'Hello Python')
        print(ret.group())  # Hello Python

        # 匹配0到9第一种写法
        ret = re.match('[0123456789]Hello Python', '7Hello Python')
        print(ret.group())  # 7Hello Python

        # 匹配0到9第二种写法
        ret = re.match('[0-9]Hello Python', '7Hello Python')
        print(ret.group())  # 7Hello Python

        ret = re.match('[0-35-9]Hello Python', '7Hello Python')
        print(ret.group())  # 7Hello Python

        # 下面这个正则不能够匹配到数字 4，因此 ret 为 None
        ret = re.match('[0-35-9]Hello Python', '4Hello Python')
        if ret:
            print(ret.group())

    @staticmethod
    def test4():
        # 普通的匹配方式
        ret = re.match('嫦娥1号', '嫦娥1号发射成功')
        print(ret.group())  # 嫦娥1号

        ret = re.match('嫦娥2号', '嫦娥2号发射成功')
        print(ret.group())  # 嫦娥2号

        # 使用\d进行匹配
        ret = re.match('嫦娥\d号', '嫦娥1号发射成功')
        print(ret.group())  # 嫦娥1号

        ret = re.match('嫦娥\d号', '嫦娥2号发射成功')
        print(ret.group())  # 嫦娥2号

        # 使用 \s 匹配单个空白字符
        ret = re.match('嫦娥\s号', '嫦娥 号发射成功')
        print(ret)  # 嫦娥 号


class MultiRegularExpression:
    """
    匹配多个字符

    *	匹配前一个字符出现0次或者无限次，即可有可无
    +	匹配前一个字符出现1次或者无限次，即至少有1次
    ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
    {m}	匹配前一个字符出现m次
    {m,n}	匹配前一个字符出现从m到n次
    """

    def __init__(self):
        pass

    @staticmethod
    def test1():
        """匹配出一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无"""
        ret = re.match('[A-Z][a-z]*', 'a')  # 不能够匹配到第一个大写字母，因此 ret 为 None
        if ret:
            print(ret.group())

        ret = re.match('[A-Z][a-z]*', 'M')
        print(ret.group())  # M

        ret = re.match('[A-Z][a-z]*', 'MnnM')
        print(ret.group())  # Mnn

        ret = re.match('[A-Z][a-z]*', 'Aabcdef')
        print(ret.group())  # Aabcdef

    @staticmethod
    def test2():
        """匹配出变量名是否有效"""
        # names = ['name1', '_name', '2_name', '__name__']
        names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123", "__________"]
        for name in names:
            """
            ^ 规定开头，$ 规定结尾
            Python 中的 match 默认是从头开始判断的，所以在 match 中可以不写 ^
            但是 match 不会判断结尾，所以当需要以 xxx 结尾的时候 还需要写上 $

            如果在正则表达式中需要用到了某些普通的字符，比如 . 比如 ? 等，仅仅需要在他们前面添加一个反斜杠进行转义
            """

            # ret = re.match('[a-zA-Z_]+[\w]*', name)
            # ret = re.match('^[a-zA-Z_]+[\w]*$', name)
            # ret = re.match('[a-zA-Z_][a-zA-Z0-9_]*', name)
            ret = re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', name)
            if ret:
                print("变量名:%s 符合要求....通过正则匹配出来的数据是:%s" % (name, ret.group()))
            else:
                print("变量名:%s 不符合要求...." % name)

    @staticmethod
    def test3():
        """匹配出 0 到 99 之间的数字"""
        ret = re.match('[1-9]?[0-9]', '7')
        print(ret.group())  # 7

        ret = re.match('[1-9]?\d', '33')
        print(ret.group())  # 33

        ret = re.match('[1-9]?\d', '09')
        print(ret.group())  # 0    这个结果并不是想要的，利用 $ 才能解决

        ret = re.match('[1-9]?\d$', '09')
        if ret:
            print(ret.group())  # 不能够匹配到第一个为非零数字，因此 ret 为 None

    @staticmethod
    def test4():
        """匹配出 8 到 20 位的密码，可以是大小写英文字母、数字、下划线"""
        # 往多的匹配，一直匹配到满足条件的最大长度
        ret = re.match('[a-zA-Z0-9_]{6}', '12a3g45678')
        print(ret)
        print(ret.group())  # 12a3g4

        ret = re.match('[a-zA-Z0-9_]{8,20}', '1ad12f23s34455ff66')
        print(ret.group())  # 1ad12f23s34455ff66

    @staticmethod
    def test5():
        """
        ^ 规定开头，$ 规定结尾
        Python 中的 match 默认是从头开始判断的，所以在 match 中可以不写 ^
        但是 match 不会判断结尾，所以当需要以 xxx 结尾的时候 还需要写上 $
        
        如果在正则表达式中需要用到了某些普通的字符，比如 . 比如 ? 等，仅仅需要在他们前面添加一个反斜杠进行转义
        """
        email_list = ['xiaoWang@163.com', 'xiaoWang@163.comheihei', '.com.xiaowang@qq.com']
        for email in email_list:
            # ret = re.match('[a-zA-Z_0-9]{4,20}@163\.com$', email)
            ret = re.match('[\w]{4,20}@163\.com$', email)
            if ret:
                print('%s 是符合规定的邮件地址,匹配后的结果是:%s' % (email, ret.group()))
            else:
                print('%s 不符合要求' % email)


class GroupRegularExpression:
    """
    匹配分组

    |	匹配左右任意一个表达式
    (ab)	将括号中字符作为一个分组
    \num	引用分组num匹配到的字符串
    (?P<name>)	分组起别名
    (?P=name)	引用别名为name分组匹配到的字符串
    """

    def __init__(self):
        pass

    @staticmethod
    def test1():
        """匹配出 0-100 之间的数字"""
        ret = re.match('[1-9]?\d', '8')
        print(ret.group())  # 8

        ret = re.match('[1-9]?\d', '78')
        print(ret.group())  # 78

        # 不正确的情况
        ret = re.match('[1-9]?\d', '08')
        print(ret.group())  # 0

        # 修正之后的
        ret = re.match('[1-9]?\d$', '08')
        if ret:
            print(ret.group())
        else:
            print('不在 0-100 之间')

        # 添加 | 或
        ret = re.match('[1-9]?\d$|100', '8')
        print(ret.group())  # 8

        ret = re.match('[1-9]?\d$|100', '78')
        print(ret.group())  # 78

        ret = re.match('[1-9]?\d$|100', '08')
        if ret:
            print(ret.group())
        else:
            print('不在 0-100 之间')

        ret = re.match('[1-9]?\d$|100', '100')
        print(ret.group())  # 100

    @staticmethod
    def test2():
        """匹配出163、126、qq邮箱"""
        ret = re.match('\w{4,20}@(163|126|qq)\.com', 'test@163.com')
        print(ret.group())  # test@163.com

        ret = re.match('\w{4,20}@(163|126|qq)\.com', 'test@126.com')
        print(ret.group())  # test@126.com

        ret = re.match('\w{4,20}@(163|126|qq)\.com', 'test@qq.com')
        print(ret.group())  # test@qq.com

        ret = re.match('\w{4,20}@(163|126|qq)\.com', 'test@gmail.com')
        if ret:
            print(ret.group())
        else:
            print('不是 163、126、qq 邮箱')  # 不是 163、126、qq 邮箱

    @staticmethod
    def test3():
        """匹配不是以 4、7 结尾的手机号码(11 位)"""
        tels = ['13100001234', '18912344321', '10086', '18800007777']
        for tel in tels:
            ret = re.match('1\d{9}[0-35-68-9]', tel)
            if ret:
                print(ret.group())
            else:
                print('%s 不是想要的手机号' % tel)

    @staticmethod
    def test4():
        """提取区号和电话号码"""
        ret = re.match('([^-]*)-(\d+)', '010-12345678')  # TODO
        print(ret)  # <_sre.SRE_Match object; span=(0, 12), match='010-12345678'>
        print(ret.group())  # 010-12345678
        print(ret.group(0))  # 010-12345678
        print(ret.group(1))  # 010
        print(ret.group(2))  # 12345678

    @staticmethod
    def test5():
        """匹配出<html>hh</html>"""
        # 能够完成对正确的字符串的匹配
        ret = re.match('<[a-zA-Z]+>\w+</[a-zA-Z]+>', '<html>hh</html>')
        print(ret.group())  # <html>hh</html>

        # 如果遇到非正常的 html 格式字符串，匹配出错
        ret = re.match('<[a-zA-Z]+>\w+</[a-zA-Z]+>', '<html>hh</htmlbalabala>')
        print(ret.group())  # <html>hh</htmlbalabala>

        # 正确的理解思路：如果在第一对<>中是什么，按理说在后面的那对<>中就应该是什么

        """
        通过 \数字 引用分组中匹配到的数据即可，但是要注意是元字符串，即类似 r"" 这种格式
        第一个组是 \1，第二个组时 \2，以此类推
        """
        ret = re.match(r'<([a-zA-Z]+)>\w+</\1>', '<html>hh</html>')
        print(ret.group())  # <html>hh</html>

        # 因为两对 <> 中的数据不一致，所以没有匹配出来
        test_label = '<html>hh</htmlbalabala>'
        ret = re.match(r'<([a-zA-Z]*)>\w+</\1>', test_label)
        if ret:
            print(ret.group())
        else:
            print('%s 这是一对不正确的标签' % test_label)  # <html>hh</htmlbalabala> 这是一对不正确的标签

    @staticmethod
    def test6():
        """通过「\数字 引用分组的方式」匹配出 <html><h1>www.bingoogolapple.cn</h1></html>"""
        labels = ['<html><h1>www.bingoogolapple.cn</h1></html>', '<html><h1>www.bingoogolapple.cn</h2></html>']
        for label in labels:
            """
            通过 \数字 引用分组中匹配到的数据即可，但是要注意是元字符串，即类似 r"" 这种格式
            第一个组是 \1，第二个组时 \2，以此类推
            """
            ret = re.match(r'<([a-zA-Z]+)><(\w+)>.+</\2></\1>', label)
            if ret:
                print('%s 是符合要求的标签' % ret.group())
            else:
                print('%s 不符合要求' % label)

    @staticmethod
    def test7():
        """通过「(?P<name>) (?P=name) 引用分组的方式」匹配出 <html><h1>www.bingoogolapple.cn</h1></html>"""
        labels = ['<html><h1>www.bingoogolapple.cn</h1></html>', '<html><h1>www.bingoogolapple.cn</h2></html>']
        for label in labels:
            ret = re.match(r'<(?P<name1>[a-zA-Z]+)><(?P<name2>\w+)>.+</(?P=name2)></(?P=name1)>', label)
            if ret:
                print('%s 是符合要求的标签' % ret.group())
            else:
                print('%s 不符合要求' % label)


class AdvancedRegularExpression:
    def __init__(self):
        pass

    @staticmethod
    def test1():
        address = 'c:\\a\\b\\c'
        print(address)  # c:\a\b\c
        # Python 中字符串前面加上 r 表示原生字符串
        r_address = r'c:\\a\\b\\c'
        print(r_address)  # c:\\a\\b\\c

        """
        与大多数编程语言相同，正则表达式里使用 \ 作为转义字符，这就可能造成反斜杠困扰。
        假如你需要匹配文本中的字符 \，那么使用编程语言表示的正则表达式里将需要 4 个反斜杠 \，前两个和后两个分别用于在编程语言里转义成反斜杠，转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。
        """
        print(re.match('c:\\\\', address).group())  # c:\
        print(re.match('c:\\\\a', address).group())  # c:\a
        print(re.match('c:\\\\\\\\', r_address).group())  # c:\\
        print(re.match('c:\\\\\\\\a', r_address).group())  # c:\\a
        # Python 里的原生字符串很好地解决了这个问题，有了原生字符串，你再也不用担心是不是漏写了反斜杠，写出来的表达式也更直观
        print(re.match(r'c:\\a', address).group())  # c:\a
        print(re.match(r'c:\\\\a', r_address).group())  # c:\\a

    @staticmethod
    def test2():
        """匹配出文章阅读的次数"""
        ret = re.search(r'\d+', '阅读次数为 9999')
        print(ret)  # <_sre.SRE_Match object; span=(6, 10), match='9999'>
        print(ret.group())  # 9999

    @staticmethod
    def test3():
        """统计出 Python、C、C++ 相应文章阅读的次数"""
        ret = re.findall(r'\d+', 'Python = 9999, C = 7890, C++ = 12345')
        print(ret)  # ['9999', '7890', '12345']
        ret = re.findall(r'\d+', 'Python = , C = , C++ = ')
        print(ret)  # []

    @staticmethod
    def add(temp):
        str_num = temp.group()
        num = int(str_num) + 1
        return str(num)

    @staticmethod
    def test4():
        """将匹配到的阅读次数加 1"""
        ret = re.sub(r"\d+", '998', "Python = 997")
        print(ret)  # 998

        ret = re.sub(r"\d+", AdvancedRegularExpression.add, "Python = 9")
        print(ret)  # 10

        ret = re.sub(r"\d+", AdvancedRegularExpression.add, "Python = 99")
        print(ret)  # 100

    @staticmethod
    def test5():
        """从下面的字符串中取出文本"""
        text = """<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div>"""
        print(re.sub(r"<[^>]*>|&nbsp;|\n", "", text))  # TODO

    @staticmethod
    def test6():
        """split 根据匹配进行切割字符串，并返回一个列表。切割字符串 info:xiaoZhang 33 shandong"""
        ret = re.split(r':| ', 'info:xiaoZhang 33 shandong')
        print(ret)  # ['info', 'xiaoZhang', '33', 'shandong']
        ret = re.split(r':|\s', 'info:xiaoZhang 33 shandong')
        print(ret)  # ['info', 'xiaoZhang', '33', 'shandong']

    @staticmethod
    def test7():
        """
        非贪婪操作符「?」，这个操作符可以用在「*、+、?」的后面，使贪婪变成非贪婪，要求正则匹配的越少越好
        """
        s = "This is a number 234-235-22-423"
        # 「.+」会从字符串的启始处抓取满足模式的最长字符，其中包括我们想得到的第一个整型字段的中的大部分
        # 「\d+」只需一位字符就可以匹配，所以它匹配了数字 4，而「.+」则匹配了从字符串起始到这个第一位数字 4 之前的所有字符
        r = re.match('(.+)(\d+-\d+-\d+-\d+)', s)
        print(r.group(1))  # 「This is a number 23」
        print(r.group(2))  # 4-235-22-423

        r = re.match('(.+?)(\d+-\d+-\d+-\d+)', s)
        print(r.group(1))  # 「This is a number 」
        print(r.group(2))  # 234-235-22-423

        print(re.match(r'aa(\d+)', 'aa2343ddd').group(1))  # 2343
        print(re.match(r'aa(\d+?)', 'aa2343ddd').group(1))  # 2
        print(re.match(r'aa(\d+)ddd', 'aa2343ddd').group(1))  # 2343
        print(re.match(r'aa(\d+?)ddd', 'aa2343ddd').group(1))  # 2343

        img_tag = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'
        # https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg
        print(re.search(r'https://.+?\.jpg', img_tag).group())
        # https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg
        print(re.search(r'https://.+\.jpg', img_tag).group())


# SingleRegularExpression.test1()
# SingleRegularExpression.test2()
# SingleRegularExpression.test3()
# SingleRegularExpression.test4()


# MultiRegularExpression.test1()
# MultiRegularExpression.test2()
# MultiRegularExpression.test3()
# MultiRegularExpression.test4()
# MultiRegularExpression.test5()

# GroupRegularExpression.test1()
# GroupRegularExpression.test2()
# GroupRegularExpression.test3()
# GroupRegularExpression.test4()
# GroupRegularExpression.test5()
# GroupRegularExpression.test6()
# GroupRegularExpression.test7()

# AdvancedRegularExpression.test1()
# AdvancedRegularExpression.test2()
# AdvancedRegularExpression.test3()
# AdvancedRegularExpression.test4()
# AdvancedRegularExpression.test5()
# AdvancedRegularExpression.test6()
AdvancedRegularExpression.test7()
