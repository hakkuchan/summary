"""
1) python有2种数值类型：int（整型）, float（浮点型);
2) int(), float() 分别创建int和float类型数值;
3) bool型是int型的子类，bool(0) = False, bool(任何非零数) = True;
4) 常用数值运算: 加(+)、减(-)、乘(*)、除(/)、乘方（**）
                 整除（//）：5 // 2 = 2， type(5 // 2) >> int
                 取余（%）：5 % 2 = 1，type(5 % 2) >> int
"""
# 四舍五入：
num = 3.141592653
round(num, 2) # 四舍五入至小数点后两位
round(num, 0) # 四舍五入至个位
round(num, -1) # 四舍五入至十位
round(num, -2) # 四舍五入至百位

# 取绝对值：
abs(num)

import math 
""" math中所有函数的返回值都是float型 """


""" 特殊常数 """

e = math.e
pi = math.pi


""" 常用计算 """
 
math.trunc(2.9) # 返回num整数部分

math.ceil(1.2)  # 返回不小于num的最小整数

math.floor(10.9)  # 返回 ≦ num的最大整数

math.factorial(5) # 返回5的阶乘

math.gcd(17,51)   # 返回两个数的最大公约数

math.log(e**3)    # 求以e为底数，num的对数，即 ln(num)

math.log(81,3)    # 以a为底数，num的对数(记忆:逗号后面是底数)

math.log2(16)     # 以2为底数，num的对数

math.log10(1000)  # 以10为底数，num的对数

# 三角函数和双曲函数详见math文档