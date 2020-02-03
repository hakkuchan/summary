""" · 目录
    |
    |—— 1. 网页代码
    |
    |—— 2. 网页解析
    |
    |—— 3. BeautifulSoup类的方法
    |   |
    |   |—— 3.1 访问标签
    |   |
    |   |—— 3.2 访问标签的属性
    |   |
    |   |—— 3.3 
"""



""" 1. 网页代码
    
    · html(hyper text markup language): 超文本标记语言
    
    · HTML通过预定义的<>…</>标签形式组织不同类型的信息
      
      例如： 
      
      <html>
          <body>
              <p class='title'> … </p>
          <body>
      </html>
    
    · <p class='title'> … </p>
      其中的 class 是属性，还可有 href、title 等无数种属性
"""



""" 2. 网页解析 """

import requests
from bs4 import BeautifulSoup

# Step 1: 访问并读取网页
url = 'https://movie.douban.com/top250' # 豆瓣电影 Top 250 网页
kv = {'User-Agent':'Chrome 79.0'}
r = requests.get(url, headers=kv)
print(r.status_code)
page = r.content.decode('utf-8')  # 读取页面并更改编码方式

# Step 2: 解析页面 (解析器: 'html.parser', 'lxml', 'xml', 'html5lib')
soup = BeautifulSoup(page,'html.parser')
print(type(soup))  # >>> <class 'bs4.BeautifulSoup'>



""" 3. BeautifulSoup类的方法 """

''' 3.1 访问标签 '''
# (1) 访问 soup → head标签 → title标签
print(soup.head.title)  # >>> <title> 豆瓣电影 Top 250 </title>
# (2) 访问标签中的内容
print(soup.head.title.string)  # >>> 豆瓣电影 Top 250



''' 3.2 访问标签的属性 '''
# (1) 访问 soup → html标签 → 全部属性列表
print(soup.html.attrs)
# (2) 访问 soup → html标签 → 'lang'属性
# 方法 1：
print(soup.html['lang'])
# 方法 2：
print(soup.html.get('lang'))

# ''' 3.5 prettify()方法 '''
# # (1) 格式化 soup 的输出
# print(soup.prettify())
# # (2) 格式化 soup.head 的输出
# print(soup.head.prettify())


"——————————————————————————————————————————————————"

""" 标准选择器 ：按照标签或属性查找网页中内容 """
# select() 返回所有匹配项的列表
for i in soup.select('dd'):
    print(i.a['title'])
print(60*'-')

# 利用 selector path 定位
for num in range(1,11):
    name_ = 'dl > dd:nth-child(' + str(num) + ') > div > div > div.movie-item-info > p.name'
    print(soup.select(name_)[0].string)
print(60*'-')

# find_all() 按标签查找，返回所有匹配项的列表
for i in soup.find_all('dd'):
    print(i.a['title'])
print(60*'-')

# find_all() 按属性查找，返回所有匹配项的列表
for i in soup.find_all(attrs={'class':'name'}): 
    print(i.a['title'])
print(60*'-')

# find() 返回第一个匹配项
for i in soup.find_all('dd'):
    print(i.find(attrs={'class':'name'}).string)
print(60*'-')