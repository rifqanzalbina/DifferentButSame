# Import the library
import numpy as np

# test element-wise for complex numbers, real numbers in a given array. 
# Also test if a given number is of a scalar type or not. 

# --- Code ---

x = np.array([-1+1j,1+0j,4.5,3,2,2j])
print("The Sample Array")
print(x)

print("Checking for complex number : ")
print(np.iscomplex(x))

print("Checking for A real number : ")
print(np.isreal(x))

print("Checking the scalar type : ")
print(np.isscalar(3.1))
print(np.isscalar([3.1]))

# --- EndCode --- 


