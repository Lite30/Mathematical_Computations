The code implements the Jacobi method for solving a system of linear equations Ax=b,
where A is the coefficient matrix, b is the column vector, 
and x is the solution vector. 

Function Definition:

    1. jacobi(A, b, x0, tol=1e-10, max_iter=1000): Defines the Jacobi method function.
    2. Takes the coefficient matrix A, column vector b, initial guess x0, and optional parameters for tolerance and maximum iterations.
    3. Returns the solution x and the number of iterations num_iter.

Algorithm:

    Uses a while loop to iterate until convergence or reaching the maximum number of iterations.
    For each iteration:
        1. Calculates the new values of x using the Jacobi iteration formula.
        2. Checks for convergence based on the Euclidean norm of the difference between current and previous x.
        3. Updates x and increments the iteration count.
