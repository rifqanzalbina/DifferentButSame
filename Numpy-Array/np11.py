import numpy as np

a = np.array((
            [2,4,6],
            [8,10,12]
            ))


print("Matriks a dengan ukuran : ", a.shape)
print(a)

# TRANSPOSE MATRIX
print('transpose matrix dari a : ',a.shape)
print(a.transpose())
print("Matriks a dengan ukuran : ",a.shape)

# FLATTEN
print("flatten matrix a : ")
print(a.ravel())
print(np.ravel(a))
print("Matriks a dengan ukuran : ",a.shape)

# RESHAPE
print("Reshape matrix a : ")
print(a.reshape(3,2))
print("Matriks a dengan ukuran : ",a.shape)

# RESIZE
print("Resize matrix a : ")
a.resize(3,2)
print(a)
print("Matriks a dengan ukuran : ",a.shape)