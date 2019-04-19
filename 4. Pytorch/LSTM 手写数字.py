import torch 
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

# Device configuration
device = torch.device('cuda:0')

# Hyper-parameters
seq_len = 28   # 设定 28 个时间点
input_size = 28  # 每个时间点传入数据的维度
# MNIST中的图片维度是 28 * 28，相当于每次把 1 行数据依次传入 RNN，共传入 28 次
hidden_size = 128  # 隐藏层节点数
num_layers = 2     # LSTM 的层数，num_layers=2 表示第一层的输出等于第二层的输入，以此类推
num_classes = 10   # 10分类任务
batch_size = 100   # 批训练个数
num_epochs = 2     # 迭代轮数
learning_rate = 0.01  # 学习率

# MNIST dataset
train_dataset = torchvision.datasets.MNIST(root='E:\Work\Jupyter\data',
                                           train=True, 
                                           transform=transforms.ToTensor(),
                                           download=False)

test_dataset = torchvision.datasets.MNIST(root='E:\Work\Jupyter\data',
                                          train=False, 
                                          transform=transforms.ToTensor())

# Data loader
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size, 
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size, 
                                          shuffle=False)

# Recurrent neural network (many-to-one)
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, 
                            num_layers, 
                            batch_first=True
                           )
        self.fc = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):       
        # Forward propagate LSTM
        out, _ = self.lstm(x, None)  # out: tensor of shape (batch_size, seq_len, hidden_size)
        
        # Decode the hidden state of the last time step
        out = self.fc(out[:, -1, :])
        return out

model = RNN(input_size, hidden_size, num_layers, num_classes).to(device)


# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
total_step = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        images = images.reshape(-1, seq_len, input_size).to(device)
        labels = labels.to(device)
        
        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (i+1) % 100 == 0:
            print ('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}' 
                   .format(epoch+1, num_epochs, i+1, total_step, loss.item()))

# Test the model
with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in test_loader:
        images = images.reshape(-1, seq_len, input_size).to(device)
        labels = labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    print('Test Accuracy of the model on the 10000 test images: {} %'.format(100 * correct / total))