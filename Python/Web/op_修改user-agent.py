""" 修改 User‐Agent
    
    · 某些网站会检查来访 HTTP 协议头的 User‐Agent 域（即"来源审查"）
      只响应浏览器或友好爬虫的访问
    
	· 反来源审查方法：修改User‐Agent
"""

import requests

url = 'https://movie.douban.com/top250'  # 豆瓣电影排行网页
r = requests.get(url)
print(r.request.headers)  # >>> {'User-Agent': 'python-requests/2.22.0' …… } 说明我们在用爬虫访问
print(r.status_code)      #  由于豆瓣网站进行了来源审查，因此无法访问

''' 修改 User-Agent: '''
kv = {'user-agent': 'Chrome 79.0'}  # 设置字典，其中 'Chrome 79.0'为浏览器版本
r = requests.get(url, headers=kv)   # 替换 headers 中 User-Agent
print(r.status_code)  # >>> 200  访问正常