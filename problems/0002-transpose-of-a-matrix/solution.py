def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:

    # return [list(i) for i in zip(*a)]
    return list(map(list, zip(*a)))