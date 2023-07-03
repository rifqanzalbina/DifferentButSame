import numpy as np

arr = np.random.randint(10, size=15)

print("Array 1D :")
print(arr)

mean = np.mean(arr)
print("Rata - rata : ", mean)

median = np.median(arr)
print("Median : ", median)

std = np.std(arr)
print("Standar deviasi : ", std)

