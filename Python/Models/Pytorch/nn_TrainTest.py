import torch
import torch.nn as nn
from sklearn import datasets, model_selection

''' 搭建 ANN '''
class MLP(nn.Module):
    def __init__(self, in_dim, n_hidden, out_dim):
        super(MLP, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(in_dim, n_hidden),
                                    nn.BatchNorm1d(n_hidden),
                                    nn.ReLU(True))
        self.layer2 = nn.Linear(n_hidden, out_dim)
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        return x

''' 导入数据集 '''
X = datasets.load_digits().data
y = datasets.load_digits().target

''' 分割数据集 '''
kfold = model_selection.KFold(n_splits=10)
progress = 1
print('|{:>5}|{:>15}|'.format('CV', 'Accuracy (%)'))
for train, test in kfold.split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    # 把 X 数据转换为 tensor，可导
    X_train = torch.tensor(X_train).clone().detach().requires_grad_(True).float()
    X_test = torch.tensor(X_test).clone().detach().requires_grad_(True).float()
    # 把 y 数据转换为 tensor，不可导
    y_train = torch.tensor(y_train).clone().detach().requires_grad_(False).long()
    y_test = torch.tensor(y_test).clone().detach().requires_grad_(False).long()
    
    ''' 初始化模型 (训练前进行)：实例化MLP / 定义损失函数 / 定义优化器 '''
    model = MLP(64, 50, 10)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    
    ''' 训练 ANN '''
    for epoch in range(200):
        # 向前传播：计算预测结果
        y_pred = model(X_train)
        label_pred = torch.max(y_pred, 1)[1]
        loss = criterion(y_pred, y_train)
        # 向后传播
        optimizer.zero_grad()   # 把优化器中的梯度清零，否则 pytorch 会累计每次误差梯度
        loss.backward()  # loss函数对其自变量求导
        optimizer.step() # optimizer根据 loss的导数对 ANN 中的参数进行更新

    ''' 测试 ANN '''
    model.eval()  # 把 model 转为测试模式
    # 预测
    y_pred = model(X_test)
    label_pred = torch.max(y_pred, 1)[1] 
    # 计算正确率
    num_correct = (label_pred == y_test).sum()    
    print(f'|{progress:>5}|{num_correct.item()/len(y_test)*100:>15.2f}|')
    progress += 1