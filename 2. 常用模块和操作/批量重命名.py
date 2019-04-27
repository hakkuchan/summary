import os

# 设置路径，注意 \\ 和 / 的使用
path='E:\\Other\\Downloads\\Pic/'      

# 提取路径下的所有文件 
f=os.listdir(path)

# 按照规则重命名
for num, item in enumerate(f):
    oldname=path+f[num]
    if oldname[25:26] == '.':
        newname= path + '00' + str(oldname[24:25])+'.JPG'  
        os.rename(oldname,newname)
    if oldname[26:27] == '.':
        newname= path + '0' + str(oldname[24:26])+'.JPG'
        os.rename(oldname,newname)
    if oldname[27:28] == '.':
        newname= path + str(oldname[24:27])+'.JPG'
        os.rename(oldname,newname)
print('Complete')