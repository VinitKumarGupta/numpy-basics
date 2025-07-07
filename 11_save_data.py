import numpy as np 

# ======================================================================= #
# Example 1: Save NumPy array to a CSV file using np.savetxt
# ======================================================================= #

# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Sample 2D array

# np.savetxt('./saved_datas/first_data.csv', data, delimiter=',')  
# Save array to a CSV file (comma-separated values)

# print("Data saved to 'first_data.csv' successfully!")  

# ======================================================================= #
# Example 2: Save NumPy array to a plain text file using np.savetxt
# ======================================================================= #

# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  

# np.savetxt('./saved_datas/second_data.txt', data)  
# Save array to a text file (default delimiter is space)

# print("Data saved to 'second_data.txt' successfully!") 

# ======================================================================= #
# Example 3: Save NumPy array in binary format using np.save
# ======================================================================= #

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  

np.save('./saved_datas/third_data.npy', data)  
# Save array in NumPy’s binary .npy format (more efficient for later loading)

print("Data saved to 'third_data.npy' successfully!")
