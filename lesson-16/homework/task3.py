import numpy as np



# Define the coefficient matrix A and the constant matrix b
A = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
b = np.array([7, 4, 5])

# Solve the system of equations
solution = np.linalg.solve(A, b)

print("Solution for x, y, z:", solution)
