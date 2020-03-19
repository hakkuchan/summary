""" 集成分类器
    
    · 原理：生成一组个体分类器，用一定策略将它们结合起来，再进行预测
    
    · 分类：结合个体分类器的策略主要有两类：Boosting 和 Bagging
      Boosting策略中的个体分类器之间存在强依赖关系，而Bagging反之
    
    · 个体分类器的选择准则：1) 预测能力不能太差；2) 个体分类器之间要有差异
    
    · 目录
    |
    |—— 1. Boosting
    |   |
    |   |—— 1.1 Adaboost
    |   |
    |   |—— 1.2 GBDT
    |
    |
    |—— 2. Bagging
        |
        |—— 2.1 bagging
        |
        |—— 2.2 Random Forest
        |
        |—— 2.3 Extra tree
        |
        |—— 2.4 Voting
"""


from sklearn import datasets
from sklearn import ensemble
from sklearn import naive_bayes, svm, tree
from sklearn import model_selection

# Data: Iris
X = datasets.load_iris().data
y = datasets.load_iris().target


""" 1. Boosting

       Step 1：先从初始训练集训练出一个个体分类器
       Step 2：根据其预测表现对训练样本的分布进行调整，使被预测错误的样本在后续收到更多关注
       Step 3：基于调整后的样本训练出下一个个体分类器
       Step 4：重复Step 2、3，直至个体分类器个数达到指定值
       Step 5：对所有训练好的个体分类器进行加权结合
"""

''' 1.1 Adaboost (Adaptive Boosting, 自适应增强)
    思想: 先给每个样本赋予权值(1/N, N为样本总数)，在训练过程中调高分类错误的样本权值，降低分类正确的样本权值
'''
base = naive_bayes.GaussianNB() # 构建单个分类器
model = ensemble.AdaBoostClassifier(base_estimator=base, # 设定单个分类器，默认为决策树
                                    n_estimators=20,     # 设定单个分类器的个数，默认为50
                                    learning_rate=0.1,   # 设定步长，该参数值越小，n_estimator需调大
                                    random_state=1 # 随机种子
                                   )
kfold = model_selection.KFold(n_splits=10, random_state=1)
result = model_selection.cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
print(f'Accuracy of Adaboost: {result.mean()*100:.2f}%')


''' 1.2 GradientBoostingClassifier 梯度提升决策树 (GBDT)
    思想：用初始样本训练1个个体分类器后，用y_real与y_pred的残差作为新的y，训练下一个个体分类器
'''
model = ensemble.GradientBoostingClassifier(n_estimators=30, random_state=1)
kfold = model_selection.KFold(n_splits=10,random_state=2)
result = model_selection.cross_val_score(model,X,y,cv=kfold)
print(f'Accuracy of GBDT: {result.mean()*100:.2f}%')



""" 2. Bagging

    · 显然，Boosting策略受到数据集的影响较大，
      为了获得更好的泛化能力，有必要使个体分类器尽可能独立
    
    · Bagging策略：
      Step 1：对给定数据集进行采样，获得N个子数据集(可以有交集)
      Step 2：用N个子数据集训练N个个体分类器
      Step 3：将所有个体分类器并行结合，对分类任务采用投票法预测
"""

''' 2.1 BaggingClassifier (实现基本的Bagging策略) '''
base = tree.DecisionTreeClassifier()
model = ensemble.BaggingClassifier(base_estimator=base,
                                   n_estimators=10,
                                   random_state=1)
kfold = model_selection.KFold(n_splits=20,random_state=1)
result = model_selection.cross_val_score(model,X,y,cv=kfold)
print(f'Accuracy of Bagging: {result.mean()*100:.2f}%')


''' 2.2 RandomForestClassifier 随机森林 (RF) 
    思想：在Bagging策略的基础上，构建决策树时，随机选择特征作为节点
'''
model = ensemble.RandomForestClassifier(n_estimators=30, random_state=1)
kfold = model_selection.KFold(n_splits=10,random_state=1)
result = model_selection.cross_val_score(model,X,y,cv=kfold)
print(f'Accuracy of RF: {result.mean()*100:.2f}%')


''' 2.3 ExtraTreesClassifier 极端随机树 (ET)
        思想: ET是RF的变种，其区别在于采用全部数据集训练个体分类器，且节点选择随机、树算法选择随机
'''
model = ensemble.ExtraTreesClassifier(n_estimators=100,
                                      max_features=4,
                                      random_state=3)
kfold = model_selection.KFold(n_splits=10,random_state=1)
result = model_selection.cross_val_score(model,X,y,cv=kfold)
print(f'Accuracy of ET: {result.mean()*100:.2f}%')


""" 2.4 Voting算法 
        思想：设置多种不同个体分类器，使用投票法进行预测
"""
base1 = tree.DecisionTreeClassifier()
base2 = svm.SVC(gamma='auto')
base3 = naive_bayes.GaussianNB()

bases = []
bases.append(('Decision Tree',base1))
bases.append(('SVC',base2))
bases.append(('Naive Bayes', base3))

model = ensemble.VotingClassifier(estimators=bases)
kfold = model_selection.KFold(n_splits=10,random_state=1)
result = model_selection.cross_val_score(model,X,y,cv=kfold)
print(f'Accuracy of Voting: {result.mean()*100:.2f}%')