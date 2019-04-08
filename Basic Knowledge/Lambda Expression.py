""" lambda表达式可以定义一个匿名函数，例如： """

f = lambda x: x ** 2 + 2 * x
print('lambda expression:',f(2))

""" 上例的代码x为入口参数，x ** 2 + 2 * x 为函数体, 相当于："""
def g(x):
    return x ** 2 + 2 * x
print('traditional expression:',g(2))