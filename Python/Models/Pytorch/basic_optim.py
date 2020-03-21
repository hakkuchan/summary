""" optim

    · optim，即优化器
      其作用是根据损失函数与模型参数的导数对模型参数进行更新
      内置优化器包括：SGD、ASGD、Rprop、Adagrad、Adadelta、RMSprop、Adam(AMSGrad)、Adamax、SparseAdam、LBFGS
    
    · 优化器的主要区别在于对 梯度 的处理：
      有的优化器直接以 学习率×梯度 作为参数的更新量，
      有的优化器在梯度较大时，采用高学习率，梯度较小时，采用弟学习率，
      还有其它策略，不再赘述
      
    · 下面以SGD优化器为例，展示优化器的用法：
"""

import torch
import torch.nn as nn

# Toy data:
X = torch.randint(10,20, (10,1)).float()
y = 3 * X

# 实例化 Linear层
linear = nn.Linear(1,1)

# 设定损失函数为 MSELoss
criterion = nn.MSELoss()

# 设定优化器为 SGD
optimizer = torch.optim.SGD(linear.parameters(),  # 模型名.parameters() 指定了需优化的模型参数
                            lr=0.001) # 学习率

# 训练 10次
for epoch in range(10):
    # 向前传播：计算 y 及 损失函数值
    y_pred = linear(X)
    loss = criterion(y_pred, y)
    # 向后传播
    optimizer.zero_grad()  # 把优化器中的梯度清零，否则误差梯度会累加
    loss.backward()   # loss函数对其模型参数求导
    optimizer.step()  # optimizer根据 loss的导数对模型参数进行更新
    print(f'Epoch = {epoch+1}:')
    print(f'loss ={loss.item()}', end='   ')
    print('d(loss)/dw =', linear.weight.grad.item(), end='   ')
    print('d(loss)/db =', linear.bias.grad.item(), end='\n\n')

""" · 优化器学习率(lr)的设定十分重要，对于上例：
      lr = 0.0001 → loss 下降缓慢
      lr = 0.01 → loss 显著下降
      lr = 0.1 → loss 发散
"""