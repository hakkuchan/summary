import progressbar
import time

bar = progressbar.ProgressBar() # 样式 1
for i in bar(range(100)):
    time.sleep(0.01)
    
bar = progressbar.ProgressBar(widgets=[progressbar.Percentage()]) # 样式 2
for i in bar(range(100)):
    time.sleep(0.01)