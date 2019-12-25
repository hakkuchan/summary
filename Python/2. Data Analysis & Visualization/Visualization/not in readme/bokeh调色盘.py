''' 调色盘 '''
# 颜色参考文档：http://bokeh.pydata.org/en/latest/docs/reference/palettes.html
# ColorBrewer：http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3

import bokeh.palettes as bp
from bokeh.palettes import brewer

# 查看所有调色板名称
print('所有调色板名称：\n',bp.__palettes__)
print(80*'-')

# 查看蓝色调色盘颜色
print('蓝色调色盘颜色：\n',bp.Blues)
print(80*'-')

# 调色盘解析 → 不同颜色解析最多颜色有限
n = 8
colori = brewer['Blues'][n]   
print(f'Blues可解析为{n}个颜色，分别为：{colori}')