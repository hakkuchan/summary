""" 1. 概述
    (1) python有2种数值类型：int（整型）, float（浮点型);
    (2) int(), float() 用来分别创建int和float类型数值;
    (3) bool型是int型的子类，bool(0) = False, bool(任何非零数) = True。
"""


""" 2. 简单数值运算包括:
    (1) 加(+)、减(-)、乘(*)、除(/)、乘方（**）
    (2) 整除（//）：5 // 2 = 2， type(5 // 2) >> int
    (3) 取余（%）：5 % 2 = 1，type(5 % 2) >> int
"""


""" 3. 内置运算函数 """
num = -51.2
print(abs(num)) # 取绝对值
print(round(num, 2))   # 四舍五入至小数点后两位
print(round(num, 0))   # 四舍五入至个位
print(round(num, -1))  # 四舍五入至十位
print(round(num, -2))  # 四舍五入至百位


""" 4. math 模块 (注：math中所有函数的返回值都是float型) """
import math 

''' (1) 特殊常数 '''
e = math.e
pi = math.pi

''' (2) 常用计算 '''
print(math.trunc(2.9))   # 返回num整数部分 
print(math.ceil(1.2))    # 返回不小于num的最小整数
print(math.floor(10.9))  # 返回 ≦ num的最大整数
print(math.factorial(5)) # 返回5的阶乘
print(math.gcd(17,51))   # 返回两个数的最大公约数
print(math.log(e**3))    # 求以e为底数，num的对数，即 ln(num)
print(math.log(81,3))    # 以a为底数，num的对数(记忆:逗号后面是底数)
print(math.log2(16))     # 以2为底数，num的对数
print(math.log10(1000))  # 以10为底数，num的对数

''' (3) 其余运算见math文档 '''