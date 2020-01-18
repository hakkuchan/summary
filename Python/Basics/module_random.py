import random

# 产生 0 到 1 之间的随机浮点数
print(random.random())    

# 产生 1.1-5.4 之间的随机浮点数
print(random.uniform(1.1, 5.4))

# 产生 1 到 10 的一个随机整数
print(random.randint(1, 10))

# 从序列中随机选取一个元素
print(random.choice('tomorrow'))

# 从序列中随机选取2个元素
print(random.sample(['a','b','c','d','e'], 2))

# 将可变序列中的元素随机排序
print(random.shuffle(['a','b','c','d','e']))