num_1, num_2 = 100, 1000

""" format的用法 """
print('num:{:.4f}'.format(num_1)) # 设置输出精度
print('|{:>10}|{:>10}|'.format(num_1, num_2)) # 生成表格：{:>10} 表示格子宽10个字符，内容右对齐
print('|{:>10.3f}|{:>10.2f}|'.format(num_1, num_2))  # 既设置格子，又设置内容精度

""" 等价形式(推荐) """
print(f'num:{num_1:.4f}')
print(f'|{num_1:>10}|{num_2:>10}|')
print(f'|{num_1:>10.3f}|{num_2:>10.2f}|')

""" end的用法 """
# end = '\r': 覆盖上一行
# end = '\n': 换行
# end = ''  : 不换行