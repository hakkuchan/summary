import numpy as np
import itertools

param_idx = np.array([1,2,3,4,5])

# 有序排列
for comb in itertools.combinations(param_idx, 3):
    print(list(comb))
    
# 无序排列（全排列）
for comb in itertools.permutations(param_idx, 3):
    print(list(comb))