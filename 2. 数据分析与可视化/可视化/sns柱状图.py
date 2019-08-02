""" 柱状图-barplot() """

''' 形式一： '''
titanic = sns.load_dataset("titanic")
print(titanic.head())
print('-----')

sns.barplot(x="sex", y="survived", hue="class", data=titanic,
            palette = 'hls', 
            order = ['male','female'],  # 筛选类别
            capsize = 0.05,  # 误差线横向延伸宽度
            saturation=.8,   # 颜色饱和度
            errcolor = 'gray',errwidth = 2,  # 误差线颜色，宽度
            ci = 'sd'    # 置信区间误差 → 0-100内值、'sd'、None
            )
print(titanic.groupby(['sex','class']).mean()['survived'])
print(titanic.groupby(['sex','class']).std()['survived'])
plt.show()


''' 形式二 '''
sns.barplot(x="day", y="total_bill", hue="sex", data=tips,
            palette = 'Blues',edgecolor = 'w')
tips.groupby(['day','sex']).mean()
plt.show()


''' 堆积柱状图 '''

crashes = sns.load_dataset("car_crashes").sort_values("total", ascending=False)
print(crashes.head())

f, ax = plt.subplots(figsize=(6, 15)) # 创建图表
# 设置第一个柱状图
sns.set_color_codes("pastel")
sns.barplot(x="total", y="abbrev", data=crashes,
            label="Total", color="b",edgecolor = 'w')
# 设置第二个柱状图
sns.set_color_codes("muted")
sns.barplot(x="alcohol", y="abbrev", data=crashes,
            label="Alcohol-involved", color="b",edgecolor = 'w')

ax.legend(ncol=2, loc="lower right")
sns.despine(left=True, bottom=True)
plt.show()


''' 计数柱状图 '''
# 用法和barplot相似
sns.countplot(x="class", hue="who", data=titanic, palette='magma')
plt.show()