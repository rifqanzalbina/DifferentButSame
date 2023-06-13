# Import library
import numpy as np

# Test elements-wise for positive or negative infinity. 

# --- Code ---
a = np.array([1,0,np.nan,np.inf])
print("A Sample Array")
print(a)

print()

print("Test The element wise for positive or negative infinity : ")
print(np.isinf(a)) # The function checks if the elements in the array " " are positive or negative infinity

# --- Encode ---
