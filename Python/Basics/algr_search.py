""" 1. 顺序查找
    
    · 如果数据保存在线性数据结构中，可以按照顺序查找数据项，
      即从第1个数据项开始，逐个对比数据项，
      如果匹配，返回数据项(及位置)，
      如果未发现待查数据，返回False
    
    · 比对次数决定了复杂度，即 O(n) 复杂度
"""



""" 2. 二分查找
    
    · 二分查找适用于有序表，即从有序表中间开始比对，
      待查数据如果小于中间的数，就把查找范围缩小至前半段，否则缩小至后半段
      依次类推
    
    · 二分查找为 log(n) 复杂度
"""

def binary_search(alist,item): 
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if alist[mid] == item:
            found = True
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

testlist = [0, 1, 2, 3, 4, 5, 6]
print(binary_search(testlist, 5))