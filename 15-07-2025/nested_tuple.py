from collections.abc import Iterable

def flatten(nested) -> tuple:
    result = []
    for item in nested:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return tuple(result)

nested = (1, (2, [3, (4, 5)], 6), 7, ((8,)))
print(flatten(nested))