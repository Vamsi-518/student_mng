a = {1, 2, 3, 4}
b = {2, 3, 5}
c = {2, 3, 6}

result = a.intersection(b, c)
print("Common elements in A, B, C:", result)

if result:
    print("Intersection found!")
else:
    print("No common elements")