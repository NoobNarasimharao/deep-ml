import numpy as np
def calculate_matrix_mean(a: list[list[float]], mode: str) -> list[float]:
	means=[]
	if mode == 'column':
		means=np.mean(a, axis=0)
	else:
		means=np.mean(a,axis=1)
	return means