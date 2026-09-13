# Creating sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)
print()

# Add element
A.add(7)
print("After adding 7 to A:", A)

# Remove element
A.remove(7)
print("After removing 7 from A:", A)

# Discard element (no error if missing)
A.discard(10)  # 10 not in A, no error
print("After discarding 10 from A:", A)

print()

# Set union (all unique elements from both sets)
union = A | B
print("Union of A and B:", union)

# Set intersection (elements common to both)
intersection = A & B
print("Intersection of A and B:", intersection)

# Set difference (elements in A but not in B)
difference = A - B
print("Difference A - B:", difference)

# Set symmetric difference (elements in either A or B but not both)
sym_diff = A ^ B
print("Symmetric difference of A and B:", sym_diff)

print()

# Check subset and superset
print("Is A subset of B?", A <= B)
print("Is B superset of A?", B >= A)

# Check disjoint (no common elements)
print("Are A and B disjoint?", A.isdisjoint(B))

print()

# Copy sets
C = A.copy()
print("Copy of A:", C)

# Frozen set (immutable set)
frozen = frozenset([1, 2, 3])
print("Frozen set:", frozen)