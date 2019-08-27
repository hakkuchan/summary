""" 1. 测试一段代码的运行时间 """
import time
start = time.time()
for i in range(10000000):
    pass
end = time.time()
print(f'{end-start:.4f} s')

""" 2. 测试单行语句执行 10e7次 的平均时间 """
%timeit a = 1+2+3+4+5

""" 3. 测试单行语句执行 1次 的时间 """
%time a = list(i for i in range(10000))

""" 4. 测试 1 个 jupyter notebook 的 cell 中，代码运行 10e7 次的平均时间 """
%%timeit    
# %%timeit 必须放在 CEll 的开头
a = 1+2+3+4+5

""" 5. 测试 1 个 jupyter notebook 的 cell 中，代码执行 1 次的时间 """
%%time
# 注意：%%time 必须放在 CEll 的开头
a = list(i for i in range(10000))