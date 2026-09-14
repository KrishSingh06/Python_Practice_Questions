print("09/09/2026")

# consider a sq matrix & use the following method after print the result with explanation 
#i) qr ii) svd iii)lstsq 

import numpy as np
from scipy import linalg
A = np.array([[12, -51, 4],[6, 167, -68], [-4, 24, -41]])
b = np.array([1, 2, 3], dtype=float)

# i) QR Decomposition
Q, R = linalg.qr(A)

# ii) SVD Decomposition
U, s, Vh = linalg.svd(A)

# iii) Least Squares (Finds vector x that minimizes ||Ax - b||)
x, residuals, rank, singular_vals = linalg.lstsq(A, b)

# --- Print Results ---
print("=== Original Matrix A ===")
print(A)

print("\n=== i) QR Decomposition ===")
print("Orthogonal Matrix Q:\n", Q)
print("Upper Triangular Matrix R:\n", R)

print("\n=== ii) SVD Decomposition ===")
print("Left Singular Vectors U:\n", U)
print("Singular Values (s):\n", s)
print("Right Singular Vectors (Vh):\n", Vh)

print("\n=== iii) Least Squares (lstsq) ===")
print("Optimal Solution vector x:\n", x)
print("Residuals (Sum of squared errors):\n", residuals)
print("Effective Rank of A:\n", rank)