import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import LeaveOneOut
import torch
from torch import nn, optim
np.random.seed(1)
torch.manual_seed(1)

""" 定义参数 """
n_epoch = 1000
lr = 1e-3

""" 搭建 ANN """
class Model(nn.Module):
    def __init__(self, n_input, n_hidden, n_output):
        super(Model, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(n_input, n_hidden), nn.LeakyReLU())
        self.layer2 = nn.Linear(n_hidden, n_output)
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        return x

""" 导入数据集 """
char_df = pd.read_csv('E:\Work\Jupyter\data\char_data.csv')
char_nd = char_df.values
np.random.shuffle(char_nd)

""" 数据预处理 """
X = char_nd[:, 1:11].astype('float')
X = preprocessing.MinMaxScaler(feature_range=(0,1)).fit_transform(X)
y = char_nd[:, 11].astype('long')


""" 数据分割 """
G_G, G_NG, NG_NG, NG_G = 0, 0, 0, 0
for train,test in LeaveOneOut().split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    X_train = torch.tensor(X_train,requires_grad=True).float()
    X_test = torch.tensor(X_test,requires_grad=True).float()
    y_train = torch.tensor(y_train,requires_grad=False).long()
    y_test = torch.tensor(y_test,requires_grad=False).long()
    
    """ 实例化 ANN & 定义损失函数和优化算法 """
    n_input = 10
    n_hidden = 8
    n_output = 2
    bpnn = Model(n_input, n_hidden, n_output)
    loss_func = nn.CrossEntropyLoss()
    optimizer = optim.Adam(bpnn.parameters(), lr=lr)

    # 训练
    for epoch in range(n_epoch):
        
        # 向前传播
        out = bpnn(X_train)
        loss = loss_func(out, y_train)

        # 误差后传
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    # 测试       
    bpnn.eval()
    out = bpnn(X_test)
    loss = loss_func(out, y_test)
    pred = torch.max(out, 1)[1]
    num_correct = (pred == y_test).sum()    
    if y_test == 1:
        if num_correct == 1:
            G_G += 1
        if num_correct == 0:
            G_NG += 1
    if y_test == 0:
        if num_correct == 1:
            NG_NG += 1
        if num_correct == 0:
            NG_G += 1        

""" 输出结果 """            
print('Accuracy: {:.2f} %, Precision: {:.2f} %, Recall: {:.2f} %'
      .format((G_G+NG_NG)/68*100, G_G/(G_G + NG_G)*100, G_G/(G_G + G_NG)*100))