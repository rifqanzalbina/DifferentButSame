#Import library
import numpy as np

# Program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.

# --- Code ---
x = np.array([72,79,85,90,150,-135,120,-10,60,100])
y = np.array([72,79,85,90,150,-135,120,-10,60,100.000001])

print("The Sample Array : ")
print(x)
print(y)

print()

print("Comparison - equal")
print(np.equal(x,y))

print()

print("Comparison - equal within a tolerance")
print(np.allclose(x,y))
# --- EndCode ---
