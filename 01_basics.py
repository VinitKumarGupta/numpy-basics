"""
NumPy is an open-source library for numerical and scientific computing in Python.
It provides support for multi-dimensional arrays, matrices, and high-level mathematical functions.
"""

import numpy as np

# ======================================================
# 1. Creating and Accessing a NumPy Array
# ======================================================

# Uncomment below to see basic array creation and element access

# arr = np.array([1, 2, 3, 4, 5])
# print("\nArray created:\n", arr)
# print("First element:", arr[0])
# print("Last element:", arr[-1])

# ======================================================
# 2. Creating a 2D Matrix
# ======================================================

# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
# print("\n2D Matrix (3x3):")
# print(matrix)

# ======================================================
# 3. Matrix Operations (Addition and Scalar Multiplication)
# ======================================================

# matrix1 = np.array([[1, 2],
#                     [3, 4]])
# matrix2 = np.array([[5, 6],
#                     [7, 8]])

# Element-wise addition
# added_matrix = matrix1 + matrix2
# print("\nMatrix Addition:\n", added_matrix)

# Scalar multiplication
# scalar_multiplied_matrix = matrix1 * 3
# print("\nMatrix multiplied by scalar (3):\n", scalar_multiplied_matrix)

# ======================================================
# 4. Creating Arrays with Utility Functions
# ======================================================

# array_from_list = np.array([2, 4, 6, 8, 9, 10])
# print("\nArray from List:")
# print(array_from_list)

# Array of all zeros (size = 5)
# zeros_array = np.zeros(5)
# print("\nArray of Zeros:")
# print(zeros_array)

# Array of all ones (size = 5)
# ones_array = np.ones(5)
# print("\nArray of Ones:")
# print(ones_array)

# Array with a range of numbers (start=1, stop=11, step=2)
# range_array = np.arange(1, 11, 2)  # 11 is excluded
# print("\nArray with range from 1 to 10 (step=2):")
# print(range_array)
