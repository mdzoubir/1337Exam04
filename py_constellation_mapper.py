def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    out = [["."] *dim for _ in range(dim)]
    for x, y in stars:
        if not (0 <= x<= dim and 0<=y<=dim):
            continue
        out[x][y] = "*"
    return ["".join(line) for line in out]


print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))  # Expected: ['*..', '.*.', '..*']
print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))  # Expected: ['.*.', '***', '.*.']
print(constellation_mapper([], 2))  # Expected: ['..', '..']
print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))  # Expected: ['*.', '.*']
print(constellation_mapper([(0, 0), (5, 5)], 3))  # Expected: ['*..', '...', '...']
print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))  # Expected: ['...', '***', '...']