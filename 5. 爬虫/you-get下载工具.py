""" 单文件下载 """
# 命令行中输入：
you-get -o E:\Other\Downloads 网址

""" 批量下载 """
# 将下列代码保存在一个 .py 文件 (例如，abc.py)中
# 命令行进入该文件所在目录
# 输入命令：python abc.py
import os
for page in range(124, 179):
    command = 'you-get -o E:\MySQL教程 https://www.bilibili.com/video/av43797709/?p='+str(page)
    os.system(command)
    print('Finished：{}/179'.format(page), end='\r')