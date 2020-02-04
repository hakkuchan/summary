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
    |   |—— 3.3 查找内容：find_all()方法、select()方法
    |   |
    |   |—— 3.4 prettify()方法
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
      其中的 class 是属性，还可有 href、title、src 等各种属性
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


''' 3.3 查找内容 '''

''' 3.3.1 find_all()方法 '''
# (1) 返回所有的 img标签 (列表)
for i in soup.find_all('img'):
    print(i['alt'], i['src'])
# (2) 返回所有的 img 和 a 标签 (列表)
print(type(soup.find_all(['img', 'a'])))  # >>> <class 'bs4.element.ResultSet'>
# (3) 按属性查找
print(soup.find_all('img', attrs={'width':'100'}))

''' 3.3.2 select()方法 '''
# (1) 按标签查找(与 find_all()用法一样)
for i in soup.select('img'):
    print(i['alt'], i['src'])
# (2) 按照 selector path 查找
#     先在浏览器中 Copy selector
#     例如：#content > div > div.article > ol > li:nth-child(1) > div > div.pic > a > img
#     观察规律，对该路径做一定修改，进而查找全部内容
for num in range(1,11):
    path = 'div > div.article > ol > li:nth-child('+str(num)+') > div > div.pic > a > img'
    print(soup.select(path)[0]['alt'])
	

''' 3.4 prettify()方法 '''
# (1) 格式化 soup 的输出
print(soup.prettify())
# (2) 格式化 soup.head 的输出
print(soup.head.prettify())