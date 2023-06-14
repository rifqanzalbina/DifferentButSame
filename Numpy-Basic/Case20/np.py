# Import Library
import numpy as np

# === Codes ===
x = np.array([0,1],[2,3])
print("The Sample Array : ")
print(x)

print("The sum of all elements in the array : ")
print(np.sum(x))

print("Sum of each column in the array : ")
print(np.sum(x,axis=0))

print("Sum of each row in the array : ")
print(np.sum(x,axis=1))
# === EndCodes ===