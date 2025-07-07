import numpy as np

# Generate a single random number between 0 and 1
random_number = np.random.rand()
print("\nRandom number between 0 and 1:\n", random_number)

# Generate a 3x2 array of random numbers between 0 and 1, then scale to 0–10
random_array = np.random.rand(3, 2) * 10
print("\nRandom array with values between 0 and 10:\n", random_array)

# Generate 10 random samples between 0 and 1 (not actually normal distribution)
normal_samples = np.random.rand(10)
print("\nRandom samples from a uniform distribution (0 to 1):\n", normal_samples)
