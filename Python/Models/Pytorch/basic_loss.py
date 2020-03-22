""" loss 
    
    · 损失函数，Pytorch 的 nn模块提供了多种损失函数，
      它们的输入值是两组数据，而输出值是对应的损失函数值
    
    · 利用 backward()方法，可实现损失函数可对模型参数求导，
      导数值将被用于优化模型参数(见下一篇)
      
    · 损失函数种类较多，本篇以 MSELoss 和 CrossEntropyLoss 为例
"""


import torch
import torch.nn as nn

""" 1. MSELoss (均方根误差，常用于回归) """
# 生成 X数据
X = torch.randint(10,20, (10,1)).float()
# 实例化 Linear层
linear = nn.Linear(1,1)
# 权值初始化
nn.init.constant_(linear.weight, 2)
nn.init.constant_(linear.bias, 1)
# 调用 MSELoss
criterion = nn.MSELoss()
# 实例
for coef in [1, 0.9, 0.8, 0.7, 0.6, 0.5]:
    # 生成两组有差异的 y数据，差异程度依赖于系数 coef
    y1 = linear(X)
    y2 = coef * y1
    # 计算损失函数值
    loss = criterion(y1, y2)
    print(f'Coef={coef}:')
    print(f'loss ={loss.item()}', end='   ')
    # 求导
    loss.backward()
    print('d(loss)/dw =', linear.weight.grad.item(), end='   ')
    print('d(loss)/db =', linear.bias.grad.item(), end='\n')
# 可以发现：差异程度越大 → MSELoss值及其对模型参数的导数越大 → 训练模型时参数的更新程度越大


""" 2. CrossEntropyLoss (交叉熵，常用于分类) """
# Toy data：来自 MNIST数据集
# (1) 3个手写数字样本，标签值分别为 3, 4, 2
label = torch.tensor([3, 4, 2])
# (2) 3个预测结果：总类别数为 10，故ANN输出数据维度是 10维
y_pred = torch.tensor([[ 5.4016e-02,  2.8664e-01, -2.4310e-01,  3.6999e-01, -1.4552e-01,
                        -8.7577e-02,  8.7708e-02,  2.2522e-01, -1.5215e-01, -3.2446e-01],
                       [ 7.7398e-02, -2.9893e-02,  6.3266e-02,  1.0281e-01, -9.4386e-02,
                        -8.4706e-02, -1.8968e-01,  9.8543e-02, -2.3567e-01, -3.3478e-01],
                       [ 2.4640e-01,  2.0338e-01, -4.6097e-02, -1.3645e-01, -3.8992e-01,
                         6.5466e-02,  1.5525e-01, -1.5818e-01, -2.7589e-01, -4.8260e-01]])
# 调用 CrossEntropyLoss()
criterion = nn.CrossEntropyLoss()
# 计算交叉熵
loss = criterion(y_pred, label)
print('Loss:', loss.item())
# 把 y_pred 转换为 label
label_pred = torch.max(y_pred,1)[1] # torch.max() 返回最大值和对应索引，索引即为标签
print('label_pred:', label_pred)