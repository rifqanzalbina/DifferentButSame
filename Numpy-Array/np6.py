import numpy as np

arr = np.random.randint(10, size=(2,3,4))

print("Array : ")
print(arr)

subset = arr[:, :2, 1:3]
print("Subset : ")
print(subset)

sum_subset = np.sum(subset)
print("Jumlah pada elemen pada subset : ")
print(sum_subset)

mean_subset = np.mean(subset, axis=(0,1))
print("Mena subset pada setiap axis : ")
print(mean_subset)

min_subset = np.min(subset) 
print("Nilai Maksimum subset : ")
print(min_subset)

max_subset = np.max(subset)
print("Nilai maksimum subset : ")
print(max_subset)

sqrt_subset = np.sqrt(subset)
print("Akar kuadrat subset : ")
print(sqrt_subset)

