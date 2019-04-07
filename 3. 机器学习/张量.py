import torch
import numpy as np

data_nd = np.array([[1,2],[3,4],[5,6]]).astype('float')

""" nd 和 ts 相互转换 """
data_ts = torch.from_numpy(data_nd)  # nd --> tensor
data_nd = data_ts.numpy()  # tensor --> nd

""" 常用函数 """
print(data_ts.size())   # 行列数
print(data_ts.size(0))  # 行数
print(data_ts.size(1))  # 列数
print(data_ts.view(-1,1)) # 改变行列数
print(data_ts[:, 1])    # 索引，与numpy一样
print(data_ts.type())   # 查数据类型
print(data_ts.mean())   # 求平均值

num_ts = torch.tensor([1.25]) # 对于零维矩阵，函数.item()用于取出矩阵中的值
num = num_ts.item()
print(num)

""" 自动微分 """
x_nd = np.array([[2.0,2.0],[2.0,2.0]])
x = torch.tensor(data_nd, requires_grad=True)  # 直接构建一个可自动微分的tensor，requires_grad = True,表示 x 可微分

x = torch.tensor([[2.0,2.0],[2.0,2.0]])
x = x.clone().detach().requires_grad_(True)    # requires_grad_(True),表示 x 可微分

y = x ** 3
z = y.mean() # z = 1/4 * x ** 3
print(z.item())

z.backward()  # z 对 x 求导, (2 x 2) tensor的每个位置分别求导,导数是 3 x ** 2
print(x.grad) # .grad 给出dz/dx|x=2 时的导数, (2 x 2) tensor每个位置的导数是 1/4 * 3 * x ** 2 = 1/4 * 3 * 2 ** 2 = 3