a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print("A is subset of B?", a.issubset(b))
print("B is superset of A?", b.issuperset(a))

c = {7, 8}
print("C disjoint with A?", a.isdisjoint(c))