# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/10 0:42

"""
1. 操作系统接口
"""
# os：提供了很多与操作系统交互的函数
import os

# 显示当前工作目录
print(os.getcwd())
# 更改工作目录
os.chdir('C:\\')
# 创建文件夹
os.system('mkdir temp_dir')

# shutil：提供了更高级的文件和目录管理
import shutil

# 复制文件
shutil.copyfile('data.db', 'archive.db')
# 移动文件
shutil.move('/build/executables', 'installdir')

"""
2. 文件通配符
"""
# glob：提供了一个函数用于从目录通配符搜索中生成文件列表
import glob

# 显示当前目录下以py为扩展名的文件
print(glob.glob('*.py'))

"""
3. 命令行参数
"""
# sys:命令行参数存放于sys模块的argv变量中
import sys

print(sys.argv)
# 在命令行中执行 python demo.py one two three
# 输出：['demo.py', 'one', 'two', 'three']

# getopt 模块使用 Unix getopt() 函数处理 sys.argv

"""
4. 错误输出重定向和程序终止
"""
# sys还有stdin,stdout和stderr属性，即使在stdout被重定向时，侯着页可以用于显示警告和错误信息
import sys

sys.stderr.write('Warning, log file not found starting a new one\n')

# 程序终止
sys.exit()

"""
5. 字符串正则表达式
"""
# re：为高级字符串处理提供了正则表达式工具
import re

str_findall = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(str_findall)
str_sub = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(str_sub)

# 简单操作时，可以直接使用字符串方法
my_str = 'tea for too'.replace('too', 'two')
print(my_str)

"""
6. 数学
"""
# math：为浮点运算提供了对底层C函数库的访问
import math

print(math.cos(math.pi / 4.0))
print(math.log(1024, 2))

# random：提供了生成随机数的工具
import random

# 从列表中随机选择一个
print(random.choice(['apple', 'pear', 'banana']))
# 从列表中随机选择10组数字
print(random.sample(range(100), 10))
# 用于生成一个0到1的随机浮点数
print(random.random())
# 随机获取一个整数
print(random.randrange(100))

# SciPy <http://scipy.org> 项目提供了许多数值计算的模块。

"""
7. 互联网访问
"""
# urllib.request：获取网页
from urllib.request import urlopen

for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')
    if 'EST' in line or 'EDT' in line:
        print(line)

# smtplib：发送电子邮件
import smtplib

server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org')
"""
To:jcaesar@example.org
From:soothsayer@example.org

Beware the Ides of March.
"""
server.quit()

"""
8. 日期和时间
"""
# datetime：日期和时间处理同时提供了简单和复杂的方法。

from datetime import date

