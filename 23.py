print("09/09/2026") 
# 1 define two matrix (A,B) of 3x3 order using numpy perform the following operation on the matrices 

import numpy as np
A = np.array([[1, 2, 3], [0, 1, 4], [0, 0, 1]])
print("Matrix A:")
print(A)
B = np.array([[2, 0, 1], [3, 0, 0], [5, 1, 1]])
print("Matrix B:")
print(B)
# i) Find out the inverse of matrix A
A_inverse = np.linalg.inv(A)
print("Inverse of matrix A:")
print(A_inverse)

# ii) Find out the determinant of matrix B
det_B = np.linalg.det(B)
print("Determinant of matrix B:", det_B)
print(det_B)

# iii) print the result of a*a inverse
result = np.dot(A, A_inverse)
print("Result of A * A_inverse:")
print(result)