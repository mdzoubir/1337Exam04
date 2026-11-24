def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:

    out = [["."] * dim for _ in range(dim)]

    for x,y in stars:
        if x >= dim or y >= dim or x < 0 or y <0:
            continue
        out[x][y] = "*"

    return["".join(i) for i in out ]

print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))  # Expected: ['*..', '.*.', '..*']
print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))  # Expected: ['.*.', '***', '.*.']
print(constellation_mapper([], 2))  # Expected: ['..', '..']
print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))  # Expected: ['*.', '.*']
print(constellation_mapper([(0, 0), (5, 5)], 3))  # Expected: ['*..', '...', '...']
print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))  # Expected: ['...', '***', '...']




