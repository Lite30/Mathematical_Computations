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

        print("Solution at iteration", iteration + 1, ":", x_solved)
        
        # Calculate absolute error under the L∞ norm
        error = np.max(np.abs(x_solved - x_guess))
        print("Absolute error at iteration", iteration + 1, ":", error)
        
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != "yes":
            break

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
