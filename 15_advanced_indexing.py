import numpy as np

# ten_numbers = np.arange(10)

# even_numbers = ten_numbers[ten_numbers % 2 == 0]

# print("Original Array: ", ten_numbers)
# print("Even Numbers: ", even_numbers)

# ============================================================== #

matrix = np.array([[10, 20, 30], 
                   [40, 50, 60], 
                   [70, 80, 90]])

selected_elements = matrix[[0, 1, 2], [2, 0, 1]]

print("\nOriginal Matrix: \n", matrix)
print("\nSelected Elements: \n", selected_elements)

"""
At first glance that indexing looks like black magic. 😅 
but don't worry. Let's break it down step by step.

When you do:
matrix[[0, 1, 2], [2, 0, 1]]

NumPy pair these two arrays as:
matrix[(0, 2), (1, 0), (2, 1)]    --> (row, column) of matrix

Hence, you get:
[30 40 80]
"""
