import math
import pandas as pd
import pickle


""" 1. 读写表格文件 """

''' (1) 读csv '''
oilshale_table = pd.read_csv('E:\Work\Jupyter\data\char_data.csv')

''' (2) 读excel '''
oilshale_table = pd.read_excel('E:\Work\Jupyter\data\char_data.xls')

''' (3) 添加表头 '''
name = ['preg','plas','pres','skin','test','mass','pedi','age','class'] 
diabetes_table = pd.read_csv('E:\Work\Jupyter\data\pima-indians-diabetes.csv',names=name)

name = ['NO','preg','plas','pres','skin','test','mas','pedi','age','class']
diabetes_table = pd.read_excel('E:\Work\Jupyter\data\pima-indians-diabetes.xls', names=name)

''' (4) 将 Dataframe 格式写入csv或excel文件，index=True 保留行索引 '''
oilshale_table.to_csv('E:\Work\Jupyter\data\write_csv.csv', index=True)
oilshale_table.to_excel('E:\Work\Jupyter\data\write_excel.xls', index=True)


""" 2. 读写文本文件 """

''' (1) 读取 '''
with open(r'E:\Work\Jupyter\Data\read_text.txt', 'r') as f:
    data = f.read()  # .read() 表示读取文件整体
print(data)

with open(r'E:\Work\Jupyter\Data\read_text.txt', 'r') as f:
    for line in f:
        print(line)  # 逐行读取 
    
''' (2) 写入 '''
with open(r'E:\Work\Jupyter\Data\write_text.txt', 'w') as f:
    print('Hello World!', file=f, end=' ')    # end 控制换行，默认换行
    print(math.pi, math.e, file=f, sep='|')   # sep 设定打印元素之间的符号，默认为空格

''' (3) 总结:
        (I)  with open('文件目录', '指针') as f: 创造上下文环境，with 控制块结束时，文件会自动关闭。
        (II) 指针规定文件操作类型，常用如下：
             r: 读取文件，若文件不存在则会报错
             w: 写入文件，若文件不存在则会先创建再写入，会覆盖原文件
             a: 写入文件，若文件不存在则会先创建再写入，但不会覆盖原文件，而是追加在文件末尾
'''


""" 3. 其它对象的读写 —— pickle模块 """

''' (1) pickle.dump() 将对象以文件的形式存储在磁盘上'''
data = {'a':[1,2,3,4], 'b':('string','abc'), 'c':'hello'}  # 创建一个字典变量data
dirc = open(r'E:\Work\Jupyter\Data\data.pkl', 'wb')  # 设置存储路径为 dirc，'wb'表示以二进制存储
pickle.dump(data, dirc)  # 将一个字典数据存成了pkl文件
dirc.close()

''' (2) pickle.load() 读取文件 '''
f = open(r'E:\Work\Jupyter\Data\data.pkl', 'rb') # 'rb'表示以二进制读取
data = pickle.load(f)
print(data)