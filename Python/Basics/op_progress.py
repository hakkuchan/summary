import time
import progressbar


""" 1. 自制 (推荐) """

# (1) 只显示进度
for i in range(1000):
    time.sleep(0.00001)
    print(f'进度：{round((i+1)/1000*100, 3)} %', end='\r')

# (2) 进度 + 进度条 + 运行时间
begin = time.time()
for i in range(1000):
    time.sleep(0.00001)
    run = time.time()
    print('{:<4} % |{:<30}| {} s'.format(round((i+1)/1000*100,2), int((i+1)/1000*30)*'>', round(run-begin,2)),end='\r')


""" 2. progressbar 模块 """

# 样式 1
bar = progressbar.ProgressBar()
for i in bar(range(1000)):
    time.sleep(0.00001)

# 样式 2  
bar = progressbar.ProgressBar(widgets=[progressbar.Percentage()])
for i in bar(range(1000)):
    time.sleep(0.00001)
