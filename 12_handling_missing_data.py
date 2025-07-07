import numpy as np

# Create a data with missing values
data = np.array([1, 2, np.nan, 4, 5, 6, 7, np.nan, 9, 10])

# Print the original data
print("\nOriginal Data:\n", data)

# True at missing value position
print("\nMissing Values:\n", np.isnan(data))

# Replace all the NANs with -1
data_replaced = np.nan_to_num(data, nan = -1)

# Print the replaced data
print("\nReplaced NANs with -1:\n", data_replaced)

# Well, for those who don't know, NAN stands for Not-A-Number

# Remove all the replaced/data with NAN
data_removed = data[~np.isnan(data)]

# Print the data with missing values removed
print("\nRemoved the missing/replaced data\n", data_removed)