""" 1. if 条件分支
    · if…… 
    · if…… else……  
    · if…… elif……
    · if…… elif…… else……  


    2. while 条件循环
    · while <逻辑表达式>
    · while <布尔条件>
    · while…… else……
    
    
    3. for 迭代循环
    · for i in range(num)
    · for i in [1, 2, 3]
    · for i, j in zip(['a', 'b'], [1, 2])  # 取出多个容器的元素
    · for i, j in enumerate(['a', 'b'])    # 取出索引和元素
    · for i, j in enumerate(['a', 'b'], 2) # 索引起始值从2开始
    
    
    4. break 和 continue 语句：
    · break 用于终止循环，执行循环之后的代码
    · continue 跳过当前循环的剩余语句，然后进行下一轮循环
    · break 和 continue 语句通常必须配合if语句使用
    · 慎用break和continue语句，因为它们会造成代码执行逻辑分叉过多，易出错
    · 大多数循环可通过改写循环条件或修改循环逻辑，代替break和continue语句


    5. pass 语句：
    · 当语法上需要一个语句，但需要程序不做任何操作时，可以使用 pass
"""
