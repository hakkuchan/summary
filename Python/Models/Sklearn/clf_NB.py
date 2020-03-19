""" 朴素贝叶斯分类
    
    · 假定数据集有若干个类型，根据贝叶斯思想：
      P(type_i) : 样本为类型i的先验概率
      P(type_i | xi) : 当样本取值为xi、且样本为类型i的条件概率
    
    · 贝叶斯学习器的目标是学习一个贝叶斯公式，
      使训练集所有样本的 P(type_i | xi) 之和最大，
      进一步可用该公式预测测试集数据
      
    · 若假设条件概率符合：
      Gauss分布 → GaussianNB
      多项式分布 → MultinomialNB
      二项分布 → BernoulliNB
"""

from sklearn import datasets
from sklearn import naive_bayes
from sklearn import model_selection

# Data: digits
X = datasets.load_iris().data
y = datasets.load_iris().target

''' 建模并对比 '''
models = {}
# (1) GaussianNB 高斯贝叶斯分类器 （假设条件概率分布满足高斯分布）
models['Gauss'] = naive_bayes.GaussianNB() # 无超参数

# (2) MultinomialNB 多项式贝叶斯分类器（假设条件概率分布满足多项式分布）
models['Multi'] = naive_bayes.MultinomialNB(alpha=1.0, 
                                            fit_prior=True, 
                                            class_prior=None)

# (3) BernoulliNB 伯努利贝叶斯分类器（假设条件概率分布满足二项分布）
models['Bernoulli'] = naive_bayes.BernoulliNB(alpha=1.0,
                                              binarize=0.0,
                                              fit_prior=True,
                                              class_prior=None)

''' 结果 '''
for name in models:
    model = models[name]
    results = model_selection.cross_val_score(model, X, y, cv=10)
    print(f'Accuracy of {name} : {results.mean()*100:.2f}%')