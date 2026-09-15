import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    rows, cols = new_shape

    if len(a) * len(a[0]) != rows * cols:
        return []

    res = np.reshape(a, new_shape)

    return res.tolist()