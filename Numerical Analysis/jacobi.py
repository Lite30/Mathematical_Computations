import numpy as np

def jacobi(A, b, x0, tol=1e-10, max_iter=1000):
    """
    Jacobi method for solving a system of linear equations Ax = b
    
    Parameters:
        A (numpy.ndarray): Coefficient matrix (n x n)
        b (numpy.ndarray): Column vector (n x 1)
        x0 (numpy.ndarray): Initial guess for x (n x 1)
        tol (float): Tolerance for convergence
        max_iter (int): Maximum number of iterations
    
    Returns:
        x (numpy.ndarray): Solution vector (n x 1)
        num_iter (int): Number of iterations performed
    """
    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x)
    num_iter = 0
    
    while num_iter < max_iter:
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i, j] * x[j]
            x_new[i] = (b[i] - sigma) / A[i, i]
        
        if np.linalg.norm(x_new - x) < tol:
            break
        
        x = x_new.copy()
        num_iter += 1
    
    return x, num_iter

# Example usage
A = np.array([[10, 2, 1], 
              [1, 5, 1], 
              [2, 3, 10]], 
              dtype=float)

b = np.array([7, -8, 6], dtype=float)
x0 = np.array([0, 0, 0], dtype=float)

solution, iterations = jacobi(A, b, x0)
print("Solution:", solution)
print("Number of iterations:", iterations)
