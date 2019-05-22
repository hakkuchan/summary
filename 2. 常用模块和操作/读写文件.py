""" 读写表格文件 """
import math
import pandas as pd

# 读取 csv 文件
oilshale_table = pd.read_csv('E:\Work\Jupyter\data\char_data.csv')
# 读取 excel 文件
oilshale_table = pd.read_excel('E:\Work\Jupyter\data\char_data.xls')

# 如果需要添加表头：
name = ['preg','plas','pres','skin','test','mass','pedi','age','class']
diabetes_table = pd.read_csv('E:\Work\Jupyter\data\pima-indians-diabetes.csv',names=name)

name = ['NO','preg','plas','pres','skin','test','mas','pedi','age','class']
diabetes_table = pd.read_excel('E:\Work\Jupyter\data\pima-indians-diabetes.xls', names=name)

# 将 Dataframe 格式写入csv或excel文件，index=True 保留行索引
oilshale_table.to_csv('E:\Work\Jupyter\data\write_csv.csv', index=True)
oilshale_table.to_excel('E:\Work\Jupyter\data\write_excel.xls', index=True)


""" 读写文本文件 """

# 读取
with open('E:\Work\Jupyter\data/read_text.txt', 'r') as f:
    data = f.read()  # .read() 表示读取文件整体
print(data)

with open('E:\Work\Jupyter\data/read_text.txt', 'r') as f:
    for line in f:
        print(line)  # 逐行读取 
    
# 写入
with open('E:\Work\Jupyter\data/write_text.txt', 'w') as f:
    print('Hello World!', file=f, end=' ')    # end 控制换行，默认换行
    print(math.pi, math.e, file=f, sep='|')   # sep 设定打印元素之间的符号，默认为空格


# 读写文本文件的总结：

# with open('文件目录', '指针') as f: 创造上下文环境，with 控制块结束时，文件会自动关闭。

# 文件目录中的 ‘\’ 和 ‘/’ 需要区分：目录之间用‘\’；文件与目录之间用‘/’，例如：'E:\Work\Jupyter\data/write_text.txt'

# 指针规定文件操作类型，常用如下：
 
# r : 读取文件，若文件不存在则会报错

# w: 写入文件，若文件不存在则会先创建再写入，会覆盖原文件

# a : 写入文件，若文件不存在则会先创建再写入，但不会覆盖原文件，而是追加在文件末尾

