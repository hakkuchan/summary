import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

""" 设置画布 """
fig = plt.figure(figsize=(10,6), facecolor='gray')

""" 子图 1 """
ax1 = fig.add_subplot(2,2,1)
plt.plot(np.random.rand(50).cumsum(),'k--')

""" 子图 2 """
ax2 = fig.add_subplot(2,2,2)
ax2.hist(np.random.rand(50),alpha=0.5)

""" 子图 3 """
ax3 = fig.add_subplot(2,2,3)
df2 = pd.DataFrame(np.random.rand(10,4), columns=['a', 'b', 'c', 'd'])
ax3.plot(df2,alpha=0.5,linestyle='--',marker='.')

plt.show()