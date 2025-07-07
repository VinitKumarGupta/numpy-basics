import numpy as np

# ============================================
# 1. Vectorization
# ============================================

"""
- Vectorization is the process of replacing explicit Python 
loops (like for loops) with array expressions that are implemented 
internally in optimized C code (inside NumPy).

- This allows operations on whole arrays at once, instead of element by element.
"""

data = np.array([1, 2, 3, 4, 5])
# data = [1, 2, 3, 4, 5]        - Not Possible in this case, works only with Numpy Arrays!

squared = data ** 2 # Calculates the square of each element instantly

print("\nOriginal Data:\n", data)
print("Squared Output:\n", squared)

# ============================================
# 2. Broadcasting
# ============================================

"""
Broadcasting allows NumPy to perform arithmetic operations on 
arrays of different shapes as long as they are compatible.

For two arrays to broadcast together:

1. Compare their shapes from right to left.
2. Dimensions are compatible if:
    i) They are equal, or
    ii) One of them is 1.
"""

a = np.array([[1], [2], [3]])  # Shape: (3, 1)
b = np.array([10, 20, 30])     # Shape: (3,)

result = a + b
print("\nBroadcasted Result:\n", result)
