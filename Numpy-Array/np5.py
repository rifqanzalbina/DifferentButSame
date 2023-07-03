import numpy as np

mat = np.random.randint(10, size=(3,3))

print("Matriks : ")
print(mat)

# Subset
subset = mat[1:, :2]
print("Subset : ")
print(subset)

# Transpose
transpose = subset.T
print("Transpose : ")
print(transpose)

# Inverse
inverse = np.linalg.inv(transpose)
print("Invers : ")
print(inverse)



