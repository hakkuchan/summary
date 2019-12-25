from selenium import webdriver
from bs4 import BeautifulSoup

# 声明浏览器对象
browser = webdriver.Chrome('C:/Users/ZhouBin/AppData/Local/Google/Chrome/Application/chromedriver.exe')
browser.get('website')
html = browser.page_source
browser.close()
soup = BeautifulSoup(html,'html.parser')