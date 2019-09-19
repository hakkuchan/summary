from sklearn import linear_model

""" 1. 基于最小二乘法的线性回归模型 """

''' 建模 '''
model = linear_model.LinearRegression(copy_X=True,         # 对 X 进行复制还是重写
                                      fit_intercept=True,  # 设置有无偏置项
                                      n_jobs=-1,           # 设置并行的 CPU 核数，-1为全部核
                                      normalize=False)     # 是否对回归参数进行标准化 
''' fit(X,y) 进行回归 '''
model.fit ([[0,0], [1,1], [2,2]], [0,1,2])    # [0,1,2] 也可写成 [[0],[1],[2]]
''' .coef_ 获取权重向量 '''
print(model.coef_)
''' .intercept_ 获取偏置项 '''
print(model.intercept_)
''' .predict(X) 进行预测'''
print(model.predict([[3,3], [4,5]]),'\n')

''' 需要注意：上述线性模型求出的权重不是唯一的，且训练集的输入参数会显著影响权重取值（病态）。 '''
print('普通线性回归模型:')
model.fit ([[0,0], [1,1], [2,2]], [0,1,2])
print(f'X1：{[[0,0], [1,1], [2,2]]}, 权重：{model.coef_}')
model.fit ([[0,0], [1,1.1], [2,1.9]], [0,1,2])
print(f'X2：{[[0,0], [1,1.01], [2,1.99]]}, 权重：{model.coef_}', '\n')

''' 如此一来，模型的解释性会很差，因此有必要把权重也作为目标函数的一部分；
    尽管有时会牺牲精度，但会使模型的解释性更好；
    根据目标函数中所添加权重项的形式不同，可衍生出三种线性模型：Ridge，Lasso，ElasticNet，目标函数分别如下：
        Ridge：||y-Xw||^2_2 + alpha*||w||^2_2
        Lasso：(1/(2*n_samples))*||y-Xw||^2_2 + alpha*||w||_1
        ElasticNet：1/(2*n_samples)*||y-Xw||^2_2 + alpha*l1_ratio*||w||_1 + 0.5*alpha*(1-l1_ratio)*||w||^2_2
    可以看出，可以把 Ridge，Lasso，ElasticNet 3种线性模型理解为最小二乘法线性模型的改良。 '''


""" 2. Ridge回归模型（岭回归）  """
model = linear_model.Ridge(alpha=0.5,  # 设置岭系数
                           copy_X=True, 
                           fit_intercept=True, 
                           max_iter=None,    # 参数优化的迭代次数，默认为 1000 
                           normalize=False, 
                           random_state=1,   # 设置随机种子
                           solver='auto',    # 参数估计的方法
                           tol=0.0001)       # 预测精度
print('Ridge回归模型:')
model.fit ([[0,0], [1,1], [2,2]], [0,1,2])
print(f'X1：{[[0,0], [1,1], [2,2]]}, 权重：{model.coef_}')
model.fit ([[0,0], [1,1.1], [2,1.9]], [0,1,2])
print(f'X2：{[[0,0], [1,1.01], [2,1.99]]}, 权重：{model.coef_}', '\n')
# 对比可知：Ridge模型所得权重受输入参数的影响显著降低，但预测精度也有所降低。 '''


""" 3. Lasso回归模型 (套索回归) """
model = linear_model.Lasso(alpha= 0.1,
                           copy_X=True, 
                           fit_intercept=True, 
                           max_iter=1000,
                           normalize=False, 
                           positive=False, 
                           precompute=True,    # 是否使用 precomputed Gram matrix 加速运算
                           random_state=None,
                           selection='cyclic', 
                           tol=0.0001, 
                           warm_start=False)
print('Lasso回归模型:')
model.fit ([[0,0], [1,1], [2,2]], [0,1,2])
print(f'X1：{[[0,0], [1,1], [2,2]]}, 权重：{model.coef_}')
model.fit ([[0,0], [1,1.1], [2,1.9]], [0,1,2])
print(f'X2：{[[0,0], [1,1.01], [2,1.99]]}, 权重：{model.coef_}', '\n')
# 对比可知：对于示例中的数据，Lasso模型所得权重不受输入参数的影响，但预测精度有显著降低。


""" 4. ElasticNet回归模型（弹性网回归） """
model = linear_model.ElasticNet(alpha=1.0, 
                                l1_ratio=0.5, 
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
print('ElasticNet回归模型:')
model.fit ([[0,0], [1,1], [2,2]], [0,1,2])
print(f'X1：{[[0,0], [1,1], [2,2]]}, 权重：{model.coef_}')
model.fit ([[0,0], [1,1.1], [2,1.9]], [0,1,2])
print(f'X2：{[[0,0], [1,1.01], [2,1.99]]}, 权重：{model.coef_}')
# 对比可知：ElasticNet模型所得权重受输入参数的影响显著降低，但预测精度也有所降低。