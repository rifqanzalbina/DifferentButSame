# Import library
import numpy as np

# Test elements-wise for positive or negative infinity. 

# --- Code ---

a = np.array([1,2,3,np.nan,np.inf,4])
print("The Sample Array")
print(a)

print()

print("Test program to Test a given array Elements wise for finitness : ")
print(np.isfinite(a)) # Test element-wise for finiteness (not infinity or not Not a Number).

# --- EndCode ---