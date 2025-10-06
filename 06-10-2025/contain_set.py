fs = frozenset([1, 2, 3, 4])
print("Frozen set:", fs)

print("Contains 2?", 2 in fs)

# Cannot add/remove in frozen set
for i in fs:
    print("Item:", i)