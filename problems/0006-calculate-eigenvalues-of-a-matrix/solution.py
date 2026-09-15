import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	eigenvalues= np.linalg.eig(matrix)
	return eigenvalues[0]