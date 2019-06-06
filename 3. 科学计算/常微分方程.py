import sympy as sy


""" 例1 """
# f(x)' = x^2 
def diff_eq(x,f):
    return sy.diff(f(x),x,1) - x

x = sy.symbols('x')  # 约定变量
f = sy.Function('f') # 约定函数
sy.pprint(sy.dsolve(diff_eq(x,f),f(x))) # 输出 f(x)


""" 例2 """
# f(x)''+ f(x)=0
def diff_eq(x,f):
    return sy.diff(f(x),x,2) + f(x) 

x=sy.symbols('x')  # 约定变量
f=sy.Function('f') # 约定函数
sy.pprint(sy.dsolve(diff_eq(x,f),f(x))) # 输出 f(x)


""" 例3 """
# f(x)^(4) + 3*f(x)'' - x^3 = 0
def diff_eq(x,f):
    return sy.diff(f(x),x,4) + 3 * sy.diff(f(x),x,2) - x**3

x=sy.symbols('x')  # 约定变量
f=sy.Function('f') # 约定函数
sy.pprint(sy.dsolve(diff_eq(x,f),f(x))) # 输出 f(x)