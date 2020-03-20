""" class torch.nn.Linear """

# 对数据做线性转化：out = AX + b
# 完整形式是：nn.Linear(in_features, out_features, bias=True)
# in_features: 输入样本的维度，比如输入样本有 3 个特征，infeatures = 3
# out_features: 输出样本的维度，比如输出一个值，则 out_features = 1；输出 10 个类别，则 out_features = 10
# bias：设定是否需要偏置项，若需要，bias = True (默认为 True)；若不需要，bias = False，相当于 out = AX

# 示例:
import torch
from torch import nn

# 输入 2 个样本，每个样本有 3 个特征
X = torch.tensor([[1,2,3], [4,5,6]]).float()

# 实例化 torch.nn.Linear 层
layer = nn.Linear(3,1, bias=True)

# 将 nn.Linear 中的权重和偏置项设置为 1
nn.init.constant_(layer.weight, 1)
nn.init.constant_(layer.bias, 2)

# 计算结果
y = layer(X) # 1*1 + 2*1 + 3*1 + 2 = 8; 1*4 + 1*5 + 1*6 + 2 = 17
print(y)


''' 例 1：线性回归 '''
# 生成 X, y 数据
x = torch.randn(10, 3)
y = torch.randn(10, 2)
# 构建linear层 (3个输入，2个输出)
linear = nn.Linear(3, 2)
print ('Initialized w:', linear.weight)
print ('Initialized b:', linear.bias)
# 构建 损失函数 和 优化器
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(), lr=0.01)
# 向前传播，即基于 x 计算 y
y_pred = linear(x)
# 计算损失
loss = criterion(y_pred, y)
print('Loss: ', loss.item())
# 向后传播，即loss函数对 w,b 求导
loss.backward()
print ('d(Loss)/dw: ', linear.weight.grad) 
print ('d(Loss)/db: ', linear.bias.grad)
# 基于计算所得 gradients 进行一次优化
optimizer.step()
# 计算一次优化后的损失函数
pred = linear(x)
loss = criterion(pred, y)
print('Loss after 1 step optimization: ', loss.item())


''' 例 2：线性回归 '''
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


# Hyper-parameters
input_size = 1
output_size = 1
epochs_num = 60

# Toy dataset
x_train = np.array([[3.3], [4.4], [5.5], [6.71], [6.93], [4.168], 
                    [9.779], [6.182], [7.59], [2.167], [7.042], 
                    [10.791], [5.313], [7.997], [3.1]], dtype=np.float32)

y_train = np.array([[1.7], [2.76], [2.09], [3.19], [1.694], [1.573], 
                    [3.366], [2.596], [2.53], [1.221], [2.827], 
                    [3.465], [1.65], [2.904], [1.3]], dtype=np.float32)

# Convert numpy arrays to torch tensors
inputs = torch.from_numpy(x_train)
targets = torch.from_numpy(y_train)

# Linear regression model
model = nn.Linear(input_size, output_size)

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)  

# Train the model
for epoch in range(epochs_num):
    
    # Forward pass
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    
    # Backward and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print ('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, epochs_num, loss.item()))

# Plot the graph
predicted = model(inputs).detach().numpy()
plt.plot(x_train, y_train, 'ro', label='Original data')
plt.plot(x_train, predicted, label='Fitted line')
plt.legend()
plt.show()