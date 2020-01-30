""" · 目录
    |
    |—— 1. 创建
    |   |
    |   |—— 1.1 直接创建
    |   |
    |   |—— 1.2 生成器创建：arange, linspace, zeros, ones, eye, random
    |   |
    |   |—— 1.3 由Dataframe创建
    |
    |—— 2. 操作
        |
        |—— 2.1 索引和切片
        |
        |—— 2.2 基础操作
        |
        |—— 2.3 数组运算
        |
        |—— 2.4 设置精度
        |
        |—— 2.5 ufunc函数
        |
        |—— 2.6 自定义ufunc函数
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

""" 1. 创建 """

''' 1.1 直接创建 '''
print(np.array(range(10)))                 # 整型
print(np.array([1,2,3.14,4,5]))            # 浮点型
print(np.array([[1,2,3],('a','b','c')]))   # 二维数组：嵌套序列（列表，元祖均可）

''' 1.2 生成器创建 '''
# (1) arange() 指定步长
print(np.arange(10))    # 返回0-9，整型
print(np.arange(10.0))  # 返回0.0-9.0，浮点型
print(np.arange(5,12))  # 返回5-11
print(np.arange(5.0,12,2))  # 返回5.0-12.0，步长为2
print(np.arange(5.0,8,0.5))  # 返回5.0-8.0，步长为0.5
# (2) linspace() 指定分割成多少段
print(np.linspace(2.0, 3.0, num=5)) # 以 2 开始，3 结束
print(np.linspace(2.0, 3.0, num=5, endpoint=False)) # endpoint=False: 不包含结束值，True包含
print(np.linspace(2.0, 3.0, num=5, retstep=True))   # retstep = True：显示步长，False不显示
# (3) zeros() / zeros_like()
print(np.zeros(5))
print(np.zeros((3,2), dtype = np.int)) # dtype：指定数据类型，默认numpy.float64
print(np.zeros_like(np.array([[1,2,3], [4,5,6]]))) # 返回具有与给定数组相同的形状和类型的零数组
# (4) ones() / ones_like()
print(np.ones(9))
print(np.ones((2,3,4)))
print(np.ones_like(np.array([[1,2,3], [4,5,6]])))
# (5) eye()
print(np.eye(5)) # 创建一个N*N的单位方阵(对角线值为1，其余为0)
# (6) 随机数 '''
# 随机种子
np.random.seed(1)
# 随机整数
print(np.random.randint(2,size=5))   # 生成5个[0,2)之间随机整数
print(np.random.randint(2,6,size=5)) # 生成5个[2,6)之间随机整数  
print(np.random.randint(2,size=(2,3))) # 生成一个2x3整数数组,取数范围：[0,2)随机整数 
# 随机浮点数
print(np.random.uniform(1.1,5.4,size=(10,2))) # 产生 100 个 1.1-5.4 之间的随机浮点数
# 正态分布随机数
print(np.random.normal(size=(4,4))) # 生成一个标准正太分布的 4*4 数组
ar1 = np.random.randn(1000) # 生成[0,1)之间的 1000 个随机浮点数 —— 正态分布
ar2 = np.random.randn(1000)
plt.scatter(ar1,ar2)
plt.show()
# 均匀分布随机数
ar1 = np.random.rand(1000) # 生成[0,1)之间的 1000 个随机浮点数 —— 均匀分布
ar2 = np.random.rand(1000)
plt.scatter(ar1,ar2)
plt.show()
# 打乱数组
nums = np.array([[1,2],[3,4],[5,6]])
np.random.shuffle(nums)

''' 1.3 由Dataframe创建 '''
df = pd.read_csv('E:\Work\Jupyter\Data\char_data.csv')
ar = df.values


""" 2. 操作 """

''' 2.1 索引和切片 '''
ar = np.arange(72).reshape(8, 9)
print(ar)
print(ar[0])          # 第1行数据
print(ar[0:3])        # 第1-3行数据
print(ar[[2,4,6]])    # 第2,4,6行数据
print(ar[:,[1,3,5]])  # 第1,3,5列数据

''' 2.2 基础操作 '''
print(ar)          # 注意单行数组的格式：中括号，元素之间没有逗号（和列表区分）
print(ar.ndim)     # 数组维数
print(ar.shape)    # 数组的行列数 (m, n)
print(ar.shape[0]) # 数组的行数
print(ar.shape[1]) # 数组的列数
print(ar.size)     # 数组的元素总数
print(ar.dtype)    # 数组中元素的类型
print(ar.itemsize) # 数组中每个元素的字节大小
print(ar.T)        # 转置
print(ar.ravel())  # 改为 1 行
print(ar.reshape(1,-1))    # 改变行列数
print(ar.astype('float'))  # 类型转换
ar1 = np.ones((2,2))
ar2 = np.zeros((2,2))
print(np.concatenate((ar1, ar2), axis=0)) # 按行合并数组，即样本数增加
print(np.concatenate((ar1, ar2), axis=1)) # 按列合并数组，即特征数增加

''' 2.3 数组运算 '''
ar = np.arange(6).reshape(2,3)
print(ar + 10)    # 加法
print(ar * 2)     # 乘法
print(1 / (ar+1)) # 除法
print(ar ** 0.5)  # 幂
print(ar.sum())          # 所有元素求和
print(ar.sum(axis=0))    # axis=0:每行数据求和; axis=1:按每列数据求和
print(np.sum(ar,axis=0)) # axis=0:每行数据求和; axis=1:按每列数据求和
print(ar.mean())  # 求平均值
print(ar.max())   # 求最大值
print(ar.min())   # 求最小值
print(ar.std())   # 求标准差
print(ar.var())   # 求方差
print(np.sort(np.array([1,4,3,2,5,6])))  # 排序

''' 2.4 设置精度 '''
np.set_printoptions(precision=2)

''' 2.5 ufunc函数 (注：输出为 ndarray 对象) '''
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
y = np.sin(x)
y = np.cos(x)
y = np.tan(x)
y = np.exp(x)
y = x**2

''' 2.6 自定义ufunc函数 (注：输出为 ndarray 对象)  '''
# 传统函数
def fn_test(x, a, b):
    return a * x^2 + b
# 生成 x 数据
x = np.arange(0,1000000,1)
# 对于传统函数，如果要把 x 中的每个数带入函数，需用循环语句
%time print(type([fn_test(i, 2, 1) for i in x]))  
# 更好的方法是：利用 frompyfunc 把原始函数转化为 ufunc，运算会作用于全部 x
# 比循环语句快得多，计算量越大，差距越明显
# ufunc的输出为 ndarray 格式
ufunc_test = np.frompyfunc(fn_test, 3, 1) # 其中 3 表示函数输入参数为 3 个，1 表示输出参数为 1 个
%time print(type(ufunc_test(x, 2, 1)))