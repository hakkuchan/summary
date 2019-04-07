import pandas as pd

data = pd.read_csv('E:\Work\Jupyter\data\char_data.csv') # 读取csv格式

eg：# 添加表头
name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\DataAnalysis\Library\pima-indians-diabetes.csv',names=name)

data.to_csv('123.csv', index=True)  # 将 data (Dataframe格式) 写入csv文件，index=True 保留行索引