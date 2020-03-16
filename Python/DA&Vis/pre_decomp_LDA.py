""" 线性判别分析（Linear Discriminant Analysis, LDA）
    
    · 核心思想：把高维数据的投影到低维数据
      并使在低维空间中，同类(y相同)数据尽可能靠近，而不同类(y不同)数据尽可能远离
"""

from sklearn import datasets
from sklearn import discriminant_analysis

# Data: Iris
iris = datasets.load_iris() # 150个样本，4个特征
X = iris.data
y = iris.target
# LDA降维
lda = discriminant_analysis.LinearDiscriminantAnalysis(solver='svd',   # 设置 solver
                                                       n_components=2) # 设置降维后的维度
Xr = lda.fit_transform(X, y) # 转换 X
print(Xr.shape) # >>> (150, 2)