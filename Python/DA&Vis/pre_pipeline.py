""" Pipeline
    
    · 用于把多个方法组成流水线，比如：数据标准化 → 特征选择 → 预测模型
    · 除预测模型外，其它方法必须含有transform 或 fit_transform 方法
"""

from sklearn import datasets
from sklearn import pipeline
from sklearn import feature_selection
from sklearn import decomposition
from sklearn import preprocessing
from sklearn import svm
from sklearn import model_selection

# Data：Iris
X = datasets.load_iris().data
y = datasets.load_iris().target
# 特征工程
features = []
features.append(('Select_best', feature_selection.SelectKBest(k=3))) # 选择3个指标
features.append(('PCA', decomposition.PCA(n_components=2))) # 降维至2个指标
features.append(('Standardize', preprocessing.StandardScaler())) # 正态分布化
# 设置流水线步骤
steps = []
steps.append(('feature_union',pipeline.FeatureUnion(features))) # 特征工程
steps.append(('Predictive model', svm.SVC(gamma='auto'))) # 预测模型
# 执行流水线
pipeline = pipeline.Pipeline(steps) # 此时可把pipeline理解为一个包含流水线功能的大模型
kfold = model_selection.KFold(n_splits=10,random_state=1)
result = model_selection.cross_val_score(pipeline,X,y,cv=kfold)
print('Accuracy:', round(result.mean(),4))