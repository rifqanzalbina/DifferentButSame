import numpy as np

a = np.array(([1,2],
              [3,5]))
b = np.array(([2,5],
              [2,3]))
print("Matriks A : ")
print(a)

print("Matriks B : ")
print(b)

# c1 = np.dot(a,b)
c2 = a.dot(b)
c3 = b.dot(a)

print("Matriks a * b : ")
print(c2)

print("Matriks b * a : ")
print(c3)

