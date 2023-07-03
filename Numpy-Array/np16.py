import numpy as np
import matplotlib.pylab as plt
x = np.linspace(-np.pi,np.pi,201)
plt.plot(x, np.sin(x))
plt.xlabel('Angle[rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()