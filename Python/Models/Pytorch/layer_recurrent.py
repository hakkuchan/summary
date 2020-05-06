""" 标准循环层 & 长短时记忆层 """

import torch
import torch.nn as nn

''' 1. 标准RNN层 '''
# 实例化 RNN 层 
layer = nn.RNN(input_size=2,  # 输入变量的维度
               hidden_size=6, # 隐藏层节点数
               num_layers=1,  # RNN的层数
               nonlinearity='tanh', # 设置激活函数
               batch_first=True,    # 指定参数顺序为 (batch, seq, feature)
               dropout=0, # 指定 dropout率
               bidirectional=False) # 指定是否为双向 RNN 
               
# 计算
X = torch.tensor([[[3,3], [6,6], [9,9]]]).float()
y = layer(X)
print(y[0].data) # 所有样本的隐藏层输出 
print(y[1].data) # 最后一个样本的隐藏层输出


''' 2. 长短时记忆循环层 '''
# 实例化 LSTM 层 
layer = nn.LSTM(input_size=2,  # 输入变量的维度
                hidden_size=6, # 隐藏层节点数
                num_layers=1,  # RNN的层数
                batch_first=True,    # 指定参数顺序为 (batch, seq, feature)
                dropout=0, # 指定 dropout率
                bidirectional=False) # 指定是否为双向 RNN 
               
# 计算
X = torch.tensor([[[3,3], [6,6], [9,9]]]).float()
y = layer(X)
print(y)