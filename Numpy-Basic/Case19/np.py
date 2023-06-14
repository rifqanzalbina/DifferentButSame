# Import Library
import numpy as np

# --- Codes ---

# NumPy Program to create 10x10 matrix which element in the borders will be equal to 1 , and inside is 0
x = np.ones((10,10))
x[1:-1, 1:-1] = 0
print(x)

# --- EndCodes ---