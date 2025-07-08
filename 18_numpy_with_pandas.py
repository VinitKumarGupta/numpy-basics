import numpy as np
import pandas as pd

data = np.random.rand(5, 3)

df = pd.DataFrame(data, columns=['A', 'B', 'C'])

print("Numpy Data: \n", data)
print("\nPandas Dataframe: \n", df)
