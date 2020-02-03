""" 搜索关键词
    
    · 搜索引擎通常有关键词接口，例如
      百度：http://www.baidu.com/s?wd=keyword
      其中，keyword是关键词
    
    · 利用 params 可设定关键词
"""

import requests

url = "http://www.baidu.com/s?"
kv = {'wd': 'Python'}  # 设定关键词字典
r = requests.get(url, params=kv)
print(r.status_code)