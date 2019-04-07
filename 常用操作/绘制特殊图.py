import seaborn as sns
%matplotlib inline 

flights = sns.load_dataset('flights') # 导入自带的数据集，为csv格式
flights.head() # 查看数据(年，月，乘客量)

""" 风格设置 """
sns.set_style('whitegrid')
sns.set_style('darkgrid')
sns.set_style('white')
sns.set_style('dark')
sns.set_style('ticks')
sns.despine(left=True,top=False,right=True,bottom=True) #去掉坐标线

""" 单变分布--直方图 """
sns.distplot(flights['passengers'])                       # 画出直方图，横坐标默认为10个范围
sns.distplot(flights['passengers'],kde=False)             # 画出直方图，横坐标默认为10个范围,kde=False表示不画分布曲线
sns.distplot(flights['passengers'],bins=15,kde=False)     # bins=15表示横坐标分为15个范围

""" 特征间关系分析 """
sns.catplot(data=flights, x='year', y='passengers', kind='point') # 做散点图
sns.catplot(data=flights, x='year', y='passengers', hue='month',kind='point')  # 按不同月份做散点图（hue的用法）
sns.catplot(data=flights, x='year', y='passengers', col='month',kind='point')  # 按不同月份做散点图（col的用法）
sns.catplot(data=flights, x='year', y='passengers', kind='bar')   # 做柱形图(条形图)
sns.catplot(data=flights, x='year', y='passengers', kind='box')   # 做盒形图（弄清四分位距和离群点）
sns.catplot(data=flights, x='year', y='passengers', kind='strip')                    # 做分布图
sns.catplot(data=flights, x='year', y='passengers', kind='strip',jitter=True)        # 做分布图(使点分散)
sns.catplot(data=flights, x='year', y='passengers', kind='swarm')                    # 做分布图（使点按树形分散）

""" 特征两两作图（pairplot）"""
sns.pairplot(flights)     # 同时做出所有变量的两两之间的关系，对角线为直方图。！！！特征较多时不要这样做）

""" 联合分布（jointplot）"""
sns.jointplot(data=flights,x='year', y='passengers')              # 同时做出变量的直方图和两变量的关系图
sns.jointplot(data=flights,x='year', y='passengers',kind='hex')   # 用颜色深浅表示数据密度
sns.jointplot(data=flights,x='year', y='passengers',kind='reg')   # 做出拟合结果

""" 热力图（heatmap）"""
flights = flights.pivot('month','year','passengers') # 将DataFrame表格进行预处理
sns.heatmap(flights)                     # 绘制默认的热力图
sns.heatmap(flights,cbar=False)          # 隐藏colorbar
sns.heatmap(flights,vmin=0,vmax=700)     # 修改colorbar的范围
sns.heatmap(flights,annot=True,fmt='d')  # 将参数添加进图
sns.heatmap(flights,cmap='YlGnBu')       # 修改颜色