""" 性能度量
    
    · sklearn中有三种方法评估模型的预测性能：
      (1) 模型自带的 .score()方法
      (2) model_selection.cross_val_score()方法
      (3) metrics模块
    
    · 方法(1),(2)见其它文档，本篇归纳方法(3) metrics模块
"""

from sklearn import metrics
from sklearn import datasets
from sklearn import svm
from sklearn import model_selection
from sklearn import preprocessing

""" 1. 分类指标 
       
       符号表：
       · TP: True Positive,  真正例 (1预测为1)
       · FP: False Positive, 假正例 (0预测为1)
       · TN: True Negative,  真反例 (0预测为0)
       · FN: False Negative, 假反例 (1预测为0) 
"""

# Data 1 (TP=1, FP=1, TN=1, FN=2)
real = [1,0,0,1,1]
pred = [1,1,0,0,0]

# (1) 准确率  accuracy = (TP+TN) / (TP+FP+TN+FN)
print(metrics.accuracy_score(real, pred))  # >>> 0.4

# (2) 查准率  precision = TP / (TP+FP)
print(metrics.precision_score(real, pred)) # >>> 0.5 

# (3) 查全率  recall = TP / (TP+FN)
print(metrics.recall_score(real, pred)) # >>> 0.3333333333333333

# (4) 查准率和查全率的调和值
#  a. FB值 (注：B设定的越大，查全率的贡献率越大)：
#     fbeta_score = 1 / {1/[(1+B^2)*precision] + B^2/[(1+B^2)*precision]}
print(metrics.fbeta_score(real, pred, beta=10))  # >>> 0.3344370860927152
print(metrics.fbeta_score(real, pred, beta=100)) # >>> 0.3344370860927152    
#  b. F1值  f1_score = 2 / (1/precision + 1/recall)
print(metrics.f1_score(real, pred)) # >>> 0.4

# Data 2：Iris
X = datasets.load_iris().data
y = datasets.load_iris().target
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=1) # 分割数据集
clf = svm.SVC(gamma='scale') # 设定分类器
clf.fit(X_train,y_train)     # 训练SVC
y_pred = clf.predict(X_test) # 预测

# (4) 分类报告
print(metrics.classification_report(y_test, y_pred))

# (5) 混淆矩阵
print(metrics.confusion_matrix(y_test, y_pred))



""" 2. 回归指标 """
# Toy data
real = [1.0, 2.0, 3.0, 4.0, 5.0]
pred = [1.2, 2.1, 3.3, 3.7, 5.2]

# (1) mean_absolute_error
print(metrics.mean_absolute_error(real, pred)) # >>> 0.21999999999999997

# (2) mean_squared_error
print(metrics.mean_squared_error(real, pred))  # >>> 0.05399999999999998

# (3) R^2
print(metrics.r2_score(real, pred)) # >>> 0.973