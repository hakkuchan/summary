""" · 目录
    |
    |—— 1. get()操作
    |   |
    |   |—— 1.1 status_code
    |   |
    |   |—— 1.2 ~ 1.3 text, content
    |   |
    |   |—— 1.4 ~ 1.5 encoding, apparent_encoding
    |   |
    |   |—— 1.6 爬取网页的通用框架
    |
    |—— 2. 技巧
    |   |
    |   |—— 2.1 反来源审查
    |   |
    |   |—— 2.2 爬取图片
    |   |
    |   |—— 2.3 关键字搜索
"""

import requests
import os
import random

""" 1. get()操作 """
r = requests.get('https://www.baidu.com/')  # 请求获取网页Response对象
print(type(r))  # >>> 'requests.models.Response'

''' 1.1 status_code：http请求的返回状态 '''
print(r.status_code)
# status_code 状态码：
# 200-请求成功；
# 1开头-被接受，需要继续处理； 
# 3开头-请求被重定向；
# 4开头-请求错误；
# 5开头-服务器错误
r.raise_for_status() # 判断请求是否正常，如正常，返回200

''' 1.2 text：页面内容（字符串形式） '''
print(r.text)

''' 1.3 content: 页面内容的二进制形式 '''
print(r.content)

''' 1.4 encoding：从HTTP header猜测的响应内容编码方式 '''
print(r.encoding)

# 更改编码方式 1：
r.encoding = 'utf-8'
print(r.text)  # 乱码 → 中文

# 更改编码方式 2：
print(r.content.decode('utf-8'))
# 注意：r.text.decode('utf-8')会报错，因为 r.text 返回值是字符串

''' 1.5 apparent_encoding: 从内容中分析出的响应内容编码方式 '''
print(r.apparent_encoding)

''' 1.6 爬取网页的通用框架 '''
def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 判断请求是否正常，如否，执行except
                              # 使用 r.raise_for_status() 可以避免 if r.status_code == 200 条件句
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return r.status_code
url = 'https://www.baidu.com/'
print(get_html_text(url))



""" 2. 技巧 """

''' 2.1 反反爬 '''
# 操作 1：设置 user-agent 列表，随机选取，以应对来源审查
agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)']
# 操作 2：设置 proxies 列表，随机选取，以应对针对同一 IP 多次访问的反爬机制
# proxy 可从该网站下载：https://www.xicidaili.com/
proxy_list = [
    '180.103.42.164',
    '113.116.106.212']
# 操作 3：设置 referer，表示访问是从 referer页面发起的，以应对针对用户行为的反爬机制
referer = 'https://www.baidu.com/'
# 注意：操作 1，2，3 不一定全要使用，
# 操作 4：随机生成 headers 和 proxy，并请求（可设为循环，多次尝试）
headers = {'User-Agent' : random.choice(agent_list), 'referer': referer}
proxy = {'http' : 'http://' + random.choice(proxy_list)}
# 示例：
url = 'https://www.zhihu.com/'
r = requests.get(url) # 直接用爬虫请求
print(r.status_code) # >>> 400
r = requests.get(url, headers=headers, proxies=proxy, timeout=20) # 伪装后请求
print(r.status_code) # >>> 200


''' 2.2 爬取图片 '''
# 图片资源的 url 一般以 .jpg 结尾
pic_url = 'https://pic4.zhimg.com/v2-45ed9cc0da397cbbfb8d3450c8c9cbfe_1200x500.jpg'
# 设置文件夹路径
folder = 'E:\\Other\\Downloads\\Done\\'
# 设置图片名
name = 'p.jpg'
# 设置完整文件路径
path = folder + name
# 主程序
try:
    if not os.path.exists(folder):  # 检查文件夹是否存在
        os.mkdir(folder)  # 创建文件夹路径
    if not os.path.exists(path):  # 确保没有重名文件
        r = requests.get(pic_url) # 访问 url 对应的数据资源
        with open(path, 'wb') as f: # 以二进制形式打开完整文件路径
            f.write(r.content)  # 把图片的二进制数据写入上述路径
            f.flush()  # 清理图片缓存
        print('Done')
    else:
        print('包含重名文件')  # 如果已有重名文件，返回提醒 
except:
    print(f'Fail: {r.status_code}')  # 爬取图片失败

    
''' 2.3 关键字搜索
    
    · 搜索引擎通常有关键字接口，例如
      百度：http://www.baidu.com/s?wd=keyword
      其中，keyword是关键字
    · 利用 params 可设定关键字
'''
url = "http://www.baidu.com/s?"
kv = {'wd': 'Python'}  # 设定关键字字典
r = requests.get(url, params=kv)  # 利用 params 修改关键字
print(r.status_code)