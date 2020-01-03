import numpy as np
import torch 
import torch.nn as nn

""" numpy 和 tensor 的相互转换 """
# Creat ndarray data
data_nd = np.array([[1,2],[3,4],[5,6]]).astype('float')
# ndarray --> tensor
data_ts = torch.from_numpy(data_nd) # 无法指定是否可导
data_ts = torch.tensor(data_nd, requires_grad=False)
# tensor  --> ndarray
data_nd = data_ts.numpy()  # 针对 requires_grad=False 的 tensor
data_nd = data_ts.detach().numpy()  # 针对 requires_grad=True 的 tensor
# 令 tensor 可导：
x = torch.tensor([[1.0,2.0],[2.0,3.0]])
x = x.clone().detach().requires_grad_(True)


""" 常用方法 """
# 行列数
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
# 转化为标量(scalar)，仅对零维矩阵有效
print(torch.tensor([1.25]).item())