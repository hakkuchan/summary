""" · 时间 & 日期
    |
    |—— 1. time
    |
    |—— 2. calender
    |
    |—— 3. datetime
"""

import time
import calendar
import datetime
from dateutil.parser import parse


""" 1. time 模块 """
# (1) time.time 获取时间戳（从1970年00:00:00至今经历了多少秒）
print(time.time()) # 应用：运行程序前后时间戳之差为程序运行时间
# (2) time.sleep(x) 程序暂停x秒
for i in range(3):
    print('hello')
    time.sleep(0.5)
# (3) 格式化输出时间
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) # >>> xxxx-xx-xx xx:xx:xx
# (4) 将当前时间转换为一个字符串
print(time.ctime())
# (5) 将当前时间转为当前时区的struct_time
print(time.localtime())



""" 2. calendar 模块 """
# (1) 生成年历
print(calendar.calendar(2019))  
# (2) 生成月历
print(calendar.month(2019, 9))  
# (3) 判断闰年
print(calendar.isleap(2020))  # >>> True
# (4) 返回特定月份首日是周几，一共多少天
print(calendar.monthrange(2019, 9)) # >>> (6, 30) 首日星期天，9月有30天
print(calendar.monthrange(2020, 2)) # >>> (5, 29) 首日星期六，2020年2月有29天
# (5) 返回特定日期是星期几
print(calendar.weekday(2019, 9, 1)) # >>> 6 星期天



""" 3. datetime 模块 """

''' 3.1 datetime.date() : 处理日期 '''
# (1) 返回今日日期（输出格式为date类）
print(datetime.date.today())    # >>> 2020-01-05
# (2) 修改日期格式
today = datetime.date.today()
print(today.strftime('%Y.%m.%d'))  # >>> 2020.01.05
# (3) 返回特定日期
print(datetime.date(2019,9,1)) # >>> 2019-09-01

''' 3.2 datetime.datatime() : 处理日期+时间 '''
# (1) 返回现在时刻
print(datetime.datetime.now())  # >>> 2020-01-05 10:13:44.223869
# (2) 修改格式
print(datetime.datetime.now().strftime('%Y.%m.%d %H-%M-%S'))  # >>> 2020.01.05 10-13-44
# (3) 转化为国际标准格式
now = datetime.datetime.now()
print(now.isoformat())  # >>> 2020-01-05T10:15:44.271514 (其中的 T 表示 time)
# (4) 返回特定时间
print(datetime.datetime(2019,9,1,10,28,0))  # >>> 2019-09-01 10:28:00
# (5) 时间运算
t1 = datetime.datetime(1992,3,13,3,15,0)
t2 = datetime.datetime(2019,9,1,10,28,0)
print(abs(t1-t2))  # >>> 10033 days, 7:13:00

''' 3.3 datetime.timedelta() : 处理时间间隔 '''
today = datetime.datetime.today()
before = today - datetime.timedelta(hours=7)
yestoday = today - datetime.timedelta(days=1)
print(today)     # >>> 2020-01-05 10:24:14.269598
print(before)    # >>> 2020-01-05 03:24:14.269598
print(yestoday)  # >>> 2020-01-04 10:24:14.269598

''' 3.4 日期时间解析 : 将str类转化成datetime类 '''
print(parse('2019-9-1'))  # >>> 2019-09-01 00:00:00
print(parse('1-9-2019 10:28:00'))    # >>> 2019-01-09 10:28:00
print(parse('1/9/2019', dayfirst = True))   # >>> 2019-09-01 00:00:00
print(parse('1/9/2019', dayfirst = False))  # >>> 2019-01-09 00:00:00
print(parse('Sep 1, 2019 10:28 PM'))  # >>> 2019-09-01 22:28:00