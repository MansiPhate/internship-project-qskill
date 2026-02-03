import numpy as np

# Define two matrices
matrix1 = np.array([[1, 2],
                     [3, 4]])

matrix2 = np.array([[5, 6],
                     [7, 8]])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Matrix Addition
addition = matrix1 + matrix2
print("\nMatrix Addition:")
print(addition)

# Matrix Subtraction
subtraction = matrix1 - matrix2
print("\nMatrix Subtraction:")
print(subtraction)

# Matrix Multiplication
multiplication = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(multiplication)

# Transpose of Matrix 1
transpose = matrix1.T
print("\nTranspose of Matrix 1:")
print(transpose)

# Determinant of Matrix 1
determinant = np.linalg.det(matrix1)
print("\nDeterminant of Matrix 1:")
print(determinant)
