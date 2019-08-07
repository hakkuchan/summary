import time

""" time.sleep() 程序暂停 () 秒 """
for i in range(2):
    print('hello')
    time.sleep(1)

""" 将当前时间转换为一个字符串 """
print(time.ctime())

""" 将当前时间转为当前时区的struct_time """
print(time.localtime()) # 将当前时间转为当前时区的struct_time

# time.strftime(a,b)
# a为格式化字符串格式
# b为时间戳，一般用localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''