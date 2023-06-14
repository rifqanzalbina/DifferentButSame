# Import Library
import numpy as np

# NumPy Program to find missing data in a given array 

# === Codes ===
num = np.array([[3,2,np.nan,1],
               [10,12,10,9],
               [5, np.nan, 1, np.nan]])

print("The Array : ")
print(num)
print("Find the missing data of the said array : ")
print(np.isnan(num))
# === EndCodes ===
