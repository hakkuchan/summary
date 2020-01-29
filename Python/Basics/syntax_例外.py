""" 1. 例外：错误、警告、异常
    
    (1) 错误：也称为语法错误(SyntaxError)或解析错误，代码无法执行
    
    
    (2) 警告：有时导入库时会显示警告信息，比如废用特性或使用问题，可屏蔽
    
        import warnings
        warnings.filterwarnings('ignore') # 不发出警告
        
        # 关于警告的更多信息，可参考 cookbook 中 14.11 输出警告信息
    
  
    (3) 异常：语法正确，但执行时引发了错误
        
        · AttributeError：对象没有这个属性
        · DeprecationWarning：关于被弃用的特征的警告，更新一下anaconda所有的库即可 conda update --all
        · IndexError：下标越界
        · KeyError：映射（字典）中没有这个键
        · NameError：name 'xxx' is not defined 未声明对象
        · OverflowError：数值运算超出最大限制
        · TypeError：对类型无效的操作       
        · ZeroDivisionError：除以0导致错误
"""


""" 2. 异常处理（try…… except…… else…… finally……） """
# 例：
def test(m):
    try:  # 尝试执行 Try 子句，如无异常，跳过 except 子句，完成 try 子句的执行。
        print('Try……')
        print(10 / m)
    except TypeError:  # 如果异常类型和 except 后面的异常名匹配，则执行 except 子句
        print('Input has wrong type.')
    except ZeroDivisionError:
        print('Division by zero.')
    else:     # 如无异常，补充执行的代码
        print('No error.')
    finally:  # 无论是否出现异常，都会执行的代码
        print('End')

test(2)   # >>> 5.0 
test('a') # >>> Input has wrong type.
test(0)   # >>> Division by zero.

''' 一个 try 语句可能有多个 except 子句，以指定不同异常的处理程序
    如果没有匹配到异常处理程序，则它是一个未处理异常，程序中止
    如果可能发生多种异常，可以用一个 except 子句对应多个异常类型（用元组表示）
    例如：except (RuntimeError, TypeError, NameError)
'''