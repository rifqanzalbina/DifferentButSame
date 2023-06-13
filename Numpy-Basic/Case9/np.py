# Import library
import numpy as np

# program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays

# --- Code ---
x = np.array([3,5])
y = np.array([2,5])
print("A Sample Array")
print(x)
print(y)

print()

print("Comparison - greater")
print(np.greater(x,y))

print()

print("Comparison - greater_equal")
print(np.greater_equal(x,y))

print()

print("Comparison - less")
print(np.less(x,y))

print()

print("Comparison - less_equal")
print(np.less_equal(x,y))
# --- Endcode