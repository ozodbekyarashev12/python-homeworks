import numpy as np



def power(base, exponent):
    return base ** exponent

# Vectorize the function using numpy.vectorize
vectorized_power = np.vectorize(power)

# Arrays for base and exponent
base_array = np.array([2, 3, 4, 5])
exponent_array = np.array([1, 2, 3, 4])

# Apply the vectorized function
result = vectorized_power(base_array, exponent_array)

print("Base Array:", base_array)
print("Exponent Array:", exponent_array)
print("Power Results:", result)
