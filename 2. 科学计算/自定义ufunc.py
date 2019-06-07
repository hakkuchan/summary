""" 普通函数转化为 ufunc """
x = np.arange(0,10000,1)
# 普通函数
def square_fn(x, a, b, c):
    return a * x**2 + b * x + c

# 如果要把 x 中的每个函数带入函数，需要循环语句
%time y = [square_fn(i, 3, 2, 1) for i in x]

# 利用 frompyfunc 转化为 ufunc
np_square_fn = np.frompyfunc(square_fn, 4, 1) # 其中 4 表示函数输入参数为 4 个，1 表示输出参数为 1 个
%time y = np_square_fn(x, 3, 2, 1)
# 注: frompyfunc 比循环语句快得多，计算量越大，差距越明显