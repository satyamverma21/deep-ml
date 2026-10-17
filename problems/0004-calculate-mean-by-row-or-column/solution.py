def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	# mat = zip(*matrix) if mode == "column" else matrix
	# return [sum(r)/len(r) for r in mat]


	import numpy as np
	return np.asarray(matrix).mean(axis=0 if mode=="column" else 1).tolist()
