""" · 目录
    |
    |—— 1. 卷积层：(1) 单个卷积层；(2) 多个卷积层
    |
    |—— 2. 池化层：(1) 最大池化；(2) 平均池化
    |
    |—— 3. CNN实例：MNIST
"""


import torch 
import torch.nn as nn
import torchvision
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
torch.manual_seed(1)


""" 1. 卷积层 """
x = torch.tensor([[[[1., 1., 1., 0., 0., 0.],
                    [1., 1., 1., 0., 0., 0.],
                    [1., 1., 1., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.]]]])

''' (1) 单个卷积核 '''
layer = nn.Conv2d(in_channels=1,  # 黑白图片: in_channels=1; RGB彩色图片: in_channels=3
                  out_channels=1, # 卷积核的个数：用多少个卷积核扫描图片
                  kernel_size=3,  # 卷积核的大小，也可以是(m,n)形式 
                  stride=1,       # 表示扫描速度：每次移动的像素点数
                  padding=0)      # 宽卷积：边缘补充几层 0
nn.init.constant_(layer.weight, 1.)
nn.init.constant_(layer.bias, 0.)
print(layer(x))

''' (2) 多个卷积核 '''
layer = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=3, stride=1, padding=0)
nn.init.constant_(layer.weight, 1.)
nn.init.constant_(layer.bias, 0.)
print(layer(x))




""" 2. 池化层 """
x = torch.tensor([[[[6., 1., 2.],
                    [3., 5., 4.],
                    [2., 2., 0.]]]])

''' (1) 最大池化 '''
layer = nn.MaxPool2d(kernel_size=2, stride=1)
print(layer(x))

''' (2) 平均池化 '''
layer = nn.AvgPool2d(kernel_size=2, stride=1)
print(layer(x))




""" 3. CNN实例：MNIST """

''' 设置处理器 '''
device = torch.device('cuda:0')
device = torch.device('cpu')

''' 设定超参数 '''
n_epoch = 1
batch_size = 100
lr = 1e-3

''' 准备数据集 '''
train_dataset = datasets.MNIST(root='E:\Work\Jupyter\Data\MNIST', train=True, transform=transforms.ToTensor())
test_dataset = datasets.MNIST(root='E:\Work\Jupyter\Data\MNIST', train=False, transform=transforms.ToTensor())
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

''' 搭建 ANN '''
class CNN(nn.Module):
    def __init__(self, n_class=10): # n_classes=10 表示最后分为 10 类
        super(CNN, self).__init__()
        # CNN层一般包括：卷积层、批标准化层、激活函数、池化层
        self.layer1 = nn.Sequential(
            # Conv2d 层像是一个扫描器（filter），依次扫描图片的各个区域，提取其特征
            nn.Conv2d(
                in_channels=1,    # 黑白图片: in_channels=1; RGB彩色图片: in_channels=3
                out_channels=16,  # out_channels=16 表示 16个扫描器同时扫描，对同一区域提取 16个特征
                kernel_size=4,    # kernel_size 表示扫描器大小，4x4
                stride=2,         # 扫描速度，stride=2表示扫描一个区域后，向右跳 2个单位再扫描下一个区域
                padding=2),       # 把图片边缘围绕两圈 0，保证原始图片的边缘被扫描到
                # 输出 “ 图片 ” 的尺寸 out_size = (in_size - kernel_size + 2*padding) / stride + 1 = (28-4+2*2)/2+1=15
            
            nn.BatchNorm2d(16),   # 批标准化层：对每个区域输出的 16个特征进行批标准化
            nn.ReLU(),            # 激活层
            nn.MaxPool2d(kernel_size=2, stride=1, padding=1)) # 池化层：用局部特征表示区域特征
            # out_size = (15-2+2*1)/1 + 1 = 16
        self.layer2 = nn.Sequential(
            nn.Conv2d(
                in_channels=16,   # layer1的输出 16 等于 layer2的输入 16
                out_channels=32,  # 对同一区域扫描 32次，输出 32个特征
                kernel_size=5,    # 扫描器大小为 5x5
                stride=1,         # 扫描速度为 1
                padding=2),       # 把图片边缘围绕两圈 0，保证原始图片的边缘被扫描到
                # out_size = (16-5+2*2)/1+1=16
            nn.BatchNorm2d(32),   # 批标准化层：对每个区域输出的 16 个特征进行批标准化
            nn.ReLU(),            # 激活层
            nn.MaxPool2d(kernel_size=2, stride=2, padding=1)) # 池化层：用局部特征表示区域特征
            # out_size = (16-2+2*1)/2+1=9
        self.layer3 = nn.Linear(9*9*32, n_class) 
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = x.reshape(x.size(0), -1)
        x = self.layer3(x)
        return x

''' 初始化：实例化CNN / 定义损失函数 / 优化算法 '''
model = CNN().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

''' 训练 ANN '''
total_step = len(train_loader)
for epoch in range(n_epoch):
    for i, (images, labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)
        # Output forward
        out = model(images)
        loss = criterion(out, labels)
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()   
        if (i+1) % 100 == 0:
            print(f'Epoch [{epoch+1}/{n_epoch}], Step [{i+1}/{total_step}], Loss: {loss.item():.4f}')

''' 测试 ANN '''
model.eval()
n_correct = 0
n_total = 0
for images, labels in test_loader:
    images = images.to(device)
    labels = labels.to(device)
    out = model(images)
    pred = torch.max(out.data, 1)[1]
    n_total += labels.size(0)
    n_correct += (pred == labels).sum().item()
print(f'Test Accuracy: {100 * n_correct / n_total:.2f} %')