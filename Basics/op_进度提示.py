""" 1. 基于 progressbar """
import progressbar
import time

# 样式 1
bar = progressbar.ProgressBar()
for i in bar(range(1000)):
    time.sleep(0.00001)

# 样式 2  
bar = progressbar.ProgressBar(widgets=[progressbar.Percentage()])
for i in bar(range(1000)):
    time.sleep(0.00001)


""" 2. 自制进度提示（推荐） """
for i in range(1000):
    time.sleep(0.00001)
    print(f'进度：{round((i+1)/1000*100, 3)} %', end='\r')