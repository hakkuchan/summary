"""
    Timestamp是一种pandas的数据类型，表示时间戳， 
    其作用是把数值、字符串与时间序列数据相关联
"""

""" 1. pandas.Timestamp 将不同格式的数据转化为时间戳 """
import numpy as np
import pandas as pd
import datetime

''' 1.1 datetime.datetime → timestamp '''
date1 = datetime.datetime(2016,12,1,12,45,30)
print(date1, type(date1))
time1 = pd.Timestamp(date1)
print(time1, type(time1))

''' 1.2 str → timestamp '''
date2 = '2017-12-21'
print(date2, type(date2))
time2 = pd.Timestamp(date2)
print(time2, type(t2))

''' 1.3 list → timestamp '''
date3 = [ '2017-12-21', '2017-12-22', '2017-12-23'] # 多个时间数据
time3 = pd.to_datetime(date3)
print(time3, type(time3)) # 数据结构为 DatetimeIndex

date3 = ['2017-2-1','2017-2-2','hello world!','2017-2-5','2017-2-6'] # 当一组时间序列中夹杂其他格式数据
time3 = pd.to_datetime(date3, errors='ignore') # 可用errors参数返回
print(time3, type(time3))


""" 2. pd.DatetimeIndex 给一列数据加上时间戳 """
dates = pd.DatetimeIndex(['12/1/2017','12/2/2017','12/3/2017','12/4/2017','12/5/2017'])
data = pd.Series(np.random.rand(len(rng)), index = dates) # 时间序列的series
print(data)
print(data.index)


""" 3. pd.date_range 用来生成DatetimeIndex（时间序列）
      
       pd.date_range(start=None,    # 开始时间
                     end=None,      # 结束时间
                     periods=None,  # 周期
                     freq='D',      # 频率，默认天，pd.date_range()默认频率为日历日，pd.bdate_range()默认频率为工作日
                     tz=None,       # 时区 
                     normalize=False)  # 当为 True 时，将时间转化为到 00:00:00
"""

''' 3.1 指定开始时间、结束时间，生成时间序列 '''
print(pd.date_range('1/1/2019','1/10/2019', normalize=True))


''' 3.2 指定开始时间，周期 '''
print(pd.date_range(start='1/1/2019', periods=3))


''' 3.3 增加时、分、秒数据 '''
print(pd.date_range(end='1/30/2019 15:00:00', periods=3))

print(pd.date_range(start='1/1/2019 15:30', periods = 3, 
                    name='hello world!',  # name：索引对象名称
                    normalize=True))      # normalize：时间正则化到午夜时间（直接变 15:30:00 为 0:00:00）


''' 3.4 将字符串转化为 DatetimeIndex '''
print(pd.date_range('20190101','20190103'))
print(pd.date_range('20190101','20190103',closed='right')) # right则左开右闭
print(pd.date_range('20190101','20190103',closed='left'))  # left则左闭右开
print(pd.bdate_range('20190101','20190103'))   # pd.bdate_range()默认频率为工作日
print(pd.date_range('2019/1/1','2019/1/3'))    # 默认freq = 'D'：每自然日

''' 3.5 freq的各种用法 '''
print(pd.date_range('2019/1/1','2019/1/3', freq = 'B'))                    # B：每工作日
print(pd.date_range('2019/1/1','2019/1/3', freq = 'H'))                    # H：每小时
print(pd.date_range('2019/1/1 12:00','2019/1/1 12:10', freq = 'T'))        # T/min：每分
print(pd.date_range('2019/1/1 12:00:00','2019/1/1 12:00:10', freq = 'S'))  # S：每秒
print(pd.date_range('2019/1/1 12:00:00','2019/1/1 12:00:10', freq = 'L'))  # L：每毫秒（千分之一秒）
print(pd.date_range('2019/1/1 12:00:00','2019/1/1 12:00:10', freq = 'U'))  # U：每微秒（百万分之一秒）
print(pd.date_range('2019/1/1','2019/2/1', freq = '7D'))       # 每7天
print(pd.date_range('2019/1/1','2019/1/2', freq = '2h30min'))  # 每2小时30分钟
print(pd.date_range('2018','2020', freq = '2M'))               # 每2月，每月最后一个日历日

print(pd.date_range('2019/1/1','2019/2/1', freq='W-MON'))       # W-MON：从每周星期一已开始算起 (MON/TUE/WED/THU/FRI/SAT/SUN)
print(pd.date_range('2019/1/1','2019/5/1', freq='WOM-2MON'))    # WOM-2MON：每月的每月第二个星期一开始算

print(pd.date_range('2018','2019', freq = 'M'))       # M：每月最后一个自然日
print(pd.date_range('2018','2020', freq = 'Q-DEC'))   # Q-月：指定月为季度末，每个季度末最后一月的最后一个日历日 
print(pd.date_range('2018','2020', freq = 'A-DEC'))   # A-月：每年指定月份的最后一个自然日 
# 月缩写：JAN/FEB/MAR/APR/MAY/JUN/JUL/AUG/SEP/OCT/NOV/DEC

print(pd.date_range('2018','2020', freq = 'BM'))      # BM：每月最后一个工作日
print(pd.date_range('2018','2020', freq = 'BQ-DEC'))  # BQ-月：指定月为季度末，每个季度末最后一月的最后一个工作日 
print(pd.date_range('2018','2020', freq = 'BA-DEC'))  # BA-月：每年指定月份的最后一个工作日

print(pd.date_range('2018','2020', freq = 'MS'))      # M：每月第一个自然日
print(pd.date_range('2018','2020', freq = 'QS-DEC'))  # Q-月：指定月为季度末，每个季度末最后一月的第一个日历日 
print(pd.date_range('2018','2020', freq = 'AS-DEC'))  # A-月：每年指定月份的第一个日历日

print(pd.date_range('2018','2020', freq = 'BMS'))     # BM：每月第一个工作日
print(pd.date_range('2018','2020', freq = 'BQS-DEC')) # BQ-月：指定月为季度末，每个季度末最后一月的第一个工作日 
print(pd.date_range('2018','2020', freq = 'BAS-DEC')) # BA-月：每年指定月份的第一个工作日

''' 3.6 asfreq 改变频率 '''
s = pd.Series(np.random.rand(4), index = pd.date_range('20170101','20170104'))
print(s)
print(s.asfreq('4H', # 改变频率，这里是D改为4H
                method = 'ffill')) # method：插值模式，None不插值，ffill用之前值填充，bfill用之后值填充

''' 3.7 时间戳与列数据的相对位移 '''
ts = pd.Series(np.random.rand(3), index = pd.date_range('20170101','20170103'))
print(ts)
print(ts.shift(2))  # 正数：数值后移（滞后）
print(ts.shift(-2)) # 负数：数值前移（超前）
print(ts/ts.shift(1)-1) # 计算变化百分比，这里计算：该时间戳与上一个时间戳相比，变化百分比
print(ts.shift(2, freq = 'D')) # 加上freq参数：对时间戳进行位移，而不是对数值进行位移