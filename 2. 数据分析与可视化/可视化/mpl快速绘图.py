import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# plot
plt.plot(np.random.rand(10))
plt.show()

# scatter
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x,y)
plt.show()