# Import library
import numpy as np

# --- Code ----
a = np.array([1,0,np.nan, np.inf])
print("The Sample Array")
print(a)

print()

print("Test element wise for NaN")
print(np.isnan(a))
# --- EndCode ---

