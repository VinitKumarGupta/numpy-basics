import numpy as np

# ====================================================
# 1. Creating a matrix of random numbers
# ====================================================

# data = np.random.rand(3, 3)     # Creates a 3x3 matrix of random numbers (< 1)

# print("Random 3x3 Matrix:\n", data)


# ====================================================
# 2. Loading data from csv files (np.loadtxt)
# ====================================================

# data = np.loadtxt('Dataset.csv', delimiter=',')

# print("Dataset loaded:\n", data)

"""
Pros:
- Simple and fast for numeric data.

Cons:
- Fails if there are headers, missing values, or mixed data types (strings and numbers).

Use when: Your CSV contains only numeric data and no headers.
"""

# ====================================================
# 3. Loading data from csv files (np.genfromtxt)
# ====================================================

data = np.genfromtxt('Dataset.csv', delimiter=',', skip_header=1)
print(data)

"""
Pros:
- Can handle missing values ('filling_values' parameter).
- Supports headers (via 'skip_header').
- Handles mixed data types better than loadtxt.

Cons:
- Slower than loadtxt for large numeric-only files.

Use when: Your CSV has missing data or headers.
"""

# ====================================================
# 4. Loading data from .npy or .npz files (np.load)
# ====================================================

data = np.load('Dataset.npy')

"""
Note: This is not for CSVs!
- It loads NumPy's own binary format (.npy or .npz files).
- If your data is in CSV, you can first load it with loadtxt/genfromtxt and save it:

    np.save('Dataset.npy', data)
    
- Then load it later:

    data = np.load('Dataset.npy')
"""