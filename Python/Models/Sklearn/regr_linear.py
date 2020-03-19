""" · 目录
    |
    |—— 1. 普通线性回归
    |
    |—— 2. 正则化的线性回归
    |   |
    |   |—— 2.1 Ridge
    |   |
    |   |—— 2.2 Lasso
    |   |
    |   |—— 2.3 ElasticNet
"""

from sklearn import datasets
from sklearn import linear_model
from sklearn import model_selection
from sklearn import metrics
from sklearn import preprocessing

""" 1. 普通线性回归 
    
    对给定数据集{[x1 y1], [x2 y2], ……} (x包含n个特征)，
    普通线性回归试图学得 y = w1x1 + w2x2 + …  wn*xn + b 来预测 y
"""

''' Example 1 '''
# Toy data
X = [[0,0], [1,1], [2,2]]
y = [0,1,2]
# 建模
model = linear_model.LinearRegression(copy_X=True,         # 对 X 进行复制还是重写，默认True
                                      fit_intercept=True,  # 有无 bias，默认True
                                      n_jobs=-1,           # 设置并行CPU核数，-1为使用全部核，默认 None
                                      normalize=False)     # 是否对回归参数标准化，默认False
# 训练模型
model.fit(X, y)
# 输出权重
print(model.coef_)  # >>> [0.5 0.5]
# 输出截距
print(model.intercept_)  # >>> 2.220446049250313e-16
# 预测
print(model.predict([[3,3], [4,5]]))  # >>> [3.  4.5]

''' Example 2: Boston housing price '''
# Data: Boston housing price
X = datasets.load_boston().data
X = preprocessing.MinMaxScaler(feature_range=(0,1)).fit_transform(X)
y = datasets.load_boston().target
# 建模并预测
model = linear_model.LinearRegression()
kfold = model_selection.KFold(n_splits=10, random_state=1)
r2 = metrics.make_scorer(metrics.r2_score)
out = model_selection.cross_val_score(model, X, y, cv=kfold, scoring=r2)
print(f'R^2 = {out.mean():.4f} ± {out.std():.4f}')

''' Example 3: 病态问题

    多元线性回归可能存在多个使均方误差最小化的解，
    且训练集的输入参数会显著影响权重
'''
# Toy data
X1 = [[0,0], [1,1], [2,2]]
X2 = [[0,0], [1,1.01], [2,1.99]]
y = [0, 1, 2]
model = linear_model.LinearRegression()
print(model.fit(X1, y).coef_)  # >>> [0.5 0.5]
print(model.fit(X2, y).coef_)  # >>> [1.00000000e+00 2.11962482e-15]



""" 2. 正则化的线性回归模型
    
    · 由于普通线性回归模型的病态问题
      因此有必要把权重也作为目标函数的一部分，故而引入正则化项 (一个关于权重的函数)
      这样做尽管有时会牺牲精度，但会使模型(权重)的解释性更好
    
    · 根据正则化项形式的不同，衍生出三种线性回归模型：Ridge，Lasso，ElasticNet
"""

''' 2.1 Ridge '''
# Toy data
X1 = [[0,0], [1,1], [2,2]]
X2 = [[0,0], [1,1.01], [2,1.99]]
y = [0, 1, 2]
# 建模
model = linear_model.Ridge(alpha=1,  # alpha越大，正则化项占比越大，默认为 1
                           copy_X=True,
                           fit_intercept=True, 
                           max_iter=None,   # 参数优化的迭代次数，默认为 None，具体值取决于solver
                           normalize=False, 
                           random_state=1,  # 设置随机种子
                           solver='auto',   # 参数估计的方法，默认为 'auto'
                           tol=0.001)       # 预测精度，默认为 0.001

# 输出权重
print(model.fit(X1, y).coef_)  # >>> [0.44444444 0.44444444]
print(model.fit(X2, y).coef_)  # >>> [0.44648277 0.44411712]
# 可以看出，Ridge模型所得权重受输入参数的影响显著降低，但预测精度下降


''' 2.2 Lasso '''
# Toy data
X1 = [[0,0], [1,1], [2,2]]
X2 = [[0,0], [1,1.01], [2,1.99]]
y = [0, 1, 2]
# 建模
model = linear_model.Lasso(alpha= 0.1, # 默认为 1.0
                           copy_X=True, 
                           fit_intercept=True, 
                           max_iter=1000,
                           normalize=False, 
                           positive=False,     # 权重向量是否强制为正数，默认为False
                           precompute=True,    # 是否使用 precomputed Gram matrix 加速运算
                           random_state=None,
                           selection='cyclic', # 迭代时选择权重向量的哪个分量进行更新，默认为 'cyclic'
                           tol=0.0001,         # 迭代收敛与否的阈值，默认为 0.0001
                           warm_start=False)   # 为True时表示使用前一次训练结果继续训练，否则从头开始训练，默认为False
# 输出权重
print(model.fit(X1, y).coef_)  # >>> [0.85 0.  ]
print(model.fit(X2, y).coef_)  # >>> [0.85 0.  ]
# 可以看出，Lasso模型所得权重受输入参数的影响显著降低，但预测精度下降


''' 2.3 ElasticNet回归 '''
# Toy data
X1 = [[0,0], [1,1], [2,2]]
X2 = [[0,0], [1,1.01], [2,1.99]]
y = [0, 1, 2]
# 建模
model = linear_model.ElasticNet(alpha=1.0,     # L1范数正则化项的比重
                                l1_ratio=0.5,  # L2范数正则化项的比重
                                fit_intercept=True, 
                                normalize=False, 
                                precompute=False, 
                                max_iter=1000, 
                                copy_X=True, 
                                tol=0.0001, 
                                warm_start=False, 
                                positive=False, 
                                random_state=None, 
                                selection='cyclic')
# 输出权重
print(model.fit(X1, y).coef_)  # >>> [0.09091128 0.09090784]
print(model.fit(X2, y).coef_)  # >>> [0.09306092 0.08758369]
# 可以看出，ElasticNet模型所得权重受输入参数的影响显著降低，但预测精度下降