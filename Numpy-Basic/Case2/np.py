# Import Libraries
import numpy as np

# Test whether none of the elements of a given array are zero. 

# --- Code ----

x = np.array([1,2,3,4,5])
print("A Sample Array : ")
print(x)

print("Test program to whether none of the elements of a given array are zero.")
print("The answer : ",np.all(x)) # This fucntion is tes array elements given a axis evaluate to True

print()

y = np.array([0,1,2,3,4,5])
print("A Sample Array")
print(y)

print("Test program to whether none of the elements of a given array are zero.")
print("The answer : ",np.all(y))

# --- EndCode ---