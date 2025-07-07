import numpy as np

# ============================================
# 1. Calculating Dot product
# ============================================

# matrix1 = np.array([[1, 2], [3, 4]])
# matrix2 = np.array([[5, 6], [7, 8]])

# dot_product = np.dot(matrix1, matrix2)
# print("\nMatrix 1:\n", matrix1)
# print("\nMatrix 2:\n", matrix2)
# print("\nDot product result:\n", dot_product)

# result_set = matrix1 @ matrix2
# print("\nDot product using @:\n", result_set)

"""
The @ symbol in NumPy, as used in matrix1 @ matrix2, 
is an operator introduced in Python 3.5 for matrix multiplication.
It is essentially a shorthand or syntactic sugar for np.dot() when 
performing matrix multiplication between two NumPy arrays.
"""

# ============================================
# 2. Solving a system of linear equations
# ============================================
"""
Solve A·x = B
Where: 
- A is the coefficient matrix
- x is the unknown solution vector
- B is the constant vector
"""

# Define the coefficient matrix (A)
A = np.array([[3, 1], 
              [1, 2]])

# Define the constant vector (B)
B = np.array([9, 8])

# Solve for x
x = np.linalg.solve(A, B)

# Print results
print("Coefficient Matrix (A):\n", A)
print("Constant Vector (B):\n", B)
print("Solution Vector (x):\n", x)