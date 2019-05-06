import os
import time
import random
import pandas as pd
import requests
from bs4 import BeautifulSoup

""" 显示某一页的全部结果 """
url = 'website'
html = requests.get(url)
html = html.content.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
a = soup.select('li')
b = [i for i in a if 'title' in str(i)]
c = [i for i in b if '安卓用户' not in str(i)]
for i in c:
    print(i.a.span.string, i.a['title'],'\n','http://www.yiren34.com' + i.a['href'])


""" 搜索多个页面中的关键词 """	
keyword = '123'
for page_num in range(2,100):
    url = 'website' + str(page_num) + '.html'
    html = requests.get(url)
    html = html.content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.select('li')
    b = [i for i in a if 'title' in str(i)]
    c = [i for i in b if '安卓用户' not in str(i)]
    for i in c:
        if keyword in i.a['title'] and '彩漫' in i.a['title']:
            print(i.a['title'], 'http://www.yiren34.com' + i.a['href'])
			
	 		
""" 下载保存图片 """
# 修改参数
url = 'website'
path='E:\\Other\\Downloads\\Pic\\测试/'

html = requests.get(url)
html = html.content.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
img_links = soup.find_all('img')

if not os.path.exists(path):
    os.makedirs(path)

for num, link in enumerate(img_links):
    img_name = path + '/p' + str(num + 1) +'.jpg'  
    img_html = requests.get(link['src'])
    with open(img_name, 'wb') as f:
        f.write(img_html.content)
        f.flush()
    f.close()
    print('Downloading: {}/{} '.format(num+1, len(img_links)), end='\r')
    time.sleep(random.uniform(1, 3))

f=os.listdir(path)
trans = len(path)-23
for num, item in enumerate(f):
    oldname=path+f[num]
    if oldname[25+trans:26+trans] == '.':
        newname= path + '00' + str(oldname[24+trans:25+trans])+'.jpg'       
        os.rename(oldname,newname)
    if oldname[26+trans:27+trans] == '.':
        newname= path + '0' + str(oldname[24+trans:26+trans])+'.jpg'
        os.rename(oldname,newname)
    if oldname[27+trans:28+trans] == '.':
        newname= path + str(oldname[24+trans:27+trans])+'.jpg'
        os.rename(oldname,newname)