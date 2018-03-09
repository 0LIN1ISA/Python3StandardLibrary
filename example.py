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
os.chdir('C:\\'')
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
