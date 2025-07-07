import numpy as np

data = np.array([(1, 'Alice', 25), 
                 (2, 'Bob', 30), 
                 (3, 'Charlie', 35)], 
                dtype=[('ID', int), ('Name', 'U10'), ('Age', int)])
# U10 means 'Unicode string' (the `U`) which will be of max. 10 characters long (the `10`). i.e, U10

# Display the array reshaped to 3 rows and 1 column for better readability
print("\nData:\n", data.reshape(3, 1))

# Accessing Specific Fields
print("\nNames: \t", data['Name'])
print("\nAges: \t", data['Age'])
