import numpy as np

# ========================================================== #
# 1. Stacking Arrays Horizontally and Vertically
# ========================================================== #

# Uncomment as you go :)

# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 10])

# To stack both the vectors horizontally
# h_stacked_arr = np.hstack((arr1, arr2))
# To stack both the vectors vertically
# v_stacked_arr = np.vstack((arr1, arr2))

# print("\nHorizontally Stacked array: \n", h_stacked_arr)
# print("\nVertically Stacked array: \n", v_stacked_arr)

# ========================================================== #
# 2. Splitting Arrays Horizontally and Vertically
# ========================================================== #

# myArray = np.array([[1, 2, 3, 4, 5, 6],
#                     [7, 8, 9, 10, 11, 12]])

# Horizontal split into 3 parts (splits columns)
# h_split_array = np.hsplit(myArray, 3)

# Vertical split into 2 parts (splits rows)
# v_split_array = np.vsplit(myArray, 2)

# print("\nOriginal Array:")
# print(myArray)

# print("\nHorizontally Split Arrays (Split Columns):")
# for i, arr in enumerate(h_split_array, 1):
#     print(f"Part {i}:\n{arr}")

# print("\nVertically Split Arrays (Split Rows):")
# for i, arr in enumerate(v_split_array, 1):
#     print(f"Part {i}:\n{arr}")
