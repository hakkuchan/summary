import time

''' 1. time.time()
    · 获取时间戳：从1970年00:00:00至今经历了多少秒
    · 可用于计算程序执行时间，详见运行时间分析
'''
print(time.time()) 

''' 2. time.sleep() 程序暂停x秒 '''
for i in range(2):
    print('hello')
    time.sleep(1)

''' 3. 将当前时间转换为一个字符串 '''
print(time.ctime())

''' 4. 将当前时间转为当前时区的struct_time '''
print(time.localtime()) # 将当前时间转为当前时区的struct_time

''' 5. 格式化输出时间 '''
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) # >>> 2020-01-05 11:09:36