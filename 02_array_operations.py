import numpy as np

# ======================================================
# 1. Element-wise Array Operations (Uncomment to Use)
# ======================================================

# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([5, 4, 3, 2, 1])

# Element-wise Addition
# add_result = arr1 + arr2
# print("\nElement-wise Addition:")
# print(add_result)

# Element-wise Multiplication
# mul_result = arr1 * arr2
# print("\nElement-wise Multiplication:")
# print(mul_result)

# ======================================================
# 2. Array Slicing and Stepping
# ======================================================

arr = np.array([10, 20, 30, 40, 50, 60])
# Indexes:       0   1   2   3   4   5

# Slice from index 1 to 4 (end index is exclusive)
sliced_array = arr[1:5]
print("\nSliced Array [1:5]:")
print(sliced_array)

# Slice with a step of 2 (every second element)
step_sliced_array = arr[::2]
print("\nStep Sliced Array [::2]:")
print(step_sliced_array)
