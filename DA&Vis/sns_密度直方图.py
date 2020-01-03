import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


''' 1. 绘制直方图 - displot '''
rs = np.random.RandomState(0)  # 设定随机数种子
s = pd.Series(rs.randn(1000)*100)
sns.distplot(s,
             bins=50,          # 箱数
             hist=True,        # 显示箱
             kde=True,         # 显示密度曲线
             norm_hist=False,  # 是否按照密度来显示直方图
             rug=False,        # 是否显示数据分布情况
             vertical=False,   # 是否水平显示
             color='red',      # 设置颜色
             label='distplot', # 设置图例
             axlabel='x')      # axlabel → x轴标注
plt.legend()
plt.show()

# 详细设置 
sns.distplot(s,
             hist_kws={"histtype": "step", # 设置箱子的风格
                       "linewidth": 1,     # 设置箱子的线宽
                       "alpha": 1,         # 设置箱子的透明度
                       "color": "g"},      # 设置箱子的颜色
             kde_kws={"color": "k",        # 设置密度曲线颜色
                      "lw": 1,             # 设置密度曲线线宽
                      "label": "KDE",      # 设置密度曲线标注
                      'linestyle':'--'},   # 设置密度曲线线形
             rug = True, rug_kws = {'color':'b'})  # 设置数据频率分布颜色
plt.show()


''' 2、密度图 - kdeplot() '''
rs = np.random.RandomState(0)  # 设定随机数种子
s = pd.Series(rs.randn(1000)*100)

sns.kdeplot(s,
            shade=False,    # 是否填充
            color='r',      # 设置颜色
            vertical=False  # 设置是否水平
            )

sns.kdeplot(s,
            bw=5,             # 控制拟合的程度
            label="bw:0.2",
            linestyle='-',
            linewidth=2,
            alpha=0.5)

sns.kdeplot(s,
            bw=20, 
            label="bw: 2",
            linestyle='-',
            linewidth=1.2,
            alpha=0.5)

sns.rugplot(s, height=0.1, color='k', alpha=0.5) # 数据频率分布图

plt.show()


''' 3、双样本密度图 - kdeplot() '''
# 两个维度数据生成曲线密度图，以颜色作为密度衰减显示

rs = np.random.RandomState(1)  # 设定随机数种子
df = pd.DataFrame(rs.randn(100,2), columns = ['A','B'])
sns.kdeplot(df['A'],df['B'],
            cbar=True,    # 是否显示颜色图例
            shade=True,   # 是否填充
            cmap='Reds',  # 设置调色盘
            shade_lowest=False,  # 最外围颜色是否显示
            n_levels=10          # 曲线个数（如果非常多，则会越平滑）
            )

sns.rugplot(df['A'], color="g", axis='x', alpha=0.5)  # 注意设置 x 轴
sns.rugplot(df['B'], color="r", axis='y', alpha=0.5)  # 注意设置 y 轴
plt.show()

''' 4、多个双样本密度图 - kdeplot() '''
rs1 = np.random.RandomState(1)  
rs2 = np.random.RandomState(2)  
df1 = pd.DataFrame(rs1.randn(100,2)+2,columns = ['A','B'])
df2 = pd.DataFrame(rs2.randn(100,2)-2,columns = ['A','B'])
sns.kdeplot(df1['A'], df1['B'], cbar=True, cmap='Reds', 
            shade=True, shade_lowest=False, n_levels=10)
sns.kdeplot(df2['A'], df2['B'], cbar=True, cmap='Blues', 
            shade=True, shade_lowest=False, n_levels=10)
plt.show()