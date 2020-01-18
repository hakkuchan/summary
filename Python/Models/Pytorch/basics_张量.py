import numpy as np
import torch 
import torch.nn as nn

""" 1. 生成 tensor """

# 1.1 list → tensor
x = torch.tensor([[1.0,2.0],[2.0,3.0]])
x = x.clone().detach().requires_grad_(True) # requires_grad 用于设定是否可导，True为可导

# 1.2 ndarray → tensor '''
data_nd = np.array([[1,2],[3,4],[5,6]]).astype('float') # 生成 ndarray 数据
# 方式 1：
data_ts = torch.from_numpy(data_nd) # 无法指定是否可导
# 方式 2：
data_ts = torch.tensor(data_nd, requires_grad=False) 



""" 2. tensor → ndarray & scalar """
nd = np.array([[1, 2]]).astype('float')
# 方式 1：针对 requires_grad=False 的 tensor
ts1 = torch.tensor(nd, requires_grad=False) 
print(ts1.numpy())
# 方式 2：针对 requires_grad=True 的 tensor
ts2 = torch.tensor(nd, requires_grad=True)
print(ts2.detach().numpy())
# 方式 3：零维 tensor → 标量 (scalar) 
print(torch.tensor([1.25]).item())



""" 3. 常用操作 """
# 显示行列数
print(data_ts.size())  # size(0): 行数，size(1) 列数
# 改变行列数
print(data_ts.view(-1,1))
# 拼接
print(torch.cat((data_ts, data_ts), dim=0)) # dim=0 行数增加，dim=1 列数增加
# 索引，与numpy一样
print(data_ts[:, 1])
# 查数据类型
print(data_ts.type())
# 求平均值
print(data_ts.mean())