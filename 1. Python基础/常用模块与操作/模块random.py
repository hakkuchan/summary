import random

print(random.randint(1,10))       # 产生 1 到 10 的一个整数型随机数
print(random.random())            # 产生 0 到 1 之间的随机浮点数
print(random.uniform(1.1,5.4))    # 产生 1.1-5.4 之间的随机浮点数
print(random.choice('tomorrow'))  # 从序列中随机选取一个元素
print(random.sample(['preg','plas','pres','skin','test'], 3)) # 从序列中随机选取 3 个元素