import os # 常见的文件和目录操作

# 文件路径格式
path1 = r'E:\Work\Github\Basics\module_os.py'      # r原始字符串，防止转义
path2 = 'E:/Work/Github/Basics/module_os.py'       # 单个反斜杠：/
path3 = 'E:\\Work\\Github\\Basics\\module_os.py'   # 两个斜杠：\\（第一个\是转义符）
print(path1)
print(path2)
print(path3)

# getcwd() 获取当前工作路径
now_dir = os.getcwd()
print(now_dir)

# os.listdir() 读取路径下所有文件、文件夹名 '''
path = r'E:\Work\Github\Basics'
f = os.listdir(path)
for i in f:
    print(i)

# makedirs() 创建路径
path = r'E:\Work\Jupyter\Data\Test'
if not os.path.exists(path):  # 如果目录不存在
    os.makedirs(path)  # 创建目录
    
# os.path.isdir() 判断某一路径是否是目录 '''
print(os.path.isdir(r'E:\Work\Jupyter'))
print(os.path.isdir(r'E:\Work\Jupyter\trial.ipynb'))

# os.path.isfile() 判断某一路径是否是文件 '''
print(os.path.isfile(r'E:\Work\Jupyter'))
print(os.path.isfile(r'E:\Work\Jupyter\Data\Test\test.txt'))

# os.path.split() 分割目录与文件名
path, filename = os.path.split(r'E:\Work\Jupyter\TEST.ipynb')
print(path, filename)

# os.path.join() 拼接目录 (不能后接文件)
need_dir = os.path.join('E:','Work','Jupyter')
print(need_dir)