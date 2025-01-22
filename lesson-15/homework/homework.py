import numpy as np

# Task 1: Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)
print("Vector (10 to 49):\n", vector)

# Task 2: Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("\n3x3 Matrix (0 to 8):\n", matrix_3x3)

# Task 3: Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("\n3x3 Identity Matrix:\n", identity_matrix)

# Task 4: Create a 3x3x3 array with random values
random_array = np.random.rand(3, 3, 3)
print("\n3x3x3 Random Array:\n", random_array)

# Task 5: Create a 10x10 array with random values and find the minimum and maximum values
random_10x10 = np.random.rand(10, 10)
min_value = np.min(random_10x10)
max_value = np.max(random_10x10)
print("\n10x10 Random Array:\n", random_10x10)
print("Min value:", min_value)
print("Max value:", max_value)

# Task 6: Create a random vector of size 30 and find the mean value
random_vector = np.random.rand(30)
mean_value = np.mean(random_vector)
print("\nRandom Vector (size 30):\n", random_vector)
print("Mean value:", mean_value)

# Task 7: Normalize a 5x5 random matrix
random_matrix_5x5 = np.random.rand(5, 5)
normalized_matrix = (random_matrix_5x5 - np.min(random_matrix_5x5)) / (np.max(random_matrix_5x5) - np.min(random_matrix_5x5))
print("\nNormalized 5x5 Random Matrix:\n", normalized_matrix)

# Task 8: Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)
matrix_product = np.dot(matrix_5x3, matrix_3x2)
print("\nMatrix Product (5x3 * 3x2):\n", matrix_product)

# Task 9: Create two 3x3 matrices and compute their dot product
matrix_A = np.random.rand(3, 3)
matrix_B = np.random.rand(3, 3)
dot_product = np.dot(matrix_A, matrix_B)
print("\nDot Product of 3x3 Matrices:\n", dot_product)

# Task 10: Given a 4x4 matrix, find its transpose
matrix_4x4 = np.random.rand(4, 4)
transpose_matrix = np.transpose(matrix_4x4)
print("\nTranspose of 4x4 Matrix:\n", transpose_matrix)

# Task 11: Create a 3x3 matrix and calculate its determinant
matrix_3x3 = np.random.rand(3, 3)
determinant = np.linalg.det(matrix_3x3)
print("\n3x3 Matrix Determinant:", determinant)

# Task 12: Create two matrices (A) (3x4) and (B) (4x3), and compute the matrix product (A . B)
matrix_A = np.random.rand(3, 4)
matrix_B = np.random.rand(4, 3)
matrix_product_AB = np.dot(matrix_A, matrix_B)
print("\nMatrix Product of A (3x4) and B (4x3):\n", matrix_product_AB)

# Task 13: Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product
matrix_3x3 = np.random.rand(3, 3)
column_vector = np.random.rand(3, 1)
matrix_vector_product = np.dot(matrix_3x3, column_vector)
print("\nMatrix-Vector Product (3x3 * 3x1):\n", matrix_vector_product)

# Task 14: Solve the linear system (Ax = b) where (A) is a 3x3 matrix, and (b) is a 3x1 column vector
A = np.random.rand(3, 3)
b = np.random.rand(3, 1)
x = np.linalg.solve(A, b)
print("\nSolution of the Linear System (Ax = b):\n", x)

# Task 15: Given a 5x5 matrix, find the row-wise and column-wise sums
matrix_5x5 = np.random.rand(5, 5)
row_sums = np.sum(matrix_5x5, axis=1)
column_sums = np.sum(matrix_5x5, axis=0)
print("\n5x5 Matrix:\n", matrix_5x5)
print("Row-wise sums:", row_sums)
print("Column-wise sums:", column_sums)
