def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	import numpy as np
	return np.asarray(matrix).mean(axis=0 if mode=="column" else 1).tolist()


	# return means