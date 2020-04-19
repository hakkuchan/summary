""" os模块：用于操作文件 """

import os

# (1) 文件路径的格式
path1 = r'E:\Work\Github\Basics\module_os.py'    # r原始字符串，防止转义
path2 = 'E:/Work/Github/Basics/module_os.py'     # 单个反斜杠：/
path3 = 'E:\\Work\\Github\\Basics\\module_os.py' # 两个斜杠：\\（第一个\是转义符）
# 文件路径不能以 \ 结尾，会被理解为转义符
print(path1)
print(path2)
print(path3)

# (2) getcwd获取当前工作路径
now_dir = os.getcwd() # cwd: current_work_dir 
print(now_dir)

# (3) listdir读取路径下所有文件和文件夹名 '''
path = r'E:\Work\Github/'
f = os.listdir(path)
for i in f:
    print(i)
    
# (4) makedirs 创建路径
path = r'E:\Work\Jupyter\Data/'
if not os.path.exists(path):  # 如果目录不存在
    os.makedirs(path)  # 创建目录
    
# (5) os.path.isdir 判断某一路径是否是目录 '''
print(os.path.isdir(r'E:\Work\Jupyter'))
print(os.path.isdir(r'E:\Work\Jupyter\trial.ipynb'))

# (6) os.path.isfile 判断某一路径是否是文件 '''
print(os.path.isfile(r'E:\Work\Jupyter'))
print(os.path.isfile(r'E:\Work\Jupyter\Data\Test\test.txt'))

# (7) os.path.split 分割目录与文件名
path, filename = os.path.split(r'E:\Work\Jupyter\TEST.ipynb')
print(path, filename)

# (8) os.path.join 拼接目录 (不能后接文件)
need_dir = os.path.join('E:','Work','Jupyter')
print(need_dir)
