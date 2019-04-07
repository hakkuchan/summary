import random
import numpy as np


np.random.seed(1) # 重复性

a = random.randint(1,10)             # 产生 1 到 10 的一个整数型随机数
an = np.random.randint(1,10, 100)    # 产生 100 个 1-10 之间的随机整数

b = random.random()           # 产生 0 到 1 之间的随机浮点数
bn = np.random.random(100)    # 产生 100 个 1-10 之间的随机浮点数

c = random.uniform(1.1,5.4)            # 产生 1.1-5.4 之间的随机浮点数
cn = np.random.uniform(1.1,5.4,100)    # 产生 100 个 1.1-5.4 之间的随机浮点数


d = random.choice('tomorrow')  # 从序列中随机选取一个元素

e = random.shuffle([1,2,3,4,5,6,7])  # 打乱列表
nums = np.array([[1,2],[3,4],[5,6]]) # 打乱数组
np.random.shuffle(nums)