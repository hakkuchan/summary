""" 
有时导入库时会显示警告信息，
比如废用特性或使用问题,
可以通过如下方法屏蔽，

"""

import warnings
warnings.filterwarnings('ignore') # 不发出警告

""" 关于警告的更多信息，可参考 cookbook 中 14.11 输出警告信息 """