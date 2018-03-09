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