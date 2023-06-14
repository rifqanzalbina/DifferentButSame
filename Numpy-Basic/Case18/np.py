# Import Library
import numpy as np

# --- Codes ---

x = np.arange(21)
print("The Sample Vector :")
print(x)

print("After Changing the sign of the numbers in the range from 9 to 15")
x[(x >= 10) & (x <= 15)] *= -1   
print(x)

# --- EndCodes ---