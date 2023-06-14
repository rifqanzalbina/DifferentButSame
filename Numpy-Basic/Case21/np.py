# Import Library
import numpy as np

# === Codes ====

# NumPy Program to add Elements to a matrix , if an element in the matrix is 0, we will not add the element below this element 
def sum_matrix_elements(m):
    arr = np.array(m)
    element_sum = 0
    for p in range(len(arr)):
        for q in range(len(arr[p])):
            if arr[p][q] == 0 and p < len(arr) - 1:
                arr[p+1][q] = 0
            element_sum += arr[p][q]
    return element_sum

m = [[1,1,0,2],
     [0,3,0,3],
     [1,0,4,4]]
print("The original array : ")
print(m)
print("SUM : ")
print(sum_matrix_elements(m))