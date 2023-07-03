import numpy as np
import matplotlib.pylab as plt
x = np.linspace(-1,1,num=10)
plt.plot(x,np.arccos(x))
plt.axis('square')
plt.show()