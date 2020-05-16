import torch 
import torch.nn as nn
import torchvision
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
torch.manual_seed(1)

''' 设置处理器 '''
device = torch.device('cuda:0')
device = torch.device('cpu')

''' 准备数据集 '''
train_data = datasets.MNIST(root='E:\Work\Jupyter\Data\MNIST', train=True, transform=transforms.ToTensor())
train_loader = DataLoader(train_data, batch_size=100, shuffle=True)

''' 搭建编码器和解码器 '''
class AutoEncoder(nn.Module):
    def __init__(self):
        super(AutoEncoder, self).__init__()
        # 编码器
        self.encoder = nn.Sequential(nn.Linear(28*28, 128), # (图片数据维度, 第一层隐藏层节点数)
                                     nn.Tanh(),
                                     nn.Linear(128, 64),    # (第一层隐藏层节点数, ……二……)
                                     nn.Tanh(),
                                     nn.Linear(64, 12),     # (……二……, ……三……)
                                     nn.Tanh(),
                                     nn.Linear(12, 3))      # (……三……, ……四……)
        # 解码器
        self.decoder = nn.Sequential(nn.Linear(3, 12),      # (编码维度, 第一层隐藏层节点数)
                                     nn.Tanh(),
                                     nn.Linear(12, 64),     # (第一层隐藏层节点数, ……二……)
                                     nn.Tanh(),
                                     nn.Linear(64, 128),    # (……二……, ……三……)
                                     nn.Tanh(),
                                     nn.Linear(128, 28*28), # (……四……，新图片维度)
                                     nn.Sigmoid())
    def forward(self, x):
        out_encode = self.encoder(x)
        out_decode = self.decoder(out_encode)
        return out_encode, out_decode


''' 初始化：自编码器、优化器、损失函数 '''
model = AutoEncoder()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
loss_func = nn.MSELoss()


''' 训练自编码器 '''
for epoch in range(1):
    for step, (x, y) in enumerate(train_loader):
        b_x = x.view(100, 28*28) # (batch_size, 图片维度)
        b_y = x.view(100, 28*28)
        out_encode, out_decode = model(b_x)
        loss = loss_func(out_decode, b_y) # 计算原始图片与新生成图片的损失函数值
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if step % 500 == 0:
            print(f'Epoch: {epoch+1} | loss: {loss.data:.6f}') # 显示损失函数值