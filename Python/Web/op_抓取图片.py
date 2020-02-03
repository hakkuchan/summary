""" 爬取图片 """

import requests
import os

# 图片资源的 url 一般以 .jpg 结尾
pic_url = 'https://pic4.zhimg.com/v2-45ed9cc0da397cbbfb8d3450c8c9cbfe_1200x500.jpg'

# 设置文件夹路径
folder = 'E:\\Other\\Downloads\\Pic\\'

# 设置图片名
name = 'p.jpg'

# 设置完整文件路径
path = folder + name

# 主程序
try:
    if not os.path.exists(folder):
        os.mkdir(folder)  # 创建文件夹路径
    if not os.path.exists(path):    # 确保没有重名文件
        r = requests.get(pic_url)   # 访问 url 对应的数据资源
        with open(path, 'wb') as f: # 以二进制形式打开完整文件路径
            f.write(r.content)  # 把图片的二进制数据写入上述路径
        print('Done')
    else:
        print('File has existed')   # 如果已有重名文件，返回提醒 
except:
    print('Fail')  # 爬取图片失败