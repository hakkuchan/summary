import pandas as pd

char = pd.read_csv('E:\Work\Jupyter\data\char_data.csv')

""" 类型与维度 """
print(type(char))    # 输出中的DataFrame是pandas的一种数据结构
print(char.dtypes)   # 每列数据类型
print(char.shape)    # 表格维度
print(char.shape[1]) # 列数
print(char.shape[0]) # 行数 


""" 索引与切片 """
df = char.head(2)          # 前 2 行的数据 
df = char.tail(3)          # 后 3 行的数据
df = char.loc[0]           # 第 1 行数据
df = char.loc[0:3]         # 第 1~4 行数据
df = char.loc[[2,4,7]]     # 第 2,4,7 行数据
df = char[['C%','Ng']]     # 按列名切片

""" 按条件提取数据 """
df = char[char['Type'] == 1]
df = char[char['Ng'] > 10]

""" 添加新的一列 """
Ng_kg = char['Ng']/1000
char['Ng_kg'] = Ng_kg
char.head()


""" 运算 """
print(char['Ng']/100)           # 特定列名的数据除100
print(char['C%'] + char['H%'])  # 两列数据的运算


""" 统计 """
print(char.columns)           # 显示列名
print(char.columns.tolist())  # 列名转化为数组
print(char['Ng'].count())   # 列中数据个数

print(char['Ng'].max())     # 最大值
print(char['Ng'].min())     # 最小值
print(char['Ng'].mean())    # 平均值
print(char['Ng'].sum())     # 求和
print(char['Ng'].median())  # 中位数
print(char['Ng'].mode())    # 众数
print(char['Ng'].var())     # 方差
print(char['Ng'].std())     # 标准差
char.describe()             # 显示所有列的mean、std、min、四分位数、max


""" 缺失值处理 """
char.dropna(axis=1)                      # 删除有缺失值的样本
char.dropna(axis=0,subset=['H%', 'Ng'])  # 删除有缺失值的列


""" 表格转化为矩阵 """
char_df = char.values  # .values进行转换