# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/10 0:42

# 1. 操作系统接口

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
