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
"""


import requests


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
        return '异常'
url = 'https://www.baidu.com/'
print(get_html_text(url))