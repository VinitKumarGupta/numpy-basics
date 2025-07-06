import numpy as np

data = np.array([10, 20, 30, 30, 40, 50, 50, 50, 60, 70, 80, 90])

mean_value = np.mean(data)
median_value = np.median(data)
standard_deviation = np.std(data)

print(f"\nMean: {mean_value}, Median: {median_value}, Standard Deviation: {standard_deviation}")