import calendar

# 生成年历
print(calendar.calendar(2019))  

# 生成月历
print(calendar.month(2019, 9))  

# 判断闰年
print(calendar.isleap(2020))  # >>> True

# 返回特定月份首日是周几，一共多少天
print(calendar.monthrange(2019, 9)) # >>> (6, 30) 首日星期天，9月有30天
print(calendar.monthrange(2020, 2)) # >>> (5, 29) 首日星期六，2020年2月有29天

# 返回特定日期是星期几
print(calendar.weekday(2019, 9, 1)) # >>> 6 星期天