import numpy as np

a = np.floor(np.random.randn(1,10)*5)


print(a)
print('nilai maximum dari a : ',a.min())
print('nilai posisi maximum dari a : ',a.argmin())
print('nilai maximum dari a : ',a.max())
print('nilai posisi minimum dari a : ',a.argmax())

print('mengurutkan nilai a : ')
print(np.sort(a))

