"""
Pandas时刻数据: Timestamp

时刻数据代表时间点，是pandas的数据类型，

是将值与时间点相关联的最基本类型的时间序列数据

"""

''' (1) pandas.Timestamp '''
import numpy as np
import pandas as pd
import datetime

date1 = datetime.datetime(2016,12,1,12,45,30)  # 创建一个datetime.datetime
t1 = pd.Timestamp(date1)
print(t1)
print(type(t1))  # pd.to_datetime()：如果是单个时间数据，转换成pandas的时刻数据，数据类型为Timestamp

date2 = '2017-12-21'  # 创建一个字符串
t2 = pd.Timestamp(date2)
print(t2)
print(type(t2))

date3 = [ '2017-12-21', '2017-12-22', '2017-12-23'] # 多个时间数据
t3 = pd.to_datetime(date3)
print(type(t3)) # 会转换为pandas的DatetimeIndex

date3 = ['2017-2-1','2017-2-2','hello world!','2017-2-5','2017-2-6'] # 当一组时间序列中夹杂其他格式数据
t3 = pd.to_datetime(date3, errors='ignore') # 可用errors参数返回
print(t3)


''' (2) pd.DatetimeIndex '''
rng = pd.DatetimeIndex(['12/1/2017','12/2/2017','12/3/2017','12/4/2017','12/5/2017'])
st = pd.Series(np.random.rand(len(rng)), index = rng) # 时间序列的series
print(st)
print(st.index)


''' (3) pd.date_range '''
# 用来生成DatetimeIndex
# pd.date_range(start=None, end=None, periods=None, freq='D', tz=None, normalize=False)
# start：开始时间
# end：结束时间
# periods：偏移量
# freq：频率，默认天，pd.date_range()默认频率为日历日，pd.bdate_range()默认频率为工作日
# tz：时区
print(pd.date_range('1/1/2017','1/10/2017', normalize=True))    # start + end；
print(pd.date_range(start='1/1/2017', periods=10))              # start + periods
print(pd.date_range(end = '1/30/2017 15:00:00', periods = 10))  # 增加了时、分、秒
print(pd.date_range(start = '1/1/2017 15:30', periods = 10, 
                    name = 'hello world!',  # name：索引对象名称
                    normalize = True))        # normalize：时间正则化到午夜时间（直接变 15:30:00 为 0:00:00）
print(pd.date_range('20170101','20170104'))  # 20170101也可读取
print(pd.date_range('20170101','20170104',closed = 'right')) # right则左开右闭
print(pd.date_range('20170101','20170104',closed = 'left'))  # left则左闭右开
print(pd.bdate_range('20170101','20170111')) # pd.bdate_range()默认频率为工作日

print(pd.date_range('2017/1/1','2017/1/4'))              # 默认freq = 'D'：每自然日
print(pd.date_range('2017/1/1','2017/1/4', freq = 'B'))  # B：每工作日
print(pd.date_range('2017/1/1','2017/1/2', freq = 'H'))  # H：每小时
print(pd.date_range('2017/1/1 12:00','2017/1/1 12:10', freq = 'T'))  # T/MIN：每分
print(pd.date_range('2017/1/1 12:00:00','2017/1/1 12:00:10', freq = 'S'))  # S：每秒
print(pd.date_range('2017/1/1 12:00:00','2017/1/1 12:00:10', freq = 'L'))  # L：每毫秒（千分之一秒）
print(pd.date_range('2017/1/1 12:00:00','2017/1/1 12:00:10', freq = 'U'))  # U：每微秒（百万分之一秒）
print(pd.date_range('2017/1/1','2017/2/1', freq='W-MON'))       # W-MON：从每周星期已开始算起 (MON/TUE/WED/THU/FRI/SAT/SUN)
print(pd.date_range('2017/1/1','2017/5/1', freq = 'WOM-2MON'))  # WOM-2MON：每月的每月第二个星期一开始算

print(pd.date_range('2017','2018', freq = 'M'))       # M：每月最后一个自然日
print(pd.date_range('2017','2020', freq = 'Q-DEC'))   # # Q-月：指定月为季度末，每个季度末最后一月的最后一个日历日 
print(pd.date_range('2017','2020', freq = 'A-DEC'))   # A-月：每年指定月份的最后一个自然日 
# 月缩写：JAN/FEB/MAR/APR/MAY/JUN/JUL/AUG/SEP/OCT/NOV/DEC

print(pd.date_range('2017','2018', freq = 'BM'))      # BM：每月最后一个工作日
print(pd.date_range('2017','2020', freq = 'BQ-DEC'))  # BQ-月：指定月为季度末，每个季度末最后一月的最后一个工作日 
print(pd.date_range('2017','2020', freq = 'BA-DEC'))  # BA-月：每年指定月份的最后一个工作日

print(pd.date_range('2017','2018', freq = 'MS'))      # M：每月第一个自然日
print(pd.date_range('2017','2020', freq = 'QS-DEC'))  # Q-月：指定月为季度末，每个季度末最后一月的第一个日历日 
print(pd.date_range('2017','2020', freq = 'AS-DEC'))  # A-月：每年指定月份的第一个日历日

print(pd.date_range('2017','2018', freq = 'BMS'))     # BM：每月第一个工作日
print(pd.date_range('2017','2020', freq = 'BQS-DEC')) # BQ-月：指定月为季度末，每个季度末最后一月的第一个工作日 
print(pd.date_range('2017','2020', freq = 'BAS-DEC')) # BA-月：每年指定月份的第一个工作日
print(pd.date_range('2017/1/1','2017/2/1', freq = '7D'))       # 7天
print(pd.date_range('2017/1/1','2017/1/2', freq = '2h30min'))  # 2小时30分钟
print(pd.date_range('2017','2018', freq = '2M'))               # 2月，每月最后一个日历日

ts = pd.Series(np.random.rand(4), index = pd.date_range('20170101','20170104'))
print(ts)
print(ts.shift(2))  # 正数：数值后移（滞后）
print(ts.shift(-2)) # 负数：数值前移（超前）
print(ts/ts.shift(1)-1) # 计算变化百分比，这里计算：该时间戳与上一个时间戳相比，变化百分比
print(ts.shift(2, freq = 'D')) # 加上freq参数：对时间戳进行位移，而不是对数值进行位移


''' (3) asfreq '''
s = pd.Series(np.random.rand(4), index = pd.date_range('20170101','20170104'))
print(s)
print(s.asfreq('4H', # 改变频率，这里是D改为4H
                method = 'ffill')) # method：插值模式，None不插值，ffill用之前值填充，bfill用之后值填充