# 获取今天日期
now = date.today()
print(now)
print(now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'))
birthday = date(1982, 2, 2)
# 比较两个日期
age = now - birthday
# 获取日期相差的天数
print(age.days)

"""
9. 数据压缩
"""
# zlib,gzip,bz2,lzma,zipfile,tarfile：支持通用的数据打包和压缩格式
import zlib

s = b'witch which has which witches wrist watch'
print(len(s))
# 压缩字符串
t = zlib.compress(s)
print(len(t))
# 解压经过压缩的字符串
print(zlib.decompress(t))
# 计算CRC值
print(zlib.crc32(s))

"""
10. 性能和度量
"""
# timeit模块的Timer来度量性能
from timeit import Timer

print(Timer('t=a;a=b;b=t', 'a=1;b=2').timeit())
print(Timer('a,b=b,a', 'a=1;b=2').timeit())

# 相对于 timeit 的细粒度，profile 和 pstats 模块提供了针对更大代码块的时间度量工具。

"""
11. 质量控制
"""


# doctest：提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
# 测试构造如同简单的将它的输出结果剪切并黏贴到文档字符串中。

def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print(average([20,30,70]))
    40.0
    """
    return sum(values) / len(values)


import doctest

print(doctest.testmod(verbose=True))

# unittest：可以在一个独立的文件里提供一个更全面的测试集
import unittest


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)


"""
12. 瑞士军刀
"""
# xmlrpc.client和xmlrpc.server：远程过程调用
# email：一个管理邮件信息的库，包括MIME和其它基于RFC2822的信息文档，不同于smtplib和poplib模块
# email包含了一个构造或者解析复杂消息结构（包括附件）以及实现互联网编码和头协议的完整工具集。
# xml.dom和xml.sax：为流行的信息交换格式提供了强大的支持
# gettext，locale和codecs：对国际化的支持

"""
13. 输出格式
"""
# reprlib：为大型的或深度嵌套的容器缩写显示提供了：repr()函数的一个定制版本
import reprlib

print(set('supercalifragilisticexpialidocious'))
print(reprlib.repr(set('supercalifragilisticexpialidocious')))

# pprint：提供了一种解释器可读的方式深入控制内置和用户自定义对象的打印（美化打印）
import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
print(t)
pprint.pprint(t, width=20)

# textwrap：格式化文本段落以适应特定的屏宽
import textwrap

doc = """
The wrap() method is just like fill() except that it returns 
a list of strings instead of one big string with newlines to separate 
the wrapped lines.
"""
# 文本段落换行宽度为40
print(textwrap.fill(doc, width=40))

# locale：按访问预定好的国家信息数据库，locale的格式化函数属性集提供了一个直接方式以分组标示格式化数字
import locale

print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))

"""
14. 模版
"""
# string提供了一个灵活多变的模版类Template，使用它最终用户可以用简单的进行编辑。
# 格式用$为开头的Python合法标识（数字、字母和下划线）作为占位符。$$创建一个单独$。
from string import Template

t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))
# ...
# Nottinghamfolk send $10 to the ditch fund.

# t.safe_substitute()：当占位符不完整的情况，此函数不会抛出KeyError异常

# 模板子类可以指定一个自定义分隔符

"""
15. 使用二进制数据记录布局
"""
# struct：模块为使用变长的二进制记录格式提供了pack()和unpack()函数。

"""
16. 多线程
"""
# threading：多线程模块
import threading, zipfile


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)


background = AsyncZip('example.py', 'example.zip')
background.start()
print('The main program continues to run in foreground.')
background.join()
print('Main programe waited until background was done.')

"""
17. 日志
"""
# loggin：提供了完整和灵活的日志系统
import logging

logging.debug('Debugging information')
logging.error('Error occurred')

"""
18. 弱引用
"""
# weakref：提供了不用创建引用的跟踪对象工具，一丹对象不再存在，它自动从弱引用上删除并触发回调。

import weakref


class ExpensiveObject:
    def __del__(self):
        print('(Deleting %s' % self)


obj = ExpensiveObject
r = weakref.ref(obj)

print('obj', obj)
print('ref', r)
print('r():', r())

print('deleting obj')
del obj
print('ref', r)
print('r():', r())
# 在这里,由于obj在第二次调用引用之前已经删除，所以ref返回None


import weakref, gc


class A():
    def __init__(self, value):
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)


x = A(3)
y = x
print(x)
del x
print(y)


class B():

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


a = B(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
print(gc.collect())
del a
print(gc.collect())
print(d['primary'])

"""
19. 列表工具
"""
# array：模块提供了一个类似列表的array()对象，它存储数据更为紧凑。
from array import array

a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

# collections：模块提供了类似列表的deque()对象，他从左边添加（append）和弹出(pop)更快。
from collections import deque

d = deque(['task1', 'task2', 'task3'])
d.append('task4')
print(d)
print('Handling', d.popleft())

# heapq：提供了基于正规链表的堆实现。最小的值总是保持在0点。
# 这在希望循环访问最小元素，但是不想执行完整堆排序的时候非常有用。
from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# 以线性时间将一个列表转换为堆
heapify(data)
# 往堆中插入一条新数据-5
heappush(data, -5)
print([heappop(data) for i in range(3)])

"""
20. 十进制浮点数算法
"""
# decimal：模块提供了一个Decimal数据类型用于浮点数计算。
# 相比内置的二进制浮点数实现float，这个类型有助于
# * 金融应用和其他需要精度十进制表达的场合
# * 控制精度
# * 控制舍入以使用法律或者法规要求
# * 确保十进制数位精度
# * 用户希望计算结果与手算相符合的场合。
from decimal import *

print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(.70 * 1.05, 2))
