def sum_elementwise(*tuples):
    return tuple(sum(values) for values in zip(*tuples))

print(sum_elementwise((1,2,3), (3,5,2), (2,2,3)))
# (6, 9, 8)