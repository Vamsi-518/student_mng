def transpose(matrix: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    return list(zip(*matrix))

mat = [(1, 2, 3),
       (4, 5, 6),
       (7, 8, 9)]
print(transpose(mat))