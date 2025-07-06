import numpy as np

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

dot_product = np.dot(matrix1, matrix2)
print("\nMatrix 1:\n", matrix1)
print("\nMatrix 2:\n", matrix2)
print("\nDot product result:\n", dot_product)

result_set = matrix1 @ matrix2
print("\nDot product using @:\n", result_set)

"""
The @ symbol in NumPy, as used in matrix1 @ matrix2, 
is an operator introduced in Python 3.5 for matrix multiplication.
It is essentially a shorthand or syntactic sugar for np.dot() when 
performing matrix multiplication between two NumPy arrays.
"""