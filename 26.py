print("09/09/2026 ")
# create a square matrix of 4x4 order find out the  eigen values and eigen vectors of the matrix using scipy
# find out the P=permutation ,L=lower triangular ,U=upper triangular matrix of the given matrix using scipy
from scipy import linalg
import numpy as np
A = np.array([[4, 2, 1, 3], [0, 1, -1, 2], [2, 3, 0, 1], [1, -1, 2, 4]])
print("Matrix A:")
print(A)

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = linalg.eig(A)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

# Find P, L, U matrices 
# lu decomposition simply decomposes a mtrix into a lower & upper triangular 
P, L, U = linalg.lu(A)
print("Permutation Matrix P:")
print(P)
print("Lower Triangular Matrix L:")
print(L)
print("Upper Triangular Matrix U:")
print()