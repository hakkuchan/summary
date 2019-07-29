# 测试单行语句执行 10e7次 的平均时间
%timeit a = 1+2+3+4+5

# 测试单行语句执行 1次 的时间
b = []
%time c = list(b.append(i) for i in range(10000))

%%timeit
# 测试整个单元中代码运行 10e7次 的平均时间
a = 1+2+3+4+5

%%time
# 测试整个单元中代码执行 1次的时间
b = []
c = list(b.append(i) for i in range(10000))