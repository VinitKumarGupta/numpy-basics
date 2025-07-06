import numpy as np

# Creating a NumPy array with elements 1, 2, 3, 4
myArr = np.array([1, 2, 3, 4])

# -----------------------------------------------
# Using .copy() creates a completely independent copy of the array.
# Changes made to the copy do NOT affect the original array.
# -----------------------------------------------

print("\n======================= COPYING ARRAY =======================")

copyArr = myArr.copy()
print("\nOriginal Array:\n", myArr)
print("\nCopied Array:\n", copyArr)

print("\nBoth array' state after modification:")

copyArr[0] = 10
print("\nOriginal Array:\n", myArr)
print("\nCopied Array:\n", copyArr)

# -----------------------------------------------
# Using .view() creates a new array object that **shares the same data** as the original.
# Any changes made to the data (not shape) in one will reflect in the other.
# However, the two are still distinct array objects (i.e., different memory for array object,
# but same memory for data).
# -----------------------------------------------

print("\n======================= VIEWING ARRAY =======================")


viewArr = myArr.view()
print("\nOriginal Array:\n", myArr)
print("\nViewed Array:\n", viewArr)

print("\nBoth array' state after modification:")

viewArr[0] = 10
print("\nOriginal Array:\n", myArr)
print("\nViewed Array:\n", viewArr)
