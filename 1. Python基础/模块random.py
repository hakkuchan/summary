import random
import numpy as np

# 重复性
np.random.seed(1)

# 产生 1 到 10 的一个整数型随机数
a = random.randint(1,10)
# 产生 100 个 1-10 之间的随机整数
an = np.random.randint(1,10, 100)

# 产生 0 到 1 之间的随机浮点数
b = random.random()
# 产生 100 个 1-10 之间的随机浮点数
bn = np.random.random(100)

# 产生 1.1-5.4 之间的随机浮点数
c = random.uniform(1.1,5.4)
# 产生 100 个 1.1-5.4 之间的随机浮点数
cn = np.random.uniform(1.1,5.4,100)

# 从序列中随机选取一个元素
d = random.choice('tomorrow') 

# 从序列中随机选取 3 个元素
e = random.sample(['preg','plas','pres','skin','test','mass','pedi','age','class'], 3) #

# 打乱列表
f = random.shuffle([1,2,3,4,5,6,7])

# 打乱数组
nums = np.array([[1,2],[3,4],[5,6]])
np.random.shuffle(nums)