""" loss 
    
    · 损失函数，Pytorch 的 nn模块提供了多种损失函数，
      它们的输入值是两组数据，而输出值是对应的损失函数值
    
    · 利用 backward()方法，可实现损失函数可对模型参数求导，
      导数值将被用于优化模型参数(见下一篇)
      
    · 损失函数种类较多，本篇以 MSELoss为例
"""

import torch
import torch.nn as nn

# 生成 X数据
X = torch.randint(10,20, (10,1)).float()

# 实例化 Linear层
linear = nn.Linear(1,1)
# 权值初始化
nn.init.constant_(linear.weight, 2)
nn.init.constant_(linear.bias, 1)

# 调用 MSELoss
criterion = nn.MSELoss()

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
    print('d(loss)/db =', linear.bias.grad.item(), end='\n\n')

""" 可以看出：差异程度越大 → MSELoss值及其对模型参数的导数越大 → 训练模型时参数的更新程度越大 """