import numpy as np
# STACKING
a = np.array([1,3,5])
b = np.array([2,4,6])

aMat = np.zeros((3,3))
bMat = np.ones((3,3))

c = np.hstack((a,b))
d = np.vstack((b,a))

cMat = np.hstack((aMat,bMat))
bMat = np.vstack((bMat,aMat))

print(cMat)
print(bMat)

print(c)
print(d)

