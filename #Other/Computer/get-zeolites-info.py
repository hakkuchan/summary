import time
import random
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'http://asia.iza-structure.org/IZA-SC/ftc_table.php'
html = requests.get(url).content
soup = BeautifulSoup(html,'html.parser')
links = [link for link in soup.find_all('td')][3:]
zeolites = ['http://asia.iza-structure.org/IZA-SC/' + item.a['href'] for item in links]
database = []
for num, url in enumerate(zeolites):
    print(num+1, url)
    data = []
    data.append(num+1)
    name = str(url)[-3:]
    data.append(name)
    html = requests.get(url).content  
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table').find_all('td')
    for i in range(5, 60):
        if 'a = ' in table[i].text:
            data.append(table[i].text)
        if 'b = ' in table[i].text:
            data.append(table[i].text)
        if 'c = ' in table[i].text:
            data.append(table[i].text)
        if 'α = ' in table[i].text:
            data.append(table[i].text)
        if 'β = ' in table[i].text:
            data.append(table[i].text)
        if 'γ = ' in table[i].text:
            data.append(table[i].text)
        if 'Volume = ' in table[i].text:
            data.append(table[i].text + table[i+1].text)
        if 'RDLS = ' in table[i].text:
            data.append(table[i].text + table[i+1].text)
        if 'Framework density ' in table[i].text:
            data.append(table[i].text + table[i+1].text)
        if 'Topological density' in table[i].text:
            data.append(table[i].text)
            data.append(table[i+1].text)
            data.append(table[i+2].text)
        if 'Ring sizes' in table[i].text:
            data.append(table[i].text + table[i+1].text)
        if 'Channel dimensionality' in table[i].text:
            data.append(table[i].text + table[i+1].text)
        if 'that can be included' in table[i].text:
            data.append(table[i].text)
            data.append(table[i+1].text)
        if 'that can diffuse along' in table[i].text:
            data.append(table[i].text)
            data.append(table[i+1].text)
            data.append(table[i+2].text)
            data.append(table[i+3].text)
        if 'Accessible volume' in table[i].text:
            data.append(table[i].text)
            data.append(table[i+1].text)
    database.append(data)
    time.sleep(random.uniform(2,4))
print('Done')
database_df = pd.DataFrame(database)
database_df.to_csv('E:\Work\Jupyter\data\zeolites.csv')