""" 处理 csv 文件 """
import pandas as pd
# 读取 csv 文件为 dataframe 格式
data = pd.read_csv('E:\Work\Jupyter\data\char_data.csv') 
# 如果需要添加表头：
name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\DataAnalysis\Library\pima-indians-diabetes.csv',names=name)

# 将 Dataframe 格式写入csv文件，index=True 保留行索引
data.to_csv('123.csv', index=True)



""" 读写文本文件 """

""" 打开 - 读取文件（注意 / 和 \ 的作用） """
with open('E:\Work\Jupyter/test.txt', 'r') as f: # 'r'表示以只读方式打开文件，还有其它选项，详见文档
    print(f.read()) # .read() 表示读取文件整体

with open('E:\Work\Jupyter/test.txt', 'r') as f:
    for line in f:
        print(line) # 逐行读取 

with open('E:\Work\Jupyter/test.txt', 'r') as f:
    for ele in f.read():
        print(ele)  # 逐字读取


""" 打开 - 写入文件"""
with open('E:\Work\Jupyter/test.txt', 'w') as f: # 'w'表示以写入模式
    for i in range(3):
        f.write(str(i))
        
with open('E:\Work\Jupyter/test.txt', 'r') as f: # 'w'表示以写入模式
    print(f.read())

"""
r : 读取文件，若文件不存在则会报错

w: 写入文件，若文件不存在则会先创建再写入，会覆盖原文件

a : 写入文件，若文件不存在则会先创建再写入，但不会覆盖原文件，而是追加在文件末尾

rb,wb：分别于r,w类似，但是用于读写二进制文件

r+ : 可读、可写，文件不存在也会报错，写操作时会覆盖

w+ : 可读，可写，文件不存在先创建，会覆盖

a+ ：可读、可写，文件不存在先创建，不会覆盖，追加在末尾

"""