import numpy as np

# array1 = np.array([1, 2, 3, 4, 5])
# array2 = np.array([10, 20, 30, 40, 50])
#
# addition_result = np.add(array1, array2)
# print("\nAddition Result\n", addition_result)
#
# subtraction_result = np.subtract(array2, array1)
# print("\nSubtraction Result\n", subtraction_result)

# ====================================================== #

angles = np.array([0, np.pi/2, np.pi, 3*np.pi/2, np.pi])

sine_result = np.sin(angles)
print("Sine Result:\n", sine_result)

cosine_result = np.cos(angles)
print("Cosine Result:\n", cosine_result)
