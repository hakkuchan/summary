""" 1. 数值类型

    · int(整型，即整数): 
      1) int(num) 创建int型数值
      2) Python不限制int型数值大小      
    · float(浮点型，即小数):
      1) 小数之所以也称为浮点数，是因为按照科学记数法表示时，小数点位置可变，比如，1.23e9 = 12.3e8
      2) float(num) 创建float型数值，float型数值最多有17位有效数字
      3) float型运算会有四舍五入的误差，因此比较两个浮点数是否相等，优先采用两者差值是否接近0的思路
    · 复数类型
      1) Python 中用 j 表示虚数，例如：3 + 2j
      2) 复数运算库：cmath 



    2. 数值进制
    
    · 几进制表示用几个不同符号来表示数，例如:
      二进制用 0，1 两个符号
      十进制用 0 ~ 9 九个符号
    · 二进制（binary）数前缀：0b  例如 0b10110111
      八进制（octal）数前缀：0o  例如 0o557
      十六进制（hexadecimal）数前缀：0x  例如 0x16f
    · 二进制转十进制：0b101 → 1*2^2 + 0*2^1 + 1*2^0 = 5
      其它进制转十进制的方法以此类推    
    · 十进制转二进制：用十进制数不断除以2，先得到的余数往后放，后得到的余数往前放，排列出的就是二进制数
      例如：十进制数4，先除以2，商2余0；2再除以2，商1余0；1再除以2，商0余1，所以二进制数为 0b100 
"""

# 进制转化函数
print(bin(5))   # 十进制 → 二进制
print(oct(10))  # 十进制 → 八进制
print(hex(17))  # 十进制 → 十六进制
print(int('0b11000',2))  # 二进制 → 十进制



""" 3. 数值(非复)运算 """
''' 3.1 运算符 '''
print(3 + 3)  # 加
print(3 - 3)  # 减
print(3 * 3)  # 乘
print(3 / 3)  # 除
print(3 ** 3) # 乘方
print(5 // 2) # 整除 >>> 2
print(5 % 2)  # 取余 >>> 1

''' 3.2 运算函数 '''
print(abs(-1.234))        # 取绝对值  >>> 1.234
print(round(51.234, 2))   # 四舍五入至小数点后两位 >>> 51.23
print(round(51.234, -2))  # 四舍五入至百位  >>> 100.0
print(divmod(5, 2))       # 同时整除和取余  >>> (2, 1)

''' 3.3 math模块 '''
import math 
# 特殊常数
e = math.e
pi = math.pi
# 常用计算
print(math.factorial(5)) # 返回5的阶乘  >>> 120
print(math.log(e**3))    # 求对数 (e为底数)  >>> 3
print(math.log(81, 9))   # 求对数 (3为底数)  >>> 2 
print(math.log2(16))     # 求对数 (2为底数)  >>> 4
print(math.log10(100))   # 求对数 (10为底数) >>> 2
print(math.trunc(2.9))   # 返回整数部分 >>> 2
print(math.ceil(1.2))    # 返回不小于num的最小整数 >>> 2
print(math.floor(10.9))  # 返回 ≦ num的最大整数  >>> 10
print(math.gcd(17,51))   # 返回两个数的最大公约数 >>> 17
# math中所有函数的返回值都是float型
# math模块还支持三角函数、双曲函数等运算
