""" pickle.dump() 将对象以文件的形式存放在磁盘上。pickle.load() 读取文件 """

import pickle

''' 存储：pickle.dump() '''
data = {'a':[1,2,3,4], 'b':('string','abc'), 'c':'hello'} # 创建一个字典变量data
dirc = open( 'E:\\Work\\Jupyter\\Temp\\data.pkl', 'wb')   # 以二进制来存储： wb
pickle.dump(data, dirc)  # 将一个字典数据存成了pkl文件
dirc.close()

''' 读取：pickle.load() '''
f = open( 'E:\\Work\\Jupyter\\Temp\\data.pkl', 'rb') # 以二进制来读取：rb,
data = pickle.load(f)
print(data)