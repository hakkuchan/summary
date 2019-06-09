import numpy as np
import pandas as pd
from sklearn import preprocessing


zeolites_df = pd.read_csv('E:\Work\Jupyter\Data\zeolites.csv')
zeolites = (zeolites_df.values)[:,1:]
np.random.shuffle(zeolites)
heads = ['name', 'crystal_sys', 'space_group', 'a', 'b', 'c', 'alpha', 'beta', 'gamma', 'vol', 'RDLS', 'FDS',
         'TD10', 'TD', 'ring_size', 'dim_topo', 'inc_sphere', 'diff_a', 'diff_b', 'diff_c', 'access_vol']
for num, head in enumerate(heads):
    locals()[head] = zeolites[:,num].reshape(-1,1)


y = crystal_sys.ravel()
print(y[0:5])

# 关键代码
new_y = preprocessing.LabelEncoder().fit_transform(crystal_sys.ravel())
print(new_y[0:5])