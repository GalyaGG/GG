import numpy as np


def generate_random_ndarray(n: int = 5, p: int = 8, mean: float = 0.0, std: float = 3.0) -> np.ndarray:
    shape = (n, p)
    matrix = np.random.normal(loc=mean, scale=std, size=shape)
    return matrix
