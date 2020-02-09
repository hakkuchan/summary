""" 1. 该方法会把同级目录下rename文件夹中的文件按序号重命名：001、002、003 ……   
    2. 运行前，先把文件放入Rename文件夹，并命名为 1(1)、1(2)、1(3) …… 形式 
"""

import os

path = os.getcwd() + '\\rename\\'
filenames = os.listdir(path)  # 获取全部文件路径
if filenames[0][0:5] == '1 (1)':  # 确认文件是否重命名为 1(1)、2(2) …… 形式
    oldnames = [path + name for name in filenames]
    postfix = oldnames[0][oldnames[0].index('.'):]
    for oldname in oldnames:
        num = int(oldname[oldname.index('(')+1:oldname.index(')')]) - 1
        if 0 <= num < 10:
            newname = path + '00' + str(num) + postfix
            os.rename(oldname, newname)
        elif 10 <= num < 100:
            newname = path + '0' + str(num) + postfix
            os.rename(oldname, newname)
        elif 100 <= num < 1000:
            newname = path + str(num) + postfix
            os.rename(oldname, newname)
    print('Complete')
else:
    print('请先重命名！')