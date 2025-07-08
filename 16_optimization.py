import time
import numpy as np

array = np.random.rand(1000000)

def sum_with_loop(arr):
    total = 0
    for num in arr:
        total += num
    return total

def sum_with_numpy(arr):
    return np.sum(arr)

# ================================================== #

loop_start_time = time.time()

sum_by_loop = sum_with_loop(array)

loop_end_time = time.time()

# Time taken by loop to calculate sum of all elements in array
loopTime = loop_end_time - loop_start_time  

print("Sum using loop time: ", f"{loopTime:.3f}")

# ================================================== #

np_start_time = time.time()

sum_by_numpy = sum_with_numpy(array)

np_end_time = time.time()

# Time taken by numpy library to calculate sum of all elements in array
npTime = np_end_time - np_start_time

print("Sum using Numpy time: ", f"{npTime:.3f}")

# ================================================== #

# For more such examples, go to 17_optimExamples.py
