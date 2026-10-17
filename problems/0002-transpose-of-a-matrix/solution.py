def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    import numpy
    # return [list(i) for i in zip(*a)]
    # return list(map(list, zip(*a)))
    return numpy.array(a).T