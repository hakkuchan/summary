""" 1. 模块（module)：包含Python代码的.py文件（包含了函数、特殊值等）"""

''' (1) 导入现有模块 (以math模块为例) '''
import math
import math as m
print(type(math))  # >>> <class 'module'>

from math import *  # 导入模块内定义的所有内容
# 不要使用这个功能，因为它在解释器中引入了一组module内的名称，它们很可能会覆盖一些你已经定义过的东西 '''

from math import pi  # 导入模块中的某个值
print(type(pi))  # >>> <class 'float'>

from math import log as ln  # 导入模块中的某个函数
print(type(ln))  # >>> <class 'builtin_function_or_method'>

# 注意事项：
# a) 只能逐句import，不能 from math import log, log10 as ln, lg
# b)也不能 import math.log as ln （import A.B 的语法不适用于module，只适用于package）


''' (2) 导入自定义module（比如 my_module.py）

    方法1：查看现有包（如pandas）所在路径，将my_module.py存入该路径
    import pandas
    print(pandas.__file__)

    方法2：假如 my_module.py 的保存路径为 E:/Work，先添加其位置：
    import sys
    sys.path.append('E:/Work/')
    之后便可 import my_module
'''

''' (3) 查看模块 '''
dir(math)  # 查看模块中的所有方法名
help(math) # 查看文档

''' (4) 模块的选择型运行 (if __name__ == '__main__': 的作用)

    · Python 是解释型语言，从脚本第一行开始运行。
      导入一个模块（本质上，一个 .py 文件）时，程序会从模块顶层代码直接运行
        
    · 比如，有一个模块 hello_world.py
      其内容只有一行代码：print('Hello world !')
 
      import hello_world
      会直接输出：Hello world ！
 
      显然，我们只希望引入 hello_world 模块，不希望运行其中的代码
      因此，把 hello_world.py 改写为：

      if __name__ == '__main__':
          print('Hello world !')

      此时就只引入模块，而不运行模块中 if __name__ == '__main__': 后面的代码

    · __name__ 是当前文件的内置变量，存储着当前模块（.py 文件）的名字
      当模块被运行时，当前模块名是 __main__，因此 __name__=='__main__' is True，于是执行之后的代码，
      当模块（比如 hello_world.py）被引入时，模块名是 hello_world. 因此 __name__=='__main__' is False，便不执行之后的代码。
      简言之，if __name__ == '__main__': 的作用判断当前模块是在被运行还是被引入，进而选择性执行之后的代码
'''



""" 2. 包 (package)：包含了多个module或子包(内含module和子包)的文件夹，比如sklearn """    

''' (1) 导入(以 sklearn 为例) '''
import sklearn  # 直接导入
import klearn.preprocessing  # 导入内部模块或子包，可以连续(如A.B.C)
import sklearn.preprocessing as preproecss
from sklearn import preprocessing as preprocess
''' from sklearn import *   不推荐，耗时且可能有副作用'''

''' (2) __init__.py 文件 
    
    · 包中必然包含__init__.py 文件，其作用是将普通文件夹变为一个包，
      在导入一个包时，实际上是导入了其 __init__.py 文件，
      这样我们可以在 __init__.py 文件中批量导入我们所需要的模块，而不再需要一个一个的导入
    
    · __init__.py 一般是一个空文件，也可在其中定义一个列表 __all__
      若定义了列表 __all__，from package import * 时，就会导入package的所有列表名(显式)，
      如果没有这个定义，就只导入package
      
    · 例：
      
      from sklearn import *
      
      sklearn中的 __init__.py 文件含有 __all__列表，那么就可以直接用其中的module，比如 preprocessing
      a = preprocessing.MinMaxScaler()
                
      反之，假如 sklearn 中的 __init__.py文件 没有__all__列表，
      那么 from sklearn import * 后，依然不能直接使用其中的 module
'''