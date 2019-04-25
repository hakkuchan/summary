""" 
爬虫是请求网站并提取网页数据的自动化程序
爬虫的步骤：
1) 向服务器发送请求（利用 Requests库）
2) 获取响应（通常为 HTML 代码）
3) 解析响应内容（利用 BeautifulSoup4库）
4) 结构化存储数据
"""

""" 以爬取猫眼电影网站top100榜单信息为例 """
import pandas as pd
import requests # 请求库
from bs4 import BeautifulSoup # html代码解析库

out = []
for page_num in range(0,10):
    # 根据 url 的规则生成不同页面的 url
    url = 'https://maoyan.com/board/4?offset=' + str(page_num*10)
    # requests 获取网页 html 代码
	html = requests.get(url).content
    # beautifulsoup 解析代码
	soup = BeautifulSoup(html, 'lxml')
    for page in soup.find_all('dd'):  # .find_all() 方法返回所有匹配标签的列表
        name = page.find(attrs={'class':'name'}).string  # .find() 方法返回第一个匹配标签
        star = page.find(attrs={'class':'star'}).string.strip()
        star = star.replace('主演：','')
        date = page.find(attrs={'class':'releasetime'}).string # .string 提取 html 中的文本
        date = date.replace('上映时间：','')
        score = (page.find(attrs={'class':'score'}).find(attrs={'class':'integer'}).string + 
                 page.find(attrs={'class':'score'}).find(attrs={'class':'fraction'}).string)
        out.append([name, star, date, score])

out = pd.DataFrame(out,columns=['片名','演员','上映时间','评分'])
out.to_csv('E:\Work\Jupyter\MaoYanTop100.csv', index=True, encoding='utf_8_sig')