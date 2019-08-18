""" 普通函数转化为 ufunc """
x = np.arange(0,1000000,1)

''' 定义函数 '''
def square_fn(x, a, b):
    return a * x + b

''' 如果要把 x 中的每个数带入函数，需用循环语句 '''
%time print(type([square_fn(i, 2, 1) for i in x]))

''' 
更好的方法是：利用 frompyfunc 把原始函数转化为 ufunc，
    好处1：比循环语句快得多，计算量越大，差距越明显；
    好处2：输出为 ndarray 格式而非 list
'''
np_square_fn = np.frompyfunc(square_fn, 3, 1) # 其中 3 表示函数输入参数为 3 个，1 表示输出参数为 1 个
%time print(type(np_square_fn(x, 2, 1)))