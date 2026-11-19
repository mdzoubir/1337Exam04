def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    result = []

    for i in range(dim):
        result.append("." * dim)

    for (x, y) in stars:
        if 0 <= x < dim and 0 <= y < dim:
            result[x] = result[x][0:y] + "*" + result[x][y+1:]

    return result


constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)
constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)
constellation_mapper([], 2)
constellation_mapper([(0, 0), (0, 0), (1, 1)], 2)
constellation_mapper([(0, 0), (5, 5)], 3)
constellation_mapper([(1, 0), (1, 1), (1, 2)], 3)
