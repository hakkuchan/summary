import itertools

# 有序排列
for comb in itertools.combinations([1,2,3,4,5], 3):
    print(list(comb))
print()

# 全排列
for comb in itertools.permutations([1,2,3,4,5], 3):
    print(list(comb))
print()

# 对若干列表中的元素进行有序排列
comb = list(itertools.product([1,2,3], [4,5,6], [7,8,9]))
print(comb)
