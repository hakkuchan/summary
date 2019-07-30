'''
日期和时间模块：datetime; dateutil.parser (日期解析方法)

主要掌握：datetime.date(), datetime.datetime(), datetime.timedelta()

'''
import datetime
from dateutil.parser import parse

# date
print(datetime.date.today())    # 返回今日日期，输出格式为 date类
print(datetime.date(1949,10,1)) # (年,月,日) → 直接得到当时日期

# datatime
print(datetime.datetime.now())
print(datetime.datetime(1949,10,1,9,30,0))
t1, t2 = datetime.datetime(1950,10,1,9,30,0), datetime.datetime(1949,10,1,10,30,0), 
print(t1-t2)

# datetime.timedelta：时间差
today = datetime.datetime.today()
yestoday = today - datetime.timedelta(1)
print(today)
print(yestoday)
print(today - datetime.timedelta(7))

# 日期时间解析
date = '12-21-2017'
print(parse(date)) # 直接将str转化成datetime.datetime
print(parse('2000-1-1'))
print(parse('5/1/2014'))
print(parse('5/1/2014', dayfirst = True))  # 国际通用格式中，日在月之前，可以通过dayfirst来设置
print(parse('22/1/2014'))
print(parse('Jan 31, 1997 10:45 PM'))