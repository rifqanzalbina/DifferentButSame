# Import Library
import numpy as np

# === Codes ===

#NumPy program to create a new array of given shape (5,6) and type, filled with zeros.
#Change the said array in the following format
num = np.zeros(shape=(5,6), dtype='int')
print("The Array : ")
print(num)

num[::2,::2] = 3
num[1::2,::2] = 7

print("New Array : ")
print(num)

# === EndCodes ===