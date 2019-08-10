""" 输出原始字符串 """
print('C:\some\name') 
print(r'C:\some\name')

""" 字符串的拼接 """
print(3 * 'a' + 'b') # 字符串可以用 + 进行连接，也可以用 * 进行重复

""" 相邻的两个或多个字符串字面值将会自动连接到一起 """
text = ('Put several strings within parentheses '
'to have them joined together.')
print(text)

""" 字符串索引和切片 (Python中的字符串不能被修改) """
s = 'Python'
print(s[0])   # >>> 'P'
print(s[-1])  # >>> 'n'
print(s[0:2]) # >>> 'Py'
print(s[2:5]) # >>> 'yto'
print(s[:2])  # >>> 'Py'

""" 序列的内置全局函数 (也适用于 list 和 tuple) """
s = 'pythonn'
print(len(s))
print(max(s))
print(min(s))
print(s.count('n'))  # .count(obj)方法：计算值的出现次数
print(s.index('n'))  # .index(obj)方法：从列表中找出某个值第一个匹配项的索引位置