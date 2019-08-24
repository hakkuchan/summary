""" os模块包含了常见的文件和目录操作 """

import os

''' 1. 文件路径 '''
path1 = r'E:\Work\Github\1. Python基础\常用模块与操作\模块os.py'      # r原始字符串，防止转义（推荐）
path2 = 'E:/Work/Github/1. Python基础/常用模块与操作/模块os.py'       # 单个反斜杠：/
path3 = 'E:\\Work\\Github\\1. Python基础\\常用模块与操作\\模块os.py'  # 两个斜杠：\\（第一个\是转义符）
print(path1)
print(path2)
print(path3)

''' 2. getcwd() 获取当前工作路径 '''
now_dir = os.getcwd()
print(now_dir)

''' 3. makedirs() 创建路径 '''
path = r'E:\Work\Jupyter\Data\Test'
if not os.path.exists(path):    # 如果目录不存在
    os.makedirs(path)           # 创建目录
    
''' 4. os.path.split() 分割目录与文件名 '''
path, filename = os.path.split(r'E:\Work\Jupyter\Trial.ipynb')
print(path, filename)

''' 5. os.path.join() 拼接目录 (不能后接文件) '''
need_dir = os.path.join('E:','Work','Jupyter')
print(need_dir)

''' 6. os.path.isdir() 判断某一路径是否是目录 '''
print(os.path.isdir(r'E:\Work\Jupyter'))
print(os.path.isdir(r'E:\Work\Jupyter\trial.ipynb'))

''' 7. os.path.isfile() 判断某一路径是否是文件 '''
print(os.path.isfile(r'E:\Work\Jupyter'))
print(os.path.isfile(r'E:\Work\Jupyter\Data\Test\test.txt'))