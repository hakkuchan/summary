import numpy as np
import itertools

param_idx = np.array([1,2,3,4,5])

# 有序排列
for comb in itertools.combinations(param_idx, 3):
    print(list(comb))

# 无序排列（全排列）
for comb in itertools.permutations(param_idx, 3):
    print(list(comb))
	
# 对若干列表中的元素进行有序排列
comb = list(itertools.product([1,2,3], [4,5,6], [7,8,9]))
print(comb)