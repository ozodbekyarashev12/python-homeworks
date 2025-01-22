import numpy as np

# Define the conversion function from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Vectorize the function using numpy.vectorize
vectorized_fahrenheit_to_celsius = np.vectorize(fahrenheit_to_celsius)

# Array of temperatures in Fahrenheit
temperatures_fahrenheit = np.array([32, 68, 100, 212, 77])

# Apply the vectorized function
temperatures_celsius = vectorized_fahrenheit_to_celsius(temperatures_fahrenheit)

print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
print("Temperatures in Celsius:", temperatures_celsius)
