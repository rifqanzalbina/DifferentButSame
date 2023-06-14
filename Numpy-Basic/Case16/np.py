# Import Library
import numpy as np

# --- Codes ---

# NumPy Program to make a Automate Array using "Arange and reshape"
# Arrange Is To Make a Element in the array from Start to End 
# Reshape is To Make a Size Of Element in the Array 
a = np.arange(0,20).reshape((4,5))    
print("The Sample Array 'a' : ")
print(a)
print("Each Element Of the Sample Array : ")
for x in np.nditer(a):
    print(x,end=" ")

# --- EndCodes ---

