import numpy as np

def gaussian_elimination(A, b):
    M = A.copy().astype(float)
    rhs = b.copy().astype(float)
    n = len(M)

    for i in range(n - 1):
        pivot_row = i + np.argmax(np.abs(M[i:, i]))

        M[[i, pivot_row]] = M[[pivot_row, i]]
        rhs[[i, pivot_row]] = rhs[[pivot_row, i]]

        if M[i, i] == 0:
            raise ValueError("The system does not have a unique solution.")

        for j in range(i + 1, n):
            factor = M[j, i] / M[i, i]
            M[j, i:] -= factor * M[i, i:]
            rhs[j] -= factor * rhs[i]

    if M[n - 1, n - 1] == 0:
        raise ValueError("The system does not have a unique solution.")

    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (
            rhs[i] - np.dot(M[i, i + 1:], x[i + 1:])
        ) / M[i, i]

    return x.tolist()