import numpy as np

def gauss_seidel(A, B, x0, tolerance=1e-4, max_iter=10000):
    vectorB_len = len(B)
    x_solved = x0.copy()

    # Run a loop over maximum iterations
    for iteration in range(max_iter):
        x_guess = x_solved.copy()
        # Inner loop over the length of the vector B
        # This loop allows for making x1, x2, x3 the subject of the formula
        for i in range(vectorB_len):
            # Initialize the summation
            summation = 0
            for j in range(vectorB_len):
                if j != i:
                    summation += A[i][j] * x_solved[j]
            x_solved[i] = (B[i] - summation) / A[i][i]

    return x_solved

def input_matrix(rows, cols):
    matrix = []
    print("Enter the elements of the matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
# Define 3x3 matrix A in Ax=b
A = input_matrix(rows, cols)
# Define column vector B in Ax=b
B = np.array(input_matrix(cols, 1))
# Initial guess x(0)
x0 = np.array(input_matrix(cols, 1))

# User input
# max_iter = int(input("How many times do you want to iterate? : "))

# ----- Return section ------
solution = gauss_seidel(A, B, x0)
print("Solution:", solution)
