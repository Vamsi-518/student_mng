def tuple_elementwise(op, a: tuple, b: tuple) -> tuple:
    return tuple(op(x, y) for x, y in zip(a, b))

a = (10, 4, 6, 9)
b = (5, 2, 3, 3)
print(tuple_elementwise(lambda x, y: x ^ y, a, b))  
print(tuple_elementwise(lambda x, y: x + y, (2,5,8), (3,4,7)))