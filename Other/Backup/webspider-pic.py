import os
import time
import random
import requests
from bs4 import BeautifulSoup

# 网址池
urls = [	
       ]

# 函数
def get_soup(url):
    kv = {'User-Agent':'Chrome 79.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.content,'html.parser')
    return soup

def get_link(soup):
    links = []
    for img_tag in soup.select('img'):
        if 'data-src' in img_tag.attrs:
            links.append(img_tag['data-src'])
    return links

def get_path(soup, links):
    paths = []
    folder = 'E:\\Other\\Downloads\\Pic\\' + soup.find('h4').string + '\\'
    for num in range(len(links)):
        if num < 10:
            name = '00' + str(num) + '.jpg'
        if 10 <= num < 100:
            name = '0' + str(num) + '.jpg'
        if 100 <= num < 1000:
            name = str(num) + '.jpg'
        paths.append(folder + name)
    return paths

def get_img(soup, img_paths, img_urls):
    count = 0
    folder = 'E:\\Other\\Downloads\\Pic\\' + soup.find('h4').string + '\\'
    for path, url in zip(img_paths, img_urls):
        if not os.path.exists(folder):
            os.mkdir(folder)
        kv = {'User-Agent':'Chrome 79.0'}
        with open(path, 'wb') as f:
            f.write(requests.get(url, headers=kv).content)
            f.flush()
        count += 1
        print('{}/{}'.format(count, len(img_paths)), end='\r')
        time.sleep(random.uniform(1, 2))

# 主程序
for num, url in enumerate(urls):
    soup = get_soup(url)
    img_urls = get_link(soup)
    img_paths = get_path(soup, img_urls)
    get_img(soup, img_paths, img_urls)
    print(f'Total progress: {num+1}/{len(urls)} ')
print('Download complete')