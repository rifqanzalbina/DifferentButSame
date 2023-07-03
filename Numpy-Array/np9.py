import numpy as np

a = np.arange(15)**2

print(a)

print('elemen ke 5 dari a adalah : ', a[5])
print('elemen ke 5 dari a adalah : ', a[-1])

print('elemn dari 1-6 adalah : ', a[0:5])
print('elemen ke 5 dari a adalah : ', a[4:])
print('elemen ke awal sampai 5 adalah : ', a[:5])

for i in a:
    print('value = ', i)