import time
import numpy as np

arr1 = np.random.rand(1000000)
arr2 = np.random.rand(1000000)

# Example 1: Adding two arrays using a loop
loop_start = time.time()

loop_sum = []
for i in range(len(arr1)):
    loop_sum.append(arr1[i] + arr2[i])

loop_end = time.time()
loop_duration = loop_end - loop_start
print("Sum using loop: ", f"{loop_duration:.4f}")

# ============================================

# Example 2: Adding two arrays using NumPy
np_start = time.time()

np_sum = arr1 + arr2

np_end = time.time()
np_duration = np_end - np_start
print("Sum using NumPy: ", f"{np_duration:.4f}")

# ============================================
