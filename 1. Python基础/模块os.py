""" os 模块 """
# os 封装了常见的文件和目录操作，常用方法：

import os

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

""" 注意 / 和 \ 的用法：

        上级目录\下级目录
        
        目录 / 文件
"""