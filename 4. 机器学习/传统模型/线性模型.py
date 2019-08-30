from sklearn import linear_model

""" 1. 普通最小二乘法 (目标函数：||y-Xw||^2_2) """
''' (1) 模型 '''
model = linear_model.LinearRegression(copy_X=True,         # 对 X 进行复制还是重写
                                      fit_intercept=True,  # 设置有无偏置项
                                      n_jobs=-1,           # 设置并行的 CPU 核数，-1为全部核
                                      normalize=False)     # 是否对回归参数进行标准化 
''' (2) .fit(X,y) 进行回归 '''
model.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2]) # [0, 1, 2] 也可写成 [[0],[1],[2]]
''' (3) .coef_ 获取权重向量 '''
print(model.coef_)
''' (4) .intercept_ 获取偏置项 '''
print(model.intercept_)
''' (5) .predict(X) 进行预测'''
print(model.predict([[0.5, 0.5], [1.5, 1.5]]))


""" 2. 岭回归 (目标函数：||y-Xw||^2_2 + alpha * ||w||^2_2) """
model = linear_model.Ridge(alpha=0.5,  # 设置岭系数
                           copy_X=True, 
                           fit_intercept=True, 
                           max_iter=None,    # 参数优化的迭代次数，默认为 1000 
                           normalize=False, 
                           random_state=1,   # 设置随机种子
                           solver='auto',    # 参数估计的方法
                           tol=0.0001)       # 预测精度
model.fit ([[0, 0], [0, 0.1], [1, 1]], [0, .1, 1]) # [0, 1, 2] 也可写成 [[0],[1],[2]]
print(model.coef_)
print(model.intercept_)
print(model.predict([[0.5, 0.5], [1.5, 1.5]]))


""" 3. Lasso回归 (目标函数：(1/(2*n_samples))*||y-Xw||^2_2+alpha*||w||_1) """
model = linear_model.Lasso(alpha=1.0, 
                           copy_X=True, 
                           fit_intercept=True, 
                           max_iter=1000,
                           normalize=False, 
                           positive=False, 
                           precompute=True,    # 是否使用 precomputed Gram matrix 加速运算
                           random_state=None,
                           selection='cyclic', # 
                           tol=0.0001, 
                           warm_start=False)
model.fit ([[0, 0], [0, 0.1], [1, 1]], [0, .1, 1]) # [0, 1, 2] 也可写成 [[0],[1],[2]]
print(model.coef_)
print(model.intercept_)
print(model.predict([[0.5, 0.5], [1.5, 1.5]]))


""" 4. 弹性网回归
       (目标函数：1/(2*n_samples)*||y-Xw||^2_2+alpha*l1_ratio*||w||_1+0.5*alpha*(1-l1_ratio)*||w||^2_2）
       (在很多特征互相联系的情况时非常有用)
       """

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
model.fit ([[0, 0], [1, 1], [4, 4]], [0, .1, 1]) # [0, 1, 2] 也可写成 [[0],[1],[2]]
print(model.coef_)
print(model.intercept_)
print(model.predict([[0.5, 0.5], [1.5, 1.5]]))