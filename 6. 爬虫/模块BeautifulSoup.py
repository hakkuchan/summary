import requests
from bs4 import BeautifulSoup

html = requests.get('https://maoyan.com/board/4')
html = html.content
html = html.decode('utf-8') # 解决中文乱码问题

""" 解析库 """
soup = BeautifulSoup(html,'lxml')
# python标准库:    BeautifulSoup(markup, "html.parser")
# lxml HTML解析器：BeautifulSoup(markup, "lxml")
# lxml XML解析器： BeautifulSoup(markup, "xml")
# html5lib 解析器：BeautifulSoup(markup, "html5lib")

""" 格式化代码 """
print(soup.prettify()) # 非必需

""" 标准选择器 """
# find_all() 按标签查找，返回所有匹配项的列表
for i in soup.find_all('dd'):
    print(i)
print(60*'-')

# find_all() 按属性查找，返回所有匹配项的列表
for i in soup.find_all(attrs={'class':'name'}): 
    print(i)
print(60*'-')

# find() 返回第一个匹配项
for i in soup.find_all('dd'):
    print(i.find(attrs={'class':'name'}).string)
print(60*'-')
