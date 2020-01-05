import datetime
from dateutil.parser import parse

""" 1. datetime.date() : 处理日期 """
# (1) 返回今日日期（输出格式为date类）
print(datetime.date.today())    # >>> 2020-01-05

# (2) 修改日期格式
today = datetime.date.today()
print(today.strftime('%Y.%m.%d'))  # >>> 2020.01.05

# (3) 返回特定日期
print(datetime.date(2019,9,1)) # >>> 2019-09-01



""" 2. datetime.datatime() : 处理日期+时间"""
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



""" 3. datetime.timedelta() : 处理时间间隔 """
today = datetime.datetime.today()
before = today - datetime.timedelta(hours=7)
yestoday = today - datetime.timedelta(days=1)
print(today)     # >>> 2020-01-05 10:24:14.269598
print(before)    # >>> 2020-01-05 03:24:14.269598
print(yestoday)  # >>> 2020-01-04 10:24:14.269598



""" 4. 日期时间解析 : 将str类转化成datetime类 """
print(parse('2019-9-1'))  # >>> 2019-09-01 00:00:00
print(parse('1-9-2019 10:28:00'))    # >>> 2019-01-09 10:28:00
print(parse('1/9/2019', dayfirst = True))   # >>> 2019-09-01 00:00:00
print(parse('1/9/2019', dayfirst = False))  # >>> 2019-01-09 00:00:00
print(parse('Sep 1, 2019 10:28 PM'))  # >>> 2019-09-01 22:28:00