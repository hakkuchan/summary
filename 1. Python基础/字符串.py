""" 输出原始字符串（r）"""
print('C:\some\name') 
print(r'C:\some\name')

""" 字符串的拼接 """
# 字符串可以用 + 进行连接，也可以用 * 进行重复
print(3 * 'a' + 'b')

""" 相邻的两个或多个字符串字面值将会自动连接到一起 """
text = ('Put several strings within parentheses '
'to have them joined together.')
print(text)

""" 字符串索引和切片 """
word = 'Python'
word[0] = 'P'
word[5] = 'n'
word[-1] = 'n'
word[0:2] = 'Py'
word[2:5] = 'yto'
word[:2] = 'Py'
# Python中的字符串不能被修改

""" 字符串的长度 """
s = 'Python'
len(s) = 6