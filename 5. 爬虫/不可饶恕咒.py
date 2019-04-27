import os
import time
import random
import pandas as pd
import requests
from bs4 import BeautifulSoup

html = requests.get('website')
html = html.content.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
img_links = soup.find_all('img')

for num, link in enumerate(img_links):
    img_name = 'E:\Other\Downloads\Pic\p' + str(num + 1) +'.jpg'
    img_html = requests.get(link['src'])
    with open(img_name, 'wb') as f:
        f.write(img_html.content)
        f.flush()
    f.close()
    print('进度： {}/{} '.format(num+1, len(img_links)), end='\r')
    time.sleep(random.uniform(1, 2))

path='E:\\Other\\Downloads\\Pic/'      
f=os.listdir(path)
for num, item in enumerate(f):
    oldname=path+f[num]
    if oldname[25:26] == '.':
        newname= path + '00' + str(oldname[24:25])+'.JPG'  
        os.rename(oldname,newname)
    if oldname[26:27] == '.':
        newname= path + '0' + str(oldname[24:26])+'.JPG'
        os.rename(oldname,newname)
    if oldname[27:28] == '.':
        newname= path + str(oldname[24:27])+'.JPG'
        os.rename(oldname,newname)
print('Complete')