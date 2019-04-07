""" 1. 两种等价方法 """
print ('Sample: [{}], Progress: [{}/{}], Loss: {:.4f}' .format(6,100,1000,0.005), end='\r')
print(f'Sample: [{6}], Progress: [{100}/{1000}], Loss: {0.005:.4f}',end='\r')
# end = '\r': 覆盖上一行
# end = '\n': 换行
# end = ''  : 不换行


""" 2. 自制表格 """

# Example 1：
print('          |{:>10}|{:>10}|{:>10}|{:>10}|'.format('a','b','c','r2'))
print('Real curve|{:>10.0f}|{:>10.0f}|{:>10.0f}|{:>10}|'.format(1,3,1,'/'))

# Example 2：
a = [1,2,3]
print('|{:>16}|{:>16}|{:>16}|'.format('a','b','c'))     # : 之后的 > 表示右对齐，< 表示左对齐；16 表示间隔为 16 个字符
print(f'|{a[0]:>16.2f}|{a[1]:>16.2f}|{a[2]:>16.2f}|')   # 16 后面的 .2 表示小数点后两位，f 表示 float


""" 3. %操作符 """
print('The value of pi is approximately %.3f.' % math.pi)