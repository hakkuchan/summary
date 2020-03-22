import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision import datasets

device = torch.device('cuda:0')

""" 设定超参数  """
batch_size = 32  # 表示更新一次参数所基于的梯度来自 32 个样本，假如有320个训练样本，那么一个 epoch 会依次更新 10 次
lr = 1e-2        # 学习率
n_epoch = 3      # 迭代次数，n_epoch = 1 表示只 “训练-测试” 一遍

""" 准备数据集 """
train_dataset = datasets.MNIST(root='E:\Work\Jupyter\Data\MNIST', train=True, transform=transforms.ToTensor(), download=True)
test_dataset = datasets.MNIST(root='E:\Work\Jupyter\Data\MNIST', train=False, transform=transforms.ToTensor())
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

""" 搭建 ANN 模型 """
class Model(nn.Module):
    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super(Model, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(in_dim, n_hidden_1),
                                    nn.BatchNorm1d(n_hidden_1),
                                    nn.ReLU(True))
        self.layer2 = nn.Sequential(nn.Linear(n_hidden_1, n_hidden_2),
                                    nn.BatchNorm1d(n_hidden_2),
                                    nn.ReLU(True))
        self.layer3 = nn.Sequential(nn.Linear(n_hidden_2, out_dim))
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return x

""" ANN实例化 & 定义损失函数和优化算法 """
bpnn = Model(28 * 28, 300, 100, 10).to(device)    # 对 Model 类进行实例化
loss_func = nn.CrossEntropyLoss()      # 定义损失函数
optimizer = optim.Adam(bpnn.parameters(), lr=lr)    # 定义优化器

""" 进行 n_epoch 次 “训练-测试” 中的第 epoch 次 """
for epoch in range(n_epoch):
    print('epoch {}'.format(epoch + 1))
    train_loss, train_acc = 0.0, 0.0
    
    # 训练 ANN
    for i, data in enumerate(train_loader, 1):
        img, label = data
        img = img.view(img.size(0), -1)   # 对图片格式进行转化
        img = img.clone().detach().requires_grad_(True).to(device)    # 使参数可自动微分
        label = label.clone().detach().requires_grad_(False).to(device)
        
        # 向前传播
        out = bpnn(img)    # 首先计算预测值
        loss = loss_func(out, label)  # 然后计算 n 个预测值与真实值的平均偏差
        train_loss += loss.item() * label.size(0)    # 计算总偏差
        pred = torch.max(out,1)[1]   
        # 解析：输出层有10个节点，每个节点代表一个数字，
        # 每次预测出的 out 是一个 1行10列 的 tensor，比如[-8.2, -4.6, -8.9, -2.6, 8.3, -4.1, -8, 2.9, -4.6, 0.3]
        # 最大值对应的索引就是所预测的数字，比如上述 out 的最大值的索引为 4，所以这个 out 对应的预测数字是 4.
        # torch.max(out,1)表示返回每个 out 的最大值 [0] 及其索引 [1]
        # 因此 pred = torch.max(out,1)[1] 就是返回一个Batch中的预测结果
        num_correct = (pred == label).sum() # 计算一个batch中预测对了多少个样本
        train_acc += num_correct.item()   # 计算总正确率
         
        # 向后传播
        optimizer.zero_grad()   # 把优化器中的梯度清零，否则 pytorch 会累计每次误差梯度
        loss.backward()     # loss函数对其自变量求导
        optimizer.step()    # optimizer根据 loss的导数对 ANN 中的参数进行更新

        if i % 300 == 0:    # 每训练 300 组数据，输出一下预测指标
            print('[{}/{}] Loss: {:.4f}, Acc: {:.4f}'
                  .format(epoch + 1, n_epoch, train_loss / (batch_size * i),train_acc / (batch_size * i)))
    
    print('Finish {} epoch: Loss: {:.4f}, Acc: {:.4f}' # 输出所有训练集样本训练完成后，总的预测指标
          .format(epoch + 1, train_loss / (len(train_dataset)), train_acc / (len(train_dataset))))
    
# 测试 ANN
bpnn.eval()
eval_loss = 0.0
eval_acc = 0.0
for data in test_loader:
    img, label = data
    img = img.view(img.size(0), -1)
    img = img.clone().detach().requires_grad_(True).to(device)
    label = label.to(device)
    out = bpnn(img)
    loss = loss_func(out, label)
    eval_loss += loss.item() * label.size(0)
    pred = torch.max(out, 1)[1]
    num_correct = (pred == label).sum()
    eval_acc += num_correct.item()
print('Test Loss: {:.4f}, Acc: {:.4f}' # 输出测试集上的训练结果
      .format(eval_loss / (len(test_dataset)), eval_acc / (len(test_dataset))))