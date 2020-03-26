""" 因子分析

    · 因子分析是从多个变量中提取公共因子(通常不可测量)的方法，是一种降维技术
      例如：变量 x1 ~ x5 分别表示：收缩压、舒张压、心跳间隔、呼吸间隔、舌下温度
      从医学知识可知，这5个指标受人体交感神经和副交感神经支配，但这两种神经的状态无法直接测定
      根据因子分析，可首先假设 s1 和 s2 分别为 "交感神经状态参数" 和 "副交感神经状态参数"
      然后把去中心化的 x1 ~ x5 (xm1 ~ xm5) 表示为 s1 和 s2 的线性函数(偏置项表示其它影响因素)
      具体如下：
              xm1 =  a11*s1 + a12*s2 + e1
              xm2 =  a21*s2 + a22*s2 + e2
              xm3 =  a31*s3 + a32*s2 + e3
              xm4 =  a41*s4 + a42*s2 + e4
              xm5 =  a51*s5 + a52*s2 + e5
      
    · 因子分析可分为：验证性因子分析 & 探索性因子分析
      验证性：先假设公共因子的个数(及物理意义)，验证假设是否成立
      探索性：不确定公共因子的个数，通过探索寻找到公共因子
      本篇以验证性因子分析为主
    
    · 目录
    |
    |—— 1. 充分性检验
    |
    |—— 2. 验证性因子分析
    |   |
    |   |—— 2.1 确定公共因子个数
    |   |
    |   |—— 2.2 因子分析
"""

import numpy as np
import pandas as pd
import factor_analyzer
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline


# Data: Boston housing price
X = datasets.load_boston().data 
y = datasets.load_boston().target.reshape(-1,1)
data = np.concatenate((X,y), axis=1)
names=['00犯罪率','01宅用地比例','02商用地比例','03临近河道','04NO浓度', '05房间数', '06自用房比例',
       '07到城区距离', '08交通便利指数', '09税率', '10师生比例', '11黑人比例', '12低收入比例', '13房价']
df = pd.DataFrame(X, columns=names[:-1])


""" 1. 充分性检验：检测数据集中是否可提取出公共因子
       所用方法为"MKO检验"和"巴特利特球度检验"，都是检验各变量之间相关性的方法 
"""
# 方法 1：MKO检验 (Kaiser-Meyer-Olkin Test)
kmo = factor_analyzer.calculate_kmo(df)
print(kmo[1])  # >>> 0.8530376701576892 (大于0.6 说明可做因子分析)
# 方法 2：巴特利特球度检验 (Bartlett's sphericity Test)
bartlett = factor_analyzer.calculate_bartlett_sphericity(df)
print(bartlett[0]) # >>> 4474 (需要自行把握是否大于显著性水平，若小于预期显著性水平，则不可做因子分析)



""" 2. 验证性因子分析 """

''' 2.1 确定公共因子个数 '''
# 由于不确定公共因子个数，故令 n_factors = 变量总数
fa = factor_analyzer.FactorAnalyzer(n_factors=13, rotation=None)
fa.fit(df)
# 计算特征值 (从特征值大小可判断公共因子个数)
eigval, eigvec = fa.get_eigenvalues()
plt.scatter(range(1,df.shape[1]+1),eigval)
plt.plot(range(1,df.shape[1]+1),eigval)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigen Value')
plt.grid()
plt.show()

''' 2.2 因子分析 '''
fa = factor_analyzer.FactorAnalyzer(n_factors=4, rotation="varimax") 
# 因子旋转(rotation)：重新分配各个因子所解释的方差比例，使其载荷系数更接近 1 或 0，便于解释和命名公共因子
fa.fit(df)
# 载荷系数矩阵 (原始变量和公共因子的线性关系)
load = fa.loadings_
print(load.shape) # >>> (13, 4)
# 公共因子与原始变量的相关性分析 (从图中可以看出公共因子和哪些变量相关性高)
load_df = pd.DataFrame(np.abs(load), index=df.columns) # 为突出相关性，此处对载荷系数矩阵求绝对值
plt.figure(figsize=(6,6))
ax = sns.heatmap(load_df, annot=True, cmap="BuPu")
ax.yaxis.set_tick_params(labelsize=15)
plt.title('Factor Analysis')
plt.ylabel('Sepal Width')
plt.show()
# 降维后的变量
Xr = fa.fit_transform(X)
print('Shape of X:', X.shape)
print('Shape of Xr:', Xr.shape)