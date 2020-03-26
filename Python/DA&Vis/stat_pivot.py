""" 4. 透视表 pivot_table """
# values：要聚合的列或列的列表
# index：数据透视表的index，从原数据的列中筛选
# columns：数据透视表的columns，从原数据的列中筛选
# aggfunc：用于指定函数，支持 numpy 中的 ufunc 函数，默认为 np.mean。
date = ['2017-5-1','2017-5-2','2017-5-3'] * 3
rng = pd.to_datetime(date)
df = pd.DataFrame({'date':rng, 'key':list('abcabcabc'), 'values':np.random.rand(9)*10})
print(df)
print(pd.pivot_table(df, values='values', index='date', columns='key', aggfunc=np.mean)) # 统计不同[date,key]下values的mean
print(pd.pivot_table(df, values='values', index = ['date','key'], aggfunc=np.mean))