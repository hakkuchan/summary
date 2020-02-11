""" · 目录
    |
    |—— 1. Logistic回归
    |
    |—— 2. 线性判别分析
"""

from sklearn import datasets
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

""" 1. Logistic回归 """
# 准备数据
X, y = datasets.load_iris(return_X_y=True)
kfold = model_selection.KFold(n_splits=10, shuffle=True, random_state=2)
# 建模
model = LogisticRegression(penalty='l2',  # 指定罚项是 1范数还是 2范数
                           dual=False,    # 求解对偶形式还是原始形式（当 n_samples > n_features：dual=False）
                           tol=0.0001,    # 指定收敛与否的阈值
                           C=1.0,         # 罚项系数的倒数，其值越小，正则化项越大
                           fit_intercept=True,   # 是否需要计算偏置项
                           intercept_scaling=1,  
                           class_weight=None,    # 给出每个分类的权重
                           random_state=None,    # 设置随机种子
                           solver='newton-cg',   # 指定优化算法
                           max_iter=100,         # 指定最大迭代次数
                           multi_class='multinomial',  # 指定对于多分类问题的策略
                           verbose=0, 
                           warm_start=False,     # 是否使用前一次训练结果继续训练
                           n_jobs=None)   # 指定并行的 CPU 核数
# 数据分割
for train,test in kfold.split(X):
    X_train,X_test = X[train],X[test]
    y_train,y_test = y[train],y[test]
    # .fit() 训练模型 
    model.fit(X_train, y_train)
    # .predict() 模型预测
    print(model.predict(X_test))
    # .predict_proba() 把 X 预测为各个类型的概率
    print(model.predict_proba(X_test)[0])
    # .predict_log_proba() 把 X 预测为各个类型的概率的对数值
    print(model.predict_log_proba(X_test)[0])
    # 计算准确率
    print(f'Accuracy：{model.score(X_test, y_test)}', '\n')
# 计算十折交叉验证的平均准确率
out = model_selection.cross_val_score(model,X,y,cv=kfold)
print(f'Mean Accuracy：{out.mean():.4f} ± {out.std():.4f}')



""" 2. 线性判别分析（LDA） """
# 准备数据
X, y = datasets.load_iris(return_X_y=True)
kfold = model_selection.KFold(n_splits=10, shuffle=True, random_state=2)

# 建模
model = LinearDiscriminantAnalysis(n_components=None, # 指定降维后的维度，必须小于 n_classes-1
                                   priors=None,       # 指定每个类别的先验概率
                                   shrinkage=None,    # 通常在训练样本数少于特征数、solver = lsqr 或 eigen 时使用
                                   solver='lsqr',     # 指定最优化算法 
                                   store_covariance=False,  # 计算类别的协方差矩阵
                                   tol=0.0001) # 用于指定svd算法中收敛的阈值
# 数据分割
for train,test in kfold.split(X):
    X_train,X_test = X[train],X[test]
    y_train,y_test = y[train],y[test]
    # .fit() 训练模型 
    model.fit(X_train, y_train)
    # .predict() 模型预测
    print(model.predict(X_test)) 
    # .predict_proba() 把 X 预测为各个类型的概率
    print(model.predict_proba(X_test)[0])
    # .predict_log_proba() 把 X 预测为各个类型的概率的对数值
    print(model.predict_log_proba(X_test)[0])
    # 计算准确率
    print(f'Accuracy：{model.score(X_test, y_test)}', '\n')
# 计算十折交叉验证的平均准确率
out = model_selection.cross_val_score(model,X,y,cv=kfold)
print(f'Mean Accuracy：{out.mean():.4f} ± {out.std():.4f}')