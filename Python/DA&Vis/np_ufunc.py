''' 1. ufunc函数 (注：输出为 ndarray 对象) '''
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
y = np.sin(x)
y = np.cos(x)
y = np.tan(x)
y = np.exp(x)
y = x**2

''' 2. 自定义ufunc函数 (注：输出为 ndarray 对象)  '''
# 传统函数
def fn_test(x, a, b):
    return a * x^2 + b
# 生成 x 数据
x = np.arange(0,1000000,1)
# 对于传统函数，如果要把 x 中的每个数带入函数，需用循环语句
%time print(type([fn_test(i, 2, 1) for i in x]))  
# 更好的方法是：利用 frompyfunc 把原始函数转化为 ufunc，运算会作用于全部 x
# 比循环语句快得多，计算量越大，差距越明显
# ufunc的输出为 ndarray 格式
ufunc_test = np.frompyfunc(fn_test, 3, 1) # 其中 3 表示函数输入参数为 3 个，1 表示输出参数为 1 个
%time print(type(ufunc_test(x, 2, 1)))