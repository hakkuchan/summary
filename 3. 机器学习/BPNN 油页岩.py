import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score
import torch
from torch import nn, optim
%matplotlib inline
np.random.seed(1)
torch.manual_seed(1)

""" 导入数据集 """
oilshale_df = pd.read_csv('E:\Work\Jupyter\data\oilshale_data.csv')
oilshale_nd = oilshale_df.values
np.random.shuffle(oilshale_nd)

""" 数据预处理 """
bond = oilshale_nd[:,1:10].astype('float')
temp = oilshale_nd[:,10].reshape(-1,1).astype('float')
time = oilshale_nd[:,11].reshape(-1,1).astype('float')
bond_dist = preprocessing.Normalizer(norm='l1').fit_transform(bond)
temp_scale = preprocessing.MinMaxScaler(feature_range=(0,1)).fit_transform(temp)
time_scale = preprocessing.MinMaxScaler(feature_range=(0,1)).fit_transform(time)
X = np.concatenate((bond_dist, temp_scale, time_scale), axis=1) # X = 键分布 + 归一化温度 + 归一化时间
y = oilshale_nd[:,12].astype('float')

""" 搭建 ANN """
class Model(nn.Module):
    def __init__(self, n_input, n_hidden, n_output):
        super(Model, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(n_input, n_hidden), nn.Sigmoid())
        self.layer2 = nn.Linear(n_hidden, n_output)
    def forward(self, X):
        X = self.layer1(X)
        X = self.layer2(X)
        return X

""" 分割数据集 """
kfold = KFold(n_splits=10, random_state=False)
progress, r2_list, loss_list, calcd_val, exptl_val = 0, [], [], [], []
for train,test in kfold.split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    X_train = torch.tensor(X_train,requires_grad=True).float()
    y_train = torch.tensor(y_train,requires_grad=False).float()
    X_test = torch.tensor(X_test,requires_grad=True).float()
    y_test = torch.tensor(y_test,requires_grad=False) .float()
    
    # 实例化 ANN & 定义损失函数和优化算法
    bpnn = Model(11, 10, 1)
    loss_func = nn.MSELoss()
    optimizer = optim.Adam(bpnn.parameters(), lr=1e-2)
    
    # 训练 ANN
    for epoch in range(10000):
        
        # output forward
        out = bpnn(X_train)
        loss = loss_func(out, y_train.view(-1,1))
        
        # error backward
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    # 测试 ANN
    bpnn.eval()
    out = bpnn(X_test)
    loss = loss_func(out, y_test.view(-1,1)).detach().numpy()
    r2 = r2_score(y_test.numpy(),out.view(1,-1).detach()[0].numpy())
    loss_list.append(loss)
    r2_list.append(r2)
    exptl_val.append(y_test.view(-1,1))
    calcd_val.append(out.view(1,-1).detach()[0].numpy())
    progress += 10
    print('Finished: {}%' .format(progress), end='\r')

""" 输出结果 """
print('Mean MSE: {:.4f} ± {:.4f} ' .format(np.array(loss_list).mean(), np.array(loss_list).std()))
print('Mean R^2: {:.4f} ± {:.4f}' .format(np.array(r2_list).mean(), np.array(r2_list).std()))