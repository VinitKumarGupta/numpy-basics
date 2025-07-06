import numpy as np

# -------------------------------
# Reshaping a 1D Array to 2D
# -------------------------------

# Uncomment below lines to see reshaping in action

# arr_1D = np.array([1, 2, 3, 4, 5, 6])
# arr_2D_reshaped = arr_1D.reshape(2, 3)

# print("\nOriginal 1D Array:")
# print(arr_1D)

# print("\nReshaped to 2D Array (2x3):")
# print(arr_2D_reshaped)

# -------------------------------
# Flattening a 2D Array to 1D
# -------------------------------

arr_2D = np.array([
    [2, 4, 1],
    [2, 9, 10],
    [7, 6, 3]
])

flattened_array = arr_2D.flatten()

print("\nOriginal 2D Array:")
print(arr_2D)

print("\nFlattened 1D Array:")
print(flattened_array)
