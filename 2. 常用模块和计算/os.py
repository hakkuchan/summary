""" os 模块 """
# os 封装了常见的文件和目录操作，常用方法：

import os

""" 获取当前工作路径 """
now_dir = os.getcwd()
print(now_dir)

""" 拼接目录 """
need_dir = os.path.join('E','Work','Github','笔记.txt')
print(need_dir)

""" 分割目录与文件名 """
path, filename = os.path.split(need_dir)
print(path, filename)

""" 判断某一路径是否是目录 """
print(os.path.isdir(now_dir))  # 是目录
print(os.path.isdir(need_dir)) # 不是目录