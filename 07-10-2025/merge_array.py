import array
a1 = array.array('i', [1, 2, 3])
a2 = array.array('i', [4, 5, 6])
merged = array.array('i')
merged = a1 + a2
print("Array 1:", a1)
print("Array 2:", a2)
print("Merged:", merged)
