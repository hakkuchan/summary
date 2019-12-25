import requests
from bs4 import BeautifulSoup

html = requests.get('https://maoyan.com/board/4')
html = html.content.decode('utf-8')

""" 解析库 """
soup = BeautifulSoup(html,'lxml')
# python标准库:    BeautifulSoup(markup, "html.parser")
# lxml HTML解析器：BeautifulSoup(markup, "lxml")
# lxml XML解析器： BeautifulSoup(markup, "xml")
# html5lib 解析器：BeautifulSoup(markup, "html5lib")

""" 浅识 HTML代码结构
一段典型的 HTML 代码：
<a href="/films/1203" title="霸王别姬" class="image-link"}">…</a> 
其中 a 为标签(tag)，href、title、class 是标签下的属性
"""

""" tag 操作 """
# 传递
tag = soup.dd.a # 其中 dd 是标签，a 是 dd 的子标签
# 属性
print(tag['title'])
print(tag['href'])
print(60*'-')

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