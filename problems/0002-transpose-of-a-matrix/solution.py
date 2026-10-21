import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    a = np.array(a)
    result = np.transpose(a)
    return result.tolist()
    pass