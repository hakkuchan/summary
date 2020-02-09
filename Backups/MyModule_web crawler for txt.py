import os
import time
import random
import requests
from bs4 import BeautifulSoup

# 网址池
urls = []

# 函数
def get_soup(url):
    kv = {'User-Agent':'Chrome 79.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.content,'html.parser')
    return soup

def get_text(soup):
    for i in (soup.select('br')):
        if i.div != None:
            out = str(i.text)
            return out.split('。')

def save_txt(soup, text):
    folder = os.getcwd() + "\\"
    name = soup.select('h4')[0].text + '.txt'
    path = folder + name
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(path, 'w') as f:
        for line in text:
            line = "".join(line.split())
            print(line, file=f, end='。\n')

# 主程序
for url in urls: 
    soup = get_soup(url)
    text = get_text(soup)
    save_txt(soup, text)
print('Download complete')