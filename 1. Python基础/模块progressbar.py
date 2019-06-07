import progressbar
import time

# 样式 1
bar = progressbar.ProgressBar() 
for i in bar(range(100)):
    time.sleep(0.01)

# 样式 2  
bar = progressbar.ProgressBar(widgets=[progressbar.Percentage()])
for i in bar(range(100)):
    time.sleep(0.01)