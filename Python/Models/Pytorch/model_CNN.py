import torch 
import torch.nn as nn
import torchvision
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from torchvision import datasets
torch.manual_seed(1)


""" 设置处理器 """
device = torch.device('cuda:0')
device = torch.device('cpu')

""" 设定超参数 """
n_epoch = 1
batch_size = 100
lr = 1e-3

""" 准备数据集 """
train_dataset = datasets.MNIST(root='E:\Work\Jupyter\Data\MNIST', train=True, transform=transforms.ToTensor(), download=True)
test_dataset = datasets.MNIST(root='E:\Work\Jupyter\Data\MNIST', train=False, transform=transforms.ToTensor())
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

""" 搭建ANN """
class Model(nn.Module):
    def __init__(self, n_class=10): # n_classes=10 表示最后分为 10 类
        
        super(Model, self).__init__()
        
        # 一个层一般包括：卷积层、批标准化层、激活函数、池化层
        self.layer1 = nn.Sequential(
            # Conv2d 层像是一个扫描器（filter），依次扫描图片的各个区域，提取其特征
            nn.Conv2d(
                in_channels=1,    # 黑白图片，in_channels=1；RGB彩色图片，in_channels=3
                out_channels=16,  # out_channels=16 表示 16 个扫描器同时扫描，对同一区域提取 16 个特征
                kernel_size=4,    # kernel_size 表示扫描器大小，即长、宽为 4
                stride=2,         # 扫描的速度，stride=2 表示扫描一个区域后，向右跳 2 个单位再扫描下一个区域
                padding=2),       # 把图片边缘围绕两圈 0，保证原始图片的边缘被扫描到
            
            # 输出 “ 图片 ” 的尺寸, out_size = (in_size - kernel_size + 2 * padding) / stride + 1 = (28 - 4 + 2 * 2) / 2 + 1 = 15
            
            nn.BatchNorm2d(16),   # 批标准化层：对每个区域输出的 16 个特征进行批标准化
            nn.ReLU(),            # 激活层
            nn.MaxPool2d(kernel_size=2, stride=1, padding=1)) # 池化层：用局部特征表示区域特征，局部特征可以取最大值、平均值等，具体参考文档
            # out_size = (15 - 2 + 2 * 1)/1 + 1 = 16
            
        self.layer2 = nn.Sequential(
            nn.Conv2d(
                in_channels=16,   # 上一层的输出 16 = 这一层的输入 16
                out_channels=32,  # 对同一区域扫描32次，输出32个特征
                kernel_size=5,    # 扫描器大小为 5 x 5
                stride=1,         # 扫描速度为 1
                padding=2),       # 把图片边缘围绕两圈 0，保证原始图片的边缘被扫描到
            # out_size = (16 - 5 + 2 * 2)/1 + 1 = 16
            
            nn.BatchNorm2d(32),   # 批标准化层：对每个区域输出的 16 个特征进行批标准化
            nn.ReLU(),            # 激活层
            nn.MaxPool2d(kernel_size=2, stride=2, padding=1)) # 池化层：用局部特征表示区域特征
            # out_size = (16 - 2 + 2 * 1)/2 + 1 = 9
            
        self.layer3 = nn.Linear(9*9*32, n_class) 
        
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = x.reshape(x.size(0), -1)
        x = self.layer3(x)
        return x

""" 实例化 ANN & 定义损失函数和优化算法 """
cnn = Model().to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(cnn.parameters(), lr=lr)

# 训练 ANN
total_step = len(train_loader)
for epoch in range(n_epoch):
    for i, (images, labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)
        
        # Output forward
        out = cnn(images)
        loss = loss_fn(out, labels)
        
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (i+1) % 100 == 0:
            print ('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}' 
                   .format(epoch+1, n_epoch, i+1, total_step, loss.item()))

# 测试 ANN
cnn.eval()
n_correct = 0
n_total = 0
for images, labels in test_loader:
    images = images.to(device)
    labels = labels.to(device)
    out = cnn(images)
    pred = torch.max(out.data, 1)[1]
    n_total += labels.size(0)
    n_correct += (pred == labels).sum().item()

print('Test Accuracy of the model on the 10000 test images: {} %'.format(100 * n_correct / n_total))