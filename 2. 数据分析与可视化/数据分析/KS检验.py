""" KS检验: 检验数据是否符合某种分布 """

import pandas as pd
from scipy import stats

# 样本数据，36位健康男性在未进食之前的血糖浓度
data = [87,77,92,68,80,78,84,77,81,80,80,77,92,86,76,80,81,75,
        77,72,81,72,84,86,80,68,77,87,76,77,78,92,75,80,78,85]
df = pd.DataFrame(data, columns=['blood sugar'])
ave = df['blood sugar'].mean()  # 计算均值
std = df['blood sugar'].std()  # 计算标准差

s = stats.kstest(df['blood sugar'],  # 数据
                 'norm',             # 检查是否服从正态分布（还可以检验泊松分布、t分布、卡方分布等等，用时再查文档）
                 (ave, std))         # 输入均值和标准差
print(s[:])  # 返回两个结果：D值 和 P值（p值大于0.05，为正态分布）