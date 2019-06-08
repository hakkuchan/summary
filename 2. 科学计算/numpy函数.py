import numpy as np

""" ufunc 函数 """
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
y = np.sin(x)
y = np.cos(x)
y = np.tan(x)
y = np.exp(x)
y = x**2

""" 设置精度 """
np.set_printoptions(precision=2)

""" 自动生成数组 """
# 初值，终值，步长 (不包括终值)
x = np.arange(0, 1, 0.1)
x = np.arange(10, 0, -1)
# 初值，终值，元素个数
x = np.linspace(0, 1, 11)
# 生成由 1 组成的数组
print(np.ones((3,4)))
# 生成由 0 组成的数组
print(np.zeros((3,4)))

""" 随机数 """
# 产生0-1之间的随机数
print(np.random.rand(1,3))
# 产生标准正态分布的随机数
print(np.random.randn(1,3))
# 产生期望为100，标准差为10的正态分布
print(np.random.normal(100, 10, (1,10)))
# 产生0-9之间的整数随机数
print(np.random.randint(0, 10, (1,3)))
# 产生0-9之间的均匀随机数
print(np.random.uniform(0, 10, (1,3)))
# 产生服从泊松分布的随机数
print(np.random.poisson(2, (1,10)))
# 打乱数组
x = np.array([[1,2], [3,4], [5,6]])
np.random.shuffle(x)
print(x)
# 随机种子：获得相同的随机数
r1 = np.random.randint(0,100,3)
r2 = np.random.randint(0,100,3)
np.random.seed(1)
r3 = np.random.randint(0,100,3)
np.random.seed(1)
r4 = np.random.randint(0,100,3)
print(r1,r2,r3,r4)

""" 简单统计 """
x = np.random.randint(0,10,(2,5))

# 数组中所有元素之和
print(x.sum())
# 数组元素按行相加
print(x.sum(axis=0))
# 数组元素按列相加
print(x.sum(axis=1))

# 求平均
print(x.mean())
print(x.mean(axis=0))
print(x.mean(axis=1))

# 求标准差
print(x.std())
print(x.std(axis=0))
print(x.std(axis=1))

# 求方差
print(x.var())
print(x.var(axis=0))
print(x.var(axis=1))