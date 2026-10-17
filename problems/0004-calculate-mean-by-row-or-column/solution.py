def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	import numpy as np
	mat = np.asarray(matrix)
	if mode == "column": mat = mat.T

	return list(map(np.mean, mat))


	# return means