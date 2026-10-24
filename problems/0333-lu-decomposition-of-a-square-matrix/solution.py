import numpy as np

def lu_decomposition(A: list) -> tuple:
    """
    Perform LU decomposition on a square matrix using Doolittle's method.
    
    Args:
        A: Square matrix as a list of lists
        
    Returns:
        tuple: (L, U) where L is lower triangular with 1s on diagonal,
               U is upper triangular, and A = L @ U
    """
    # Convert input to a numpy array for easier sizing and manipulation
    A = np.array(A, dtype=float)
    n = A.shape[0]
    
    # Initialize L as an identity matrix and U as a zero matrix
    L = np.eye(n, dtype=float)
    U = np.zeros((n, n), dtype=float)
    
    # Doolittle's algorithm steps
    for i in range(n):
        # Upper Triangular Matrix U
        for k in range(i, n):
            # Sum of L[i][j] * U[j][k]
            s = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - s
            
        # Lower Triangular Matrix L
        for k in range(i + 1, n):
            # Sum of L[k][j] * U[j][i]
            s = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (A[k][i] - s) / U[i][i]
            
    return L, U
