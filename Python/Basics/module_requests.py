""" · 目录
    |
	|—— 1. HTTP协议
	|
	|—— 2. get()操作
	|   |
	|   |—— 2.1 status_code
	|	|
	|	|—— 2.2~2.3 text, content
	|	|
	|	|—— 2.4~2.5 encoding, apparent_encoding
	|	|
	|	|—— 2.6 爬取网页的通用框架
	|
    |—— 3. 技巧
        |
        |—— 3.1 来源审查的破解
        |
        |—— 3.2 搜索关键词
        |
        |—— 3.3 抓取图片		
"""


import requests
import os


""" 1. HTTP协议
    
    · HTTP (Hypertext Transfer Protocol)，超文本传输协议，有3个要点：
      (1) 请求-响应模式
      (2) 无状态（表示不同操作之间不会相互影响）
      (3) 采用URL定位网络资源
      
    · HTTP协议对资源的操作（注：操作独立无状态）
      Get：请求获取URL位置的资源
      HEAD：请求获取URL位置资源的头部信息
      POST：请求向URL位置的资源后附加新的数据（不改变原数据）
      PUT：请求向URL位置存储一个资源，覆盖原URL位置的资源
      PATCH：请求局部更新URL位置的资源，即改变该处资源的部分内容
      DELETE：请求删除URL位置存储的资源
"""



""" 2. get()操作 """
r = requests.get('https://www.baidu.com/')  # 请求获取网页Response对象
print(type(r))  # >>> 'requests.models.Response'


''' 2.1 status_code：http请求的返回状态 '''
print(r.status_code)
# status_code 状态码：
# 200-请求成功；
# 1开头-被接受，需要继续处理； 
# 3开头-请求被重定向；
# 4开头-请求错误；
# 5开头-服务器错误

r.raise_for_status() # 判断请求是否正常，如正常，返回200


''' 2.2 text：页面内容（字符串形式） '''
print(r.text)


''' 2.3 content: 页面内容的二进制形式 '''
print(r.content)


''' 2.4 encoding：从HTTP header猜测的响应内容编码方式 '''
print(r.encoding)
# 更改编码方式：
r.encoding = 'utf-8'
print(r.text)  # 乱码 → 中文


''' 2.5 apparent_encoding: 从内容中分析出的响应内容编码方式 '''
print(r.apparent_encoding)


''' 2.6 爬取网页的通用框架 '''
def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 判断请求是否正常，如否，执行except
                              # 使用 r.raise_for_status() 可以避免 if r.status_code == 200 条件句
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '异常'
url = 'https://www.baidu.com/'
print(get_html_text(url))



""" 3. 技巧 """

''' 3.1 来源审查的破解 
    
    · 某些网站会进行来源审查，即检查来访 HTTP 协议头的 User‐Agent 域，
      只响应浏览器或友好爬虫的访问
    · 破解方法：修改 User‐Agent
'''
url = 'https://www.amazon.cn/'
r = requests.get(url)
print(r.request.headers)  # >>> {'User-Agent': 'python-requests/2.22.0' …… } 说明我们在用爬虫访问
print(r.status_code)  #  由于亚马逊网站进行了来源审查，因此访问异常
# 修改 User-Agent
kv = {'user-agent': 'Chrome 79.0'}  # 设置字典，其中 'Chrome 79.0'为浏览器版本
r = requests.get(url, headers=kv)   # 替换 headers 中 User-Agent
print(r.status_code)  # >>> 200  访问正常


''' 3.2 搜索关键词
    
    · 搜索引擎通常有关键词接口，例如
      百度：http://www.baidu.com/s?wd=keyword
      其中，keyword是关键词
    · 利用 params 可设定关键词
'''
url = "http://www.baidu.com/s?"
kv = {'wd': 'Python'}  # 设定关键词字典
r = requests.get(url, params=kv)
print(r.status_code)


''' 3.3 爬取图片 (需要requests和os) '''
# 图片的 url 一般以 .jpg 结尾
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
    print('Fail')  # 提取图片失败