""" os 模块 """
# os 封装了常见的文件和目录操作，常用方法：

import os

""" 文件路径 """
path1 = 'E:/Work/Github/1. Python基础/常用模块与操作/模块os.py'       # 单个反斜杠：/
path2 = 'E:\\Work\\Github\\1. Python基础\\常用模块与操作\\模块os.py'  # 两个斜杠：\\（第一个\是转义符）
path3 = r'E:\Work\Github\1. Python基础\常用模块与操作\模块os.py'      # r用于防止字符转义
print(path1)
print(path2)
print(path3)

""" os.getcwd() 获取当前工作路径 """
now_dir = os.getcwd()
print(now_dir)   # >>> E:\Work\Jupyter

""" os.path.join() 拼接目录（不能后接文件） """
need_dir = os.path.join('E:','Work','Jupyter')
print(need_dir)  # >>> E\Work\Jupyter

""" os.path.split() 分割目录与文件名 """
path, filename = os.path.split('E:\Work\Jupyter/trial.ipynb')
print(path, filename)

""" os.path.isdir() 判断某一路径是否是目录 """
print(os.path.isdir('E:\Work\Jupyter'))
print(os.path.isdir('E:\Work\Jupyter/trial.ipynb'))

""" os.path.isfile() 判断某一路径是否是文件 """
print(os.path.isfile('E:\Work\Jupyter'))
print(os.path.isfile('E:\Work\Jupyter/trial.ipynb'))