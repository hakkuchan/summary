""" 1. 冒泡排序：
    
    · 多趟对列表中相邻数据进行比较，并将逆序的数据项互换位置，最终能将本趟的最大项就位
      经过n-1（n为列表中的数据个数）趟的比较交换，实现排序
    · 每趟过程类似于“气泡”在水中不断上浮的过程，故名为“冒泡排序”
    · 冒泡排序中对比数据的复杂度为 O(n^2)，交换数据的复杂度为 O(n^2)
"""
def bubble_sort(data):
    for compare_num in range(len(data)-1, 0, -1): 
        # compare_num为对比数据的次数，假如有n个数据，那么第一趟要对比 n-1 次
        # 第一趟对比之后，最大项已经位于列表末尾，那么第二趟要对比 n-2 次
        # 依次类推，每趟的对比次数是 n-1, n-2, ...... 1
        for i in range(compare_num):
            if data[i] > data[i+1]:  # 比较相邻数据
                data[i], data[i+1] = data[i+1], data[i]  # 如果逆序，则交换二者位置 

alist = [54, 26, 93, 16, 77, 31, 6, 55, 20]
bubble_sort(alist)
print(alist)  # >>> [6, 16, 20, 26, 31, 54, 55, 77, 93]



""" 2. 选择排序

    · 选择排序是对冒泡排序的改进，保留了其多趟比对的思路，每趟都使当前最大项就位
      但选择排序每趟仅进行1次交换（记录最大项的所在位置，最后再跟本趟最后一项交换）
    · 选择排序的对比复杂度为 O(n^2)，交换复杂度为 O(n)
"""
def select_sort(data):
    for compare_num in range(len(data)-1, 0, -1):
        max_pos = 0  # 初始化最大项的索引
        for i in range(1, compare_num+1):
            if data[i] > data[max_pos]:  # 如果第 i 个元素大于 data[max_pos]
                max_pos = i  # 令 i 为最大项的索引
        # 然后交换data[max_pos] 与 当前趟的末尾位置 data[compare_num]
        temp = data[compare_num]
        data[compare_num] = data[max_pos]
        data[max_pos] = temp

alist = [54, 26, 93, 17, 77, 31, 6, 55, 20]
select_sort(alist)
print(alist)  # >>> [6, 17, 20, 26, 31, 54, 55, 77, 93]



""" 3. 插入排序
    
    · 插入排序的比对主要用来寻找“新项”的插入位置
      第1趟，子列表仅包含第1个数据项，将第2个数据项作为“新项”插入到子列表的合适位置中，
      第2趟，再继续将第3个数据项跟前2个数据项比对，并插入到合适位置中
      经过n-1趟比对和插入，子列表扩展到全表，排序完成
    · 插入排序的对比复杂度为 O(n^2)
"""
def insert_sort(data):
    for i in range(1, len(data)):
        pos = i
        now_val = data[i]  # 新项
        while pos > 0 and data[pos-1] > now_val:  # 只要新项不在首位且新项前面有比它小的值
            data[pos] = data[pos-1]  # 调换新项与前一个项的位置
            pos = pos - 1
        data[pos] = now_val # 把新项插入合适的位置

alist = [54, 26, 93, 16, 77, 31, 6, 55, 20]
insert_sort(alist)
print(alist)  # >>> [6, 16, 20, 26, 31, 54, 55, 77, 93]



""" 4. 希尔排序
    
    · 希尔排序首先它把大数据集合分割成若干个小组（逻辑分组，即没有进行实际的分组操作），
      然后对每一个小组分别进行插入排序，此时由于插入排序所作用的数据量较小，插入的效率较高
    · 分组间隔由大变小，也就是说子列表元素由少变多，直至扩展到全部数据集
"""
def shell_sort(data):
    gap = len(data) // 2  # 设定间隔为全部数据的一半
    while gap > 0:
        for start in range(gap):
            gap_insert_sort(data, start, gap)  # 对每个子列表进行插入排序
        gap = gap // 2   # 将新一轮排序的间隔设定为当前间隔的一半

def gap_insert_sort(data, start, gap):  # 对子列表进行插入排序
    for i in range(start+gap, len(data), gap):
        pos = i
        now_val = data[i]
        while pos >= gap and data[pos-gap] > now_val:
            data[pos] = data[pos-gap]
            pos = pos - gap
        data[pos] = now_val

alist = [54, 26, 93, 16, 77, 31, 6, 55, 20]
shell_sort(alist)
print(alist)  # >>> [6, 16, 20, 26, 31, 54, 55, 77, 93]



""" 5. 归并排序
  
    · 归并排序分为两个过程：分裂和合并
      分裂是将数据表持续分为两半，对两半分别进行排序
      合并是将排好序的子表合并为总表
    · 分裂的复杂度为 O(log(n))，合并的复杂度为 O(n)，总复杂度为 O(nlog(n))
"""
def merge_sort(data):
    # 递归结束条件
    if len(data) <= 1:
        return data
    # 缩小问题规模，调用自身
    mid = len(data) // 2
    left = merge_sort(data[:mid])  # 对左半部分进行排序
    right = merge_sort(data[mid:]) # 对右半部分进行排序
    out = []
    # 合并左、右部分
    while left and right: # 只要 left 和 right 中有数据
        if left[0] <= right[0]: # 比较左半部分和右半部分第一个数据，并加入 out
            out.append(left.pop(0))
        else:
            out.append(right.pop(0))
    out.extend(left if left else right) # 如果最终左半部分或右半部分有剩余元素，整体加入 out
    return out

alist = [54, 26, 93, 16, 77, 31, 6, 55, 20]
merge_sort(alist)  # >>> [6, 16, 20, 26, 31, 54, 55, 77, 93]