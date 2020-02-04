""" 
    ！！！ 运行前必读 ！！！
 
    （1） 该方法会把文件按序号重命名：001、002、003 ……
   
    （2） 确保把文件放入Rename文件夹，并命名为 1(1)、1(2)、1(3) …… 形式 
	
	（3） 确保文件的后缀正确（line 14 设置后缀）
"""

import os

# 设置参数
path = 'E:\\Other\\Downloads\\Rename\\'   # 文件路径
postfix = '.flv'  # 设置文件后缀

# 主程序
filenames = os.listdir(path)  # 提取路径下的所有文件名
if filenames[0][0:5] == '1 (1)':  # 确认文件是否重命名为 1(1)、2(2) …… 形式
    for name in filenames:
        oldname = path + name
        if oldname[len(path) + 5] == '.':
            newname = path + '00' + oldname[len(path)+3:len(path)+4] + postfix
            os.rename(oldname, newname)
        if oldname[len(path) + 6] == '.':
            newname = path + '0' + oldname[len(path)+3:len(path)+5] + postfix
            os.rename(oldname, newname)
        if oldname[len(path) + 7] == '.':
            newname = path + oldname[len(path)+3:len(path)+6] + postfix
            os.rename(oldname, newname)
    print('Done')
else:
    print('请先重命名！')