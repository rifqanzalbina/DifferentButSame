# Import Library
import numpy as np

# NumPy Program to create an array With the Values " X Var " and determine the size of the memory occupied by the Array  

# --- Code ---

X = np.array([1,8,9,13,105 ])
print("The sample Array : ")
print(X)
print("Size of the memory occupied by the sample Array : ")
print("%d bytes" % (X.size * X.itemsize)) # To Tell The Memory Size of the Array "X"

# --- EndCode ---