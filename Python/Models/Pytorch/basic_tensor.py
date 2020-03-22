"""  tensor(张量) 
     
     · tensor 是 pytorch 中的最常用的数据类型，
       其数学本质是多维数组，类似于 numpy 中的数据类型 ndarray，
       但不同于 ndarray 的是：tensor 可用于执行 GPU 计算
    
     · 在很多操作上可以借鉴对 numpy 中 ndarray 的操作
     
     · 目录
     |
     |—— 1. 构造
     |   |
     |   |—— 1.1 直接构造
     |   |
     |   |—— 1.2 生成器
     |   |
     |   |—— 1.3 ndarray → tensor
     |   |
     |   |—— 1.4 自动求导(autograd)
     |
     |—— 2. 操作
         |
         |—— 2.1 tensor → ndarray & scalar
         |
         |—— 2.2 基本操作
         |
         |—— 2.3 基本运算
"""


import numpy as np
import torch 


""" 1. 构造 """

''' 1.1 直接构造 '''
t = torch.tensor([[1.,2.], [3.,4.]])


''' 1.2 生成器 '''
# (1) arange 指定步长
t = torch.arange(1, 10, 2) # start, end, step
# (2) linspace 指定分割数
t = torch.linspace(1, 2, 5) # start, end, 分割数
# (3) zeros / zeros_like
t = torch.zeros(2,2)
t = torch.zeros_like(torch.arange(1,10,1))
# (4) ones / ones_like
t = torch.ones(2,2)
t = torch.ones_like(torch.arange(1,10,1))
# (5) eye
t = torch.eye(5) # 创建 5x5 的对角阵
# (6) diag
t = torch.diag(torch.tensor([1,2,3])) # 创建以 1,2,3 为对角线的对角阵
# (7) 随机数
t = torch.randint(low=1, high=10, size=(2,3)) # 随机整数
t = torch.randn(2,3) # size (2,3) 正态分布随机数
t = torch.rand(2,3)  # size (2,3)均匀分布随机数


''' 1.3 ndarray → tensor '''
x = np.array([[1,2],[3,4]]).astype('float')
# 方式 1
t = torch.from_numpy(x)
# 方式 2
t = torch.tensor(x)


'''1.4 自动求导 (autograd, 使tensor的求导操作被自动追踪) '''
# 方式 1：利用参数 requires_grad
t = torch.tensor([[1.,2.],[3.,4.]], requires_grad=True)
t = torch.rand(2,3, requires_grad=True)
# 方式 2：利用属性 requires_grad_ 
t = torch.tensor([[1.,2.], [3.,4.]]).requires_grad_(True)
t = torch.rand(2,3).requires_grad_(True)

# 停止自动求导
# 方式 1：detach()方法
t = torch.tensor([[1.,2.], [3.,4.]]).requires_grad_(True)
t = t.detach()
# 方式 2：利用属性 requires_grad_ 
t = torch.tensor([[1.,2.], [3.,4.]]).requires_grad_(True)
t = t.requires_grad_(False)



""" 2. 操作 """

''' 2.1 tensor → ndarray & scalar '''
# 方式 1：直接转换
t1 = torch.tensor([[1.,2.], [3.,4.]])
x1 = t1.numpy()
# 方式 2：先停止 autograd，在转换
t2 = torch.tensor([[1.,2.], [3.,4.]], requires_grad=True)
x2 = t2.detach().numpy()
# 方式 3：零维 tensor → scalar 
t3 = torch.tensor([1.25], requires_grad=True)
x3 = t3.detach().item() # >>> 1.25


''' 2.2 基础操作 '''
# 类型
t = torch.tensor([[1,2,3], [4,5,6]])
print(t.type())

# 行列数
t = torch.tensor([[1,2,3], [4,5,6]])
print(t.size())     # 显示行列数，torch.Size([2, 3])
print(t.size(0))    # 行数
print(t.size(1))    # 列数
print(t.view(1,-1)) # 改变行列数，tensor([[1, 2, 3, 4, 5, 6]])
# 等价于：
print(t.shape)         # 显示行列数，torch.Size([2, 3])
print(t.shape[0])      # 行数
print(t.shape[1])      # 列数
print(t.reshape(1,-1)) # 改变行列数，tensor([[1, 2, 3, 4, 5, 6]])

# 合并
t1 = torch.ones((2,2))
t2 = torch.zeros((2,2))
print(torch.cat((t1, t2), dim=0))
print(torch.cat((t1, t2), dim=1))

# 索引和切片
t = torch.tensor([[1,2,3], [4,5,6], [7,8,9]])
print(t[0])
print(t[1:3])
print(t[:,0])
print(t[:,[0,2]])

# 数据类型转换
t = torch.tensor([[1,2,3], [4,5,6]])
print(t.type()) # >>> torch.LongTensor  长整型
t = torch.tensor([[1,2,3], [4,5,6]]).float()
print(t.type()) # >>> torch.FloatTensor 浮点型

# 深拷贝
t = torch.tensor([1.,2.], requires_grad=True)
print(id(t))
t = t.clone()
print(id(t))


''' 2.3 基本运算 '''
t = torch.tensor([[1.,2.,3.], [4.,5.,6.]])
print(t + 10)    # 加法
print(t * 2)     # 乘法
print(1 / (t+1)) # 除法
print(t ** 0.5)  # 幂
print(t.sum())       # 所有元素求和
print(t.sum(dim=0))  # dim=0: 每行数据求和
print(t.sum(dim=1))  # dim=1: 每列数据求和
print(t.mean())  # 求平均值 (可设定 dim)
print(t.max())   # 求最大值 (可设定 dim)
print(t.min())   # 求最小值 (可设定 dim)
print(t.std())   # 求标准差 (可设定 dim)