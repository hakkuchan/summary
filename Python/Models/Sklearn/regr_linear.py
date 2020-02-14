""" · 目录
    |
    |—— 1. 普通线性回归
    |
    |—— 2. 正则化的线性回归
    |   |
    |   |—— 2.1 Ridge回归
    |   |
    |   |—— 2.2 Lasso回归
    |   |
    |   |—— 2.3 ElasticNet回归
"""

from sklearn import linear_model

""" 1. 普通线性回归 """

# 建模
model = linear_model.LinearRegression(copy_X=True,         # 对 X 进行复制还是重写
                                      fit_intercept=True,  # 有无偏置项
                                      n_jobs=-1,           # 设置并行的CPU核数，-1为使用全部核
                                      normalize=False)     # 是否对回归参数标准化

# .fit(X,y) 回归
model.fit ([[0,0], [1,1], [2,2]], [0,1,2])    # [0,1,2] 也可写成 [[0],[1],[2]]

# .coef_ 获取权重向量
print(model.coef_)  # >>> [0.5 0.5]

# .intercept_ 获取偏置项
print(model.intercept_)  # >>> 2.220446049250313e-16

# .predict(X) 进行预测
print(model.predict([[3,3], [4,5]]))  # >>> [3.  4.5]

# 多元线性回归可能存在多个解，都能使均方误差最小化
# 且训练集输入参数会显著影响权重取值(病态)
X1 = [[0,0], [1,1], [2,2]]
X2 = [[0,0], [1,1.01], [2,1.99]]
y = [0, 1, 2]
print(model.fit(X1, y).coef_)  # >>> [0.5 0.5]
print(model.fit(X2, y).coef_)  # >>> [1.00000000e+00 2.11962482e-15]



""" 2. 正则化的线性回归模型
    
    · 纯线性回归模型的问题会使模型的解释性很差
      因此有必要把权重也作为目标函数的一部分，即引入正则化项
      这样做尽管有时会牺牲精度，但会使模型的解释性更好
    
    · 根据正则化项形式的不同，衍生出三种线性回归模型：Ridge，Lasso，ElasticNet
      （正则化项的具体公式见算法笔记）
"""

''' 2.1 Ridge回归 '''
model = linear_model.Ridge(alpha=0.5,  # 其值越大，正则化项占比越大
                           copy_X=True,
                           fit_intercept=True, 
                           max_iter=None,    # 参数优化的迭代次数，默认为 1000 
                           normalize=False, 
                           random_state=1,   # 设置随机种子
                           solver='auto',    # 参数估计的方法
                           tol=0.0001)       # 预测精度

X1 = [[0,0], [1,1], [2,2]]
X2 = [[0,0], [1,1.01], [2,1.99]]
y = [0, 1, 2]
print(model.fit(X1, y).coef_)  # >>> [0.44444444 0.44444444]
print(model.fit(X2, y).coef_)  # >>> [0.44648277 0.44411712]
# 可以看出，对于例子中的数据集，Ridge模型所得权重受输入参数的影响显著降低
# 但预测精度下降（权重的理论值是 [0.5, 0.5]）


''' 2.2 Lasso回归 '''
model = linear_model.Lasso(alpha= 0.1,
                           copy_X=True, 
                           fit_intercept=True, 
                           max_iter=1000,
                           normalize=False, 
                           positive=False,     # 权重向量是否强制为正数
                           precompute=True,    # 是否使用 precomputed Gram matrix 加速运算
                           random_state=None,
                           selection='cyclic', # 迭代时选择权重向量的哪个分量进行更新
                           tol=0.0001,  # 迭代收敛与否的阈值 
                           warm_start=False)   # 为True时表示使用前一次训练结果继续训练，否则从头开始训练

X1 = [[0,0], [1,1], [2,2]]
X2 = [[0,0], [1,1.01], [2,1.99]]
y = [0, 1, 2]
print(model.fit(X1, y).coef_)  # >>> [0.85 0.  ]
print(model.fit(X2, y).coef_)  # >>> [0.85 0.  ]
# 可以看出，对于例子中的数据集，Lasso模型所得权重不受输入参数的影响
# 但预测精度显著降低（权重的理论值是 [0.5, 0.5]）


''' 2.3 ElasticNet回归 '''
model = linear_model.ElasticNet(alpha=1.0,  # L1范数正则化项的比重
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

X1 = [[0,0], [1,1], [2,2]]
X2 = [[0,0], [1,1.01], [2,1.99]]
y = [0, 1, 2]
print(model.fit(X1, y).coef_)  # >>> [0.09091128 0.09090784]
print(model.fit(X2, y).coef_)  # >>> [0.09306092 0.08758369]
# 可以看出，对于例子中的数据集，ElasticNet模型所得权重受输入参数的影响显著降低
# 但预测精度也有所降低（权重的理论值是 [0.5, 0.5]）