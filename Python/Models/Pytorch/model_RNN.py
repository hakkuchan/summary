import numpy as np
import torch
from torch import nn
import matplotlib.pyplot as plt
torch.manual_seed(1)


""" 1. RNN层 """

''' (1) 假定以下3个样本分别为t=0,1,2时的、前后相关的序列数据 '''
x = torch.tensor([[[3.,3.],   # t=0
                   [6.,6.],   # t=1 
                   [9.,9.]]]) # t=2 
                 
''' (2) RNN层预测t时刻的样本时，输入变量除了t时刻样本的特征，还包括t-1时刻样本的隐藏层输出 '''
layer = nn.RNN(input_size=2,  # 输入变量的维度
               hidden_size=6, # 隐藏层节点数
               num_layers=1,  # RNN的层数
               nonlinearity='tanh', # 设置激活函数
               batch_first=True) 

''' (3) RNN层的计算结果有两项，第一项 layer(x)[0] 是所有样本在隐藏层的输出 
        具体来说，layer(x)[0] 是一个 3×6 的结果，3表示样本数，6取决于隐藏层节点数
        前一样本的隐藏层输出是后一样本的输入之一 (另一输入是后一样本的特征) '''
print(layer(x)[0].data)

''' (4) RNN层计算结果的第二项 layer(x)[1] 是序列中最后一个样本的隐藏层输出 '''
print(layer(x)[1].data)


""" 2. RNN回归实例 """

''' (1) 训练集：共100个样本，x为sin(step)，y为cos(step) '''
step = np.linspace(0.5*np.pi, np.pi, 100)
x = np.sin(step).astype('float32')
x = torch.from_numpy(x[np.newaxis, :, np.newaxis])
y = np.cos(step).astype('float32')
y = torch.from_numpy(y[np.newaxis, :, np.newaxis])

''' (2) 搭建RNN '''
class RNN(nn.Module):
    def __init__(self, in_dim, n_hidden, n_layer, out_dim):
        super(RNN, self).__init__()
        self.layer1 = nn.RNN(in_dim, n_hidden, n_layer, nonlinearity='tanh',batch_first=True)
        self.layer2 = nn.Linear(n_hidden, out_dim)
    def forward(self, x, s):
        y, s = self.layer1(x, s)
        y = self.layer2(y)
        return y, s


''' (3) 初始化：实例化 RNN / 定义损失函数和优化器 '''
model = RNN(1, 20, 2, 1)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
loss_func = nn.MSELoss()

''' (4) 训练RNN '''
s = None
for epoch in range(1000):
    # 向前传播
    y_pred, s = model(x, s)
    s = s.data # 重要步骤：把当前隐藏层输出重新打包，作为下一轮计算的输入
    loss = loss_func(y_pred, y)
    # 向后传播
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if (epoch+1)%250 == 0:
        print(f'epoch = {epoch+1:>4} / Loss = {loss.item():.6f}')
# 展示预测结果
plt.plot(step, y.flatten(), 'r-', label='y_real')
plt.plot(step, y_pred.data.numpy().flatten(), 'b-', label='y_pred')
plt.legend(loc='best')
plt.show()

''' (5) 测试 RNN '''
# 准备测试集数据 (样本个数显著影响预测结果。这是因为RNN预测当前样本时，要以上一样本的隐藏层输出为输入)
step = np.linspace(2.5*np.pi, 3*np.pi, 100)
x_test = np.sin(step).astype('float32')
x_test = torch.from_numpy(x_test[np.newaxis, :, np.newaxis])
y_test = np.cos(step).astype('float32')
y_test = torch.from_numpy(y_test[np.newaxis, :, np.newaxis])
# 预测测试集数据
model.eval()
y_pred, s = model(x_test, s)
# 展示预测结果
plt.plot(step, y_test.flatten(), 'r-', label='y_real')
plt.plot(step, y_pred.data.numpy().flatten(), 'b-', label='y_pred')
plt.legend(loc='best')
plt.show()