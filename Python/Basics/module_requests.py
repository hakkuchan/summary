""" · 目录
    |
    |—— 1. get()操作
    |   |
    |   |—— 1.1 status_code
    |   |
    |   |—— 1.2 ~ 1.3 text, content
    |   |
    |   |—— 1.4 ~ 1.5 encoding, apparent_encoding
    |   |
    |   |—— 1.6 爬取网页的通用框架
    |
    |—— 2. 技巧
    |   |
    |   |—— 2.1 反来源审查
    |   |
    |   |—— 2.2 爬取图片
    |   |
    |   |—— 2.3 关键字搜索
"""

import requests
import os

""" 1. get()操作 """
r = requests.get('https://www.baidu.com/')  # 请求获取网页Response对象
print(type(r))  # >>> 'requests.models.Response'

''' 1.1 status_code：http请求的返回状态 '''
print(r.status_code)
# status_code 状态码：
# 200-请求成功；
# 1开头-被接受，需要继续处理； 
# 3开头-请求被重定向；
# 4开头-请求错误；
# 5开头-服务器错误
r.raise_for_status() # 判断请求是否正常，如正常，返回200

''' 1.2 text：页面内容（字符串形式） '''
print(r.text)

''' 1.3 content: 页面内容的二进制形式 '''
print(r.content)

''' 1.4 encoding：从HTTP header猜测的响应内容编码方式 '''
print(r.encoding)

# 更改编码方式 1：
r.encoding = 'utf-8'
print(r.text)  # 乱码 → 中文

# 更改编码方式 2：
print(r.content.decode('utf-8'))
# 注意：r.text.decode('utf-8')会报错，因为 r.text 返回值是字符串

''' 1.5 apparent_encoding: 从内容中分析出的响应内容编码方式 '''
print(r.apparent_encoding)

''' 1.6 爬取网页的通用框架 '''
def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 判断请求是否正常，如否，执行except
                              # 使用 r.raise_for_status() 可以避免 if r.status_code == 200 条件句
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return r.status_code
url = 'https://www.baidu.com/'
print(get_html_text(url))



""" 2. 技巧 """

''' 2.1 反来源审查
    
    · 某些网站会检查来访 HTTP 协议头的 User‐Agent 域（即"来源审查"）
      只响应浏览器或友好爬虫的访问
    · 反来源审查方法：修改User‐Agent
'''
url = 'https://movie.douban.com/top250'  # 豆瓣电影排行网页
r = requests.get(url)
print(r.request.headers)  # >>> {'User-Agent': 'python-requests/2.22.0' …… } 说明我们在用爬虫访问
print(r.status_code)      #  由于豆瓣网站进行了来源审查，因此无法访问
# 修改 User-Agent:
kv = {'user-agent': 'Chrome 79.0'}  # 设置字典，其中 'Chrome 79.0'为浏览器版本
r = requests.get(url, headers=kv)   # 替换 headers 中 User-Agent
print(r.status_code)  # >>> 200  访问正常


''' 2.2 爬取图片 '''
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
    if not os.path.exists(folder):  # 检查文件夹是否存在
        os.mkdir(folder)  # 创建文件夹路径
    if not os.path.exists(path):  # 确保没有重名文件
        r = requests.get(pic_url) # 访问 url 对应的数据资源
        with open(path, 'wb') as f: # 以二进制形式打开完整文件路径
            f.write(r.content)  # 把图片的二进制数据写入上述路径
            f.flush()  # 清理图片缓存
        print('Done')
    else:
        print('包含重名文件')  # 如果已有重名文件，返回提醒 
except:
    print(f'Fail: {r.status_code}')  # 爬取图片失败

    
''' 2.3 关键字搜索
    
    · 搜索引擎通常有关键字接口，例如
      百度：http://www.baidu.com/s?wd=keyword
      其中，keyword是关键字
    · 利用 params 可设定关键字
'''
url = "http://www.baidu.com/s?"
kv = {'wd': 'Python'}  # 设定关键字字典
r = requests.get(url, params=kv)  # 利用 params 修改关键字
print(r.status_code)