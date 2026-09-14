# create a matrix of 4x order and find out the transpose of the matrix and  the rank of the matrix using scipy

from scipy import linalg
import numpy as np

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print("Matrix A:")
print(A)

print("Transpose of Matrix A:")
print(A.T)

rank_A = np.linalg.matrix_rank(A)
print("Rank of Matrix A:", rank_A)