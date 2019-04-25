#coding=utf-8
import requests

""" 请求 """
html = requests.get('https://maoyan.com/board/4')
print(html.status_code)
# status_code 状态码：
# 1开头-被接受，需要继续处理；
# 2开头-请求成功； 
# 3开头-请求被重定向；
# 4开头-请求错误；
# 5开头 - 服务器错误 

""" 获取响应内容 """
html = html.content
html = html.decode('utf-8') # 解决中文乱码问题
html = html.decode('gb18030')
print(html)